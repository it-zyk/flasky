from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    # Permission类加入模板上下文
    return dict(Permission=Permission)
