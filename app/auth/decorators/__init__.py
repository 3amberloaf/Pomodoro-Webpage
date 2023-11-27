from functools import wraps
from flask_login import current_user
from flask import render_template

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_admin != 1:
            return render_template('403.html'), 403
        return f(*args, **kwargs)
    return decorated_function