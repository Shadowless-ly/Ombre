import aiomysql
import asyncio
# import configparser
import logging;logging.basicConfig(level=logging.DEBUG)
import doctest
import unittest

class SQL(object):
    """SQL类，实现了异步创建连接池，提供异步方法执行SQL语句
    """

    instance = {}
    def __new__(cls, host, loop,
                port=3306, user='root', 
                password='ly2951108', db='eureka'):
        """单例模式,同一个(host,db)只能存在一个实例
        """
        if (host,db) in cls.instance.keys():
            return cls.instance.get((host,db))
        else:
            sql = super(SQL, cls).__new__(cls)
            cls.instance.setdefault((host,db), sql)
            return sql
        # if hasattr(cls, 'instance'):
        #     return cls.instance
        # else:
        #     cls.instance = super(SQL, cls).__new__(cls)
        # return cls.instance

    def __init__(self, host, loop,
                port=3306, user='root', 
                password='ly2951108', db='eureka'):
        """
        设置数据库初始化信息
        """
        self.port = port
        self.host = host
        self.user = user
        self.passwd = password
        self.db = db
        self.loop = loop
        self.if_closed = True
    
    async def get_sql(self, create_pool=True):
        if create_pool:
            if self.if_closed:
                logging.info(str((self.host, self.db)) +'pool is colsed, no restart it')
                await self.create_pool()
        logging.info(str((self.host, self.db)) +'get sql')
        return self.instance

    async def create_pool(self):
        """创建连接池
        """
        self.pool = await aiomysql.create_pool(host=self.host, port=self.port, 
                                                user=self.user, password=self.passwd,
                                                db=self.db, loop=self.loop
                                                )
        self.if_closed = False
        logging.info(str((self.host, self.db)) +"create pool")

    async def execute(self, sql, args, cursor_type=None, size=None):
        """建立建立连接,执行sql语句，返回执行结果
        """
        async with self.pool.acquire() as conn:
            self.cursor = await conn.cursor(cursor_type)
            await self.cursor.execute(sql.replace('?', '%s'), args or ())
            if size:
                result = await self.cursor.fetchmany(size)
            else:
                result = await self.cursor.fetchall()
            await self.cursor.close()
            logging.info(str((self.host, self.db)) + 'row return: %s' % len(result))
            logging.debug(str((self.host, self.db)) + str(result))
            return result

    async def close(self):
        """关闭连接池
        """
        self.pool.close()
        await self.pool.wait_closed()
        logging.info(str((self.host, self.db)) +'close pool')


class SQLTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start Test')
        print('<'+'*'*50 +'>')

    def test_run(self):
        async def test_sql1(loop):
            """
            >>> asyncio.iscoroutinefunction(test_sql1)
            True
            >>> id(sql) == id(sql2) != id(sql3)
            """
            sql = SQL('127.0.0.1', loop)
            await sql.create_pool()
            await sql.execute('SELECT ?;', '88')
            await sql.execute('show databases;', '')
            await sql.close()
            sql2 = SQL('127.0.0.1', loop)
            sql3 = SQL('127.0.0.1', loop, db='mysql')
            print('test_sql1:', id(sql), id(sql2), id(sql))


        async def test_sql2(loop):
            """
            >>> asyncio.iscoroutinefunction(test_sql2)
            True
            """
            sql = SQL('127.0.0.1', loop, db="mysql")
            await sql.get_sql()
            await sql.execute('select * from user;', '', cursor_type=aiomysql.DictCursor)
            await sql.execute('show tables;', '')
            print('test_sql2', id(sql))

        loop = asyncio.get_event_loop()
        # print(asyncio.iscoroutinefunction(test_sql1))
        furures = [asyncio.ensure_future(test_sql1(loop)), asyncio.ensure_future(test_sql2(loop))]
        loop.run_until_complete(asyncio.gather(*furures))
        print('<'+'-'*50 +'>')
        print(SQL.instance)

    @classmethod
    def tearDownClass(cls):
        print('Stop Test')
        print('<'+'*'*50 +'>')

if __name__ == "__main__":
    # doctest.testmod(verbose=True)
    # main()
    unittest.main()