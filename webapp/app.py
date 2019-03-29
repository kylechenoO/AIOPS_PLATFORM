import os
from flask import Flask, render_template
from views.forms import LoginForm
from flask_wtf.csrf import CSRFProtect
from models.User import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user

app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app = app)

@login_manager.user_loader
def load_user(user_id):
    return(User.get(user_id))

csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User(user_name)
        app.logger.debug('set passwd')
        user.password(user_name)
        if user.verify_password(password):
            login_user(user, remember=remember_me)
            return(redirect(request.args.get('next') or url_for('main')))
    return(render_template('login.html', title="Sign In", form=form))

@app.route('/')
@app.route('/main')
@login_required
def main():
    return(render_template('main.html', username=current_user.username))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return(redirect(url_for('login')))

app.run(
    host = '0.0.0.0',
    port = 80,
    debug = True
)
