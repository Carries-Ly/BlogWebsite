from flask import Blueprint, jsonify, request, session
from flask_mail import Message
from flask_cors import CORS
from Flask.models import mail, db, User, Email_verify
from werkzeug.security import generate_password_hash, check_password_hash
import random

# 定义您的 Blueprint
account = Blueprint('account', __name__, url_prefix='/account')
CORS(account, cors_allowed_origins="*")

# 注册路由
@account.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    password_confirm = data.get('password_confirm')
    verify = data.get('verify')

    # 进行数据验证
    if not email or not name or not password or not password_confirm or not verify:
        return jsonify({'code': 400, 'msg': '缺少必要字段'}), 400

    if password != password_confirm:
        return jsonify({'code': 400, 'msg': '两次密码输入不一致'}), 400

    # 检查邮箱是否已被注册
    if User.query.filter_by(email=email).first():
        return jsonify({'code': 400, 'msg': '邮箱已被注册'}), 400

    # 检查验证码是否正确
    email_verify = Email_verify.query.filter_by(email=email, verify=verify).first()
    if not email_verify:
        return jsonify({'code': 400, 'msg': '验证码错误'}), 400

    # 创建新用户并保存到数据库
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, name=name, password=hashed_password, level=1, status=1)
    db.session.add(new_user)
    db.session.commit()

    # 删除已使用的验证码
    db.session.delete(email_verify)
    db.session.commit()

    return jsonify({'code': 200, 'msg': '注册成功'}), 200

@account.route('/send_verify',methods=['GET'])
def send_verify():
    email = request.args.get('email')
    verify = random.randint(1000,9999)
    message = Message(subject='欢迎来到李炫成的空间！注册验证码',recipients=[email],body="这是一个用代码发送的邮件,你的验证码是{}".format(verify))
    # print(email)
    try:
        mail.send(message)
        email_verify = Email_verify(email=email,verify=verify)
        db.session.add(email_verify)
        db.session.commit()
        return jsonify({'code':200,'msg':'成功发送'})
    except Exception as e:
        # 这里应该记录日志或者返回更具体的错误信息
        return jsonify({'code': 500, 'msg': '内部服务器错误', 'error': str(e)}), 500


@account.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    email = data.get('email')
    password = data.get('password')

    # 检查是否提供了邮箱和密码
    if not email or not password:
        return jsonify({'code': 400, 'msg': '邮箱和密码都是必填项'}), 400

    # 查询数据库中的用户
    user = User.query.filter_by(email=email).first()

    # 验证用户及其密码
    if user and check_password_hash(user.password, password):
        # 设置用户会话或执行登录成功的其他操作
        session['user_id'] = user.id
        return jsonify({'code': 200, 'msg': '登录成功'}), 200
    else:
        # 登录失败的处理
        return jsonify({'code': 400, 'msg': '无效的邮箱或密码'}), 400

