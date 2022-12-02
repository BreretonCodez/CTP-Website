from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_login import login_required, login_user, LoginManager
from App.models import User

index_views = Blueprint('index_views', __name__, template_folder='../templates')

login_manager = LoginManager()

@index_views.route('/', methods=['GET','POST'])
def index_page():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email = data['email']).first()
        if user and user.check_password(data['password']): # check credentials
            flash('Logged in successfully.') # send message to next page
            login_user(user) # login the user
            return redirect('/dashboard') # redirect to main page if login successful
        else:
            flash('Invalid username or password') # send message to next page
            return render_template('index.html')
    return render_template('index.html')


@index_views.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('/auth/index.html')