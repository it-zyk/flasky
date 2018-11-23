from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

'''
    检查用户权限的自定义修饰器
    如果用户不具有指定权限，则返回403错误码，即HTTP“禁止”错误
'''

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
