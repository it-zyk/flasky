
from flask_login import login_required
from .models import Permission
from decorators import admin_required, permission_required


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
