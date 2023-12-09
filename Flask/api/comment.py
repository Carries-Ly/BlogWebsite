from flask import Blueprint

login = Blueprint('login',__name__,url_prefix='login')

@login.route('/register',methods=['POST'])
def register():
    pass