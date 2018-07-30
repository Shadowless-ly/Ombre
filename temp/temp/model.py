import time
import uuid
from orm import Model, StringField, BooleanField, IntegerField, FloatField, TextField
import asyncio
import logging;logging.basicConfig(level=logging.DEBUG)

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    """用户列表
    """
    __table__ = 'users'
    # id
    id = StringField(name='id', default=next_id, primary_key=True, ddl='varchar(50)')
    # 名称
    name = StringField(name='name', ddl='varchar(50)')
    # 密码
    password = StringField(name='password', ddl='varchar(50)')
    # 权限id
    role_id = IntegerField(name='role_id')
    # 邮箱
    mail = StringField(name='mail', ddl='varchar(50)')
    # 创建时间
    created_at = FloatField(name='created_at', default=time.time)


class Post(Model):
    """文章列表
    """
    __table__ = 'post'
    # id
    id = StringField(name='id', default=next_id, primary_key=True, ddl='varchar(50)')
    # 板块id
    plate = IntegerField(name='plate')
    # 内容
    content = TextField(name='content')
    # 作者id
    user_id = StringField(name='user_id', ddl='varchar(50)')
    # 作者名称
    user_name = StringField(name='user_name', ddl='varchar(50)')
    # 图片
    user_image = StringField(name='user_image', ddl='varchar(500)')
    # 文章名称
    name = StringField(name='name', ddl='varchar(50)')
    # 创建时间
    created_at = FloatField(name='created_at', default=time.time)

class Comment(Model):
    """评论列表
    """
    __table__ = 'comments'
    # id
    id = StringField(name='id', primary_key=True, default=next_id, ddl='varchar(50)')
    # 关联的文章id
    post_id = StringField(name='post_id', ddl='varchar(50)')
    # 用户id
    user_id = StringField(name='user_id', ddl='varchar(50)')
    # 用户名称
    user_name = StringField(name='user_name', ddl='varchar(50)')
    # 用户图片
    user_image = StringField(name='user_image', ddl='varchar(500)')
    # 评论内容
    content = TextField(name='content')
    # 发表时间
    created_at = FloatField(name='created_at', default=time.time)

class Role(Model):
    """权限列表
    """
    __table__ = 'role'
    # id
    id = IntegerField(name='id', primary_key=True)
    # 名称
    name = StringField(name='name', ddl='varchar(50)')
    # 是否启用
    enable = BooleanField(name='enable')

class Plate(Model):
    """板块列表
    """
    __table__ = 'plate'
    # id
    id = IntegerField(name='id', primary_key=True)
    # 名称
    name = StringField(name='name', ddl='varchar(50)')
    # 对应管理权限id
    manager_role_id = IntegerField(name='manager_role_id')


async def main(loop):
    # user = User(name='shadowless', password='111111', role_id=9, mail='ly9413ly@163.com')
    # await user.save()
    # role = Role(id=9, name='administrator', enable=True)
    # plate = Plate(id=0, name='home', manager_role_id=9)
    # post = Post(plate=0, content='for test', user_id='001532965256048fd4a23504b3d4ea893eb48061415e4a9000', user_name='shadowless', user_image="test", name='post for test')
    # comment = Comment(post_id='00153296598189365877bb0508240ba861b0e25fc68deb4000', user_id='001532965256048fd4a23504b3d4ea893eb48061415e4a9000', user_name='shadowless', user_image='test', content='comment for test')
    # await role.save()
    # await plate.save()
    # await post.save()
    # await comment.save()
    print(await User.findall())
    print(await Role.findall())
    print(await Plate.findall())
    print(await Post.findall())
    print(await Comment.findall())
    
    await User.__sql__.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))