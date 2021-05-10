from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        print("Submitted login form")
        flash('Logged in')
        return redirect(url_for('auth.register'))
    return render_template('user.html', form=loginForm, heading='Login')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    return render_template('user.html',form=registerForm, heading='Register')