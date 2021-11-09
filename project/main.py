# main.py

from os import name
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from . import db
from .models import User, Journal
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.home'))

@main.route('/home')
@login_required
def home():
    # The way the next line is rendered is probably a security issue. I should use a specific query instead of this one. 
    return render_template('home.html', name=current_user.name, u_id = current_user.id, Journal = reversed(Journal.query.all()))

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email, )

@main.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['entry']:
            flash('Please enter something in each field', 'error')

        else:
            db.session.add(Journal(current_user.id, request.form['title'], datetime.today(), request.form['entry']))
            db.session.commit()
            flash('Entry added to journal')
            return redirect(url_for('main.home'))
    return render_template('new.html', name = current_user.name)

@main.route('/entries/<username>/<entry_id>', methods = ['GET', 'POST'])
@login_required
def entries(username, entry_id):
    if request.method == 'POST':
        if request.form['delete_button'] == 'delete_entry':
            db.session.execute('delete from journal where entry_id = %d',entry_id) # this line won't work
            db.session.commit()
            flash('Entry deleted')
    return render_template('entry.html', username = current_user.name, entry_id=int(entry_id), Journal = Journal.query.all()) # Entry_id should probably be something else, but I don't know what it should be 