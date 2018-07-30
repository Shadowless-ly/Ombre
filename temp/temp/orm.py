import sql
import logging;logging.basicConfig(level=logging.info)
import asyncio

HOST = '127.0.0.1'
DB = 'eureka'

class Model(dict, metaclass=ModelMetaclass):
    """ORM映射的基类

    继承该类可以创建Table类,Table类代表数据库中的一张表,
    每一个实例表示数据库表中的行。
    该类继承了字典类,实现了以属性的方式方位字典的键值。
    实现了对数据库表的增删改查。
    """
    def __init__(self, **kw):
        """以字典方式初始化kw参数
        """
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        """以属性的方式访问字典内容
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        """以属性的方式为字典赋值
        """
        self[key] = value
    
    def getValue(self, key):
        """获取对应键的值
        """
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        """获取对应键的值，若为None，则查询其默认值
        """
        value = getattr(self, key, None)
        if value is None:
            field = self.__mapping__[key]
            if field.default is not None:
                value = field.default if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' %(key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def find(cls, pk):
        """使用主键查询数据库表
        """
        await cls.__sql__.get_sql()
        rs = await cls.__sql__.select('%s where `%s`=?' %(cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await cls.__sql__.select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['__num__']

    @classmethod
    async def findall(cls, where=None, args=None, **kw):
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?', '?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await cls.__sql__.select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    async def save(self):
        """将数据插入到数据库表中
        """
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await self.__sql__.execute(self.__insert__, args)
        if rows != 1:
            logging.warning('failed to insert record: affected rows: %s' % rows)
        
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await self.__sql__.execute(self.__update__, args)
        if rows != 1:
            logging.warning('failed to update by primary key: affected rows: %s ' %rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await self.__sql__.execute(self.__delete__, args)
        if rows != 1:
            logging.warning('failed to remove by primary key: affected row: %s' % rows)


class Field(object):
    """字段类的基类
    """
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default
    
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

class StringField(Field):
    """字符串字段类
    """
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super(StringField, self).__init__(name, ddl, primary_key, default)

class BooleanField(Field):
    """布尔字段类型
    """
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
    """整型字段
    """
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):
    """浮点字段
    """
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):
    """文本字段
    """
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

class ModelMetaclass(type):
    """mode元类

    为Model类的元类,控制Mode子类型(table)的创建,
    将其子类型的类属性中,Field类型保存于__mapings__中,
    Field类型若其属性primary_key为True则保存于__primary_key__中,
    为每个表增加增删改查类属性
    """
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' %(k, v))
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise RuntimeError('Duplicate primary ket for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' %f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`,`%s` from `%s`' %(primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, ', '.join(['?' for i in len(escaped_fields)+1]))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' %(tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' %(tableName, primaryKey)
        loop = asyncio.get_event_loop()
        attrs['__sql__'] = sql.SQL(HOST, DB, loop)
        return type.__new__(cls, name, bases, attrs)

