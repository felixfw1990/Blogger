from mongoengine import *

# 文章
class Articles(Document):
    id = ObjectIdField()
    title = StringField(required=True)
    desc = StringField(max_length=50)
    create = IntField()
    uid = ObjectIdField()

# 评论
class Comments(Document):
    id = ObjectIdField()
    content = StringField(required=True),
    create = IntField()
    articles_id = ObjectIdField()
    uid = ObjectIdField()

# 用户
class Users(Document):
    id = ObjectIdField()
    name = StringField(required=True)
    email = StringField(required=True, unique=True,)
    password = StringField(required=True),
    create = IntField()