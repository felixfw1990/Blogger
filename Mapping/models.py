from mongoengine import *

# 文章
class Articles(Document):
    id = ObjectId
    title = StringField(required=True)
    desc = StringField(max_length=50)
    create = int
    uid = ObjectId

# 评论
class Comments(Document):
    id = ObjectId
    content = StringField(required=True),
    create = int
    articles_id = ObjectId
    uid = ObjectId

# 用户
class Users(Document):
    id = ObjectId
    name = StringField(required=True)
    email = StringField(required=True, unique=True,)
    password = StringField(required=True),
    create = int