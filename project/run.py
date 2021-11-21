# run.py

from os import name
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from __init__ import db #! DONT DO THIS
from models import User, Journal
from datetime import datetime

run = Blueprint('run', __name__)

@run.route('/')
def index():
    return redirect(url_for('run.home'))

@run.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.name, u_id = current_user.id, Journal = reversed(Journal.query.all()))

@run.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email, )

@run.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['entry']:
            flash('Please enter something in each field', 'error')

        else:
            db.session.add(Journal(current_user.id, request.form['title'], datetime.today(), request.form['entry']))
            db.session.commit()
            flash('Entry successfully added to journal!')
            return redirect(url_for('run.home'))
    return render_template('new.html', name = current_user.name)

@run.route('/entries/<username>/<entry_id>', methods = ['GET', 'POST'])
@login_required

def entries(username, entry_id):
    if request.method == 'POST':
        if request.form['delete_button'] == 'Delete entry':
            Journal.query.filter_by(id = entry_id).delete()
            # db.session.delete()
            db.session.commit()
            flash('Entry deleted')
            return redirect(url_for('run.home'))
    if username == current_user.name:
        return render_template('entry.html', username = current_user.name, entry_id=int(entry_id), Journal = Journal.query.all()) 
    elif username != current_user.name:
        flash('You do not have access to this resource! If you think you should be able to access this page, please contact your local systems administrator.')
        return render_template('home.html', name=current_user.name, u_id = current_user.id, Journal = reversed(Journal.query.all()))
