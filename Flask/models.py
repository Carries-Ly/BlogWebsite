from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
db = SQLAlchemy()
mail = Mail()

class User(db.Model):
    """用户表
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    # 0: 游客; 1：本人;
    level = db.Column(db.Integer)
    # 0: 被禁用；1： 正常
    status = db.Column(db.Integer)

    def __init__(self, name, email,password, level, status):
        self.name = name
        self.email = email
        self.password = password
        self.level = level
        self.status = status

    def __repr__(self):
        return '<id %r>' % self.id

class Article(db.Model):
    """
        文章
    """
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)#文章id 主键
    title = db.Column(db.Text, nullable=False)  # 文章标题
    content = db.Column(db.Text, nullable=False)# 文章内容
    create_time = db.Column(db.DateTime, default=datetime.now)#创建时间
    update_time = db.Column(db.DateTime, nullable=False)#更新时间
    cover = db.Column(db.Text, nullable = True)#文章封面
    def __init__(self, title, cover, content, create_time, update_time):
        self.title = title
        self.cover = cover
        self.content = content
        self.create_time = create_time
        self.update_time = update_time

    def __repr__(self):
        return '<Article id %r>' % self.id

class Comments(db.Model):
    """
    评论信息
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(255), nullable=False)    #   评论信息
    user_id = db.Column(db.Integer, nullable=False)  # 评论人员
    create_time = db.Column(db.DateTime, default=datetime.now)  # 建立时间
    def __init__(self, post_id, content, user_id, create_time):
        self.post_id = post_id
        self.content = content
        self.user_id = user_id
        self.create_time = create_time

    def __repr__(self):
        return '<Comments id %r>' % self.id

class Email_verify(db.Model):
    '''
    验证码信息
    '''
    __tablename__ = 'email_verify'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    verify = db.Column(db.Integer, nullable=False)
    def __init__(self, email, verify):
        self.email = email
        self.verify = verify
    def __repr__(self):
        return '<Email_verify id %r>' % self.id