class Base(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:O8(zi!myBd*2@127.0.0.1:3306/lxc?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_SIZE = 1024
    SQLALCHEMY_POOL_TIMEOUT = 90
    SQLALCHEMY_POOL_RECYCLE = 3
    SQLALCHEMY_MAX_OVERFLOW = 1024

    SALT = 'IloveYou'  # 加密盐
    SECRET_KEY = 'b1bb9c4fe0d5984d26e13d4a091199b2'

    UPLOAD_FOLDER = 'static/uploads'
    #邮箱设置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = '291603599@qq.com'
    MAIL_PASSWORD = 'ijgkrosecgfwbheg'
    MAIL_DEFAULT_SENDER = '291603599@qq.com'
class Dev(Base):
    DEBUG = True


class Pro(Base):
    DEBUG = False
