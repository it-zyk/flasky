from flask import Flask, render_template, Blueprint
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

from flask_login import LoginManager, login_required

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# 录路由在蓝本中定义，因此要在前面加上蓝本的名字。
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # 蓝本在工厂函数create_app()中注册到程序上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    # app.register_blueprint(auth_blueprint)

    '''
    注册蓝本时使用的url_prefix是可选参数。
    如果使用了这个参数，注册后蓝本中定义的所有路由都会加上指定的前缀，
    即这个例子中的/auth。
    例如，/login路由会注册成/auth/login，
    在开发Web服务器中，
    完整的URL就变成了http://localhost:5000/auth/login。
    '''
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # 附加路由和自定义的错误页面

    return app
