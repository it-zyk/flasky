
from flask_login import login_required


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
