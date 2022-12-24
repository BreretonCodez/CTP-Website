from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_login import login_required, current_user
from App.models import User
import sys

from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET','POST'])
def index_page():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        passw = data['password']

        if not email or not passw:
            flash('Please enter both an email and password')
            return redirect('/')

        user = authenticate(email, passw)

        if user:
            flash('Logged in successfully.')
            log_in_user(user, True)
            return redirect('/dashboard')
        else:
            flash('Invalid username or password') # send message to next page
            return render_template('index.html')
    return render_template('index.html')


@index_views.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = get_user_by_id(current_user.id)
    prods = get_all_prods()
    return render_template('/auth/index.html', user=user, prods=prods)