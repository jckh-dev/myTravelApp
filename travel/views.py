from flask import Blueprint, render_template, request, session, redirect, url_for

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def home():
    return render_template('index.html')
    # if 'email' in session and session['email'] is not None:
    #     # print(session['email'])
    #     message = "<h1>Hello " + session['email'] + "</h1>"
    # else:
    #     message = '<h1>HELLO</h1>'
    # return message



@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
    return 'Session has been cleared'