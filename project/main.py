# main.py

from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from __init__ import journal, jrnl_db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# Login stuff above this line, journal stuff below this line

@main.route('/home')
@login_required
def homepage():
    return render_template('show_all.html', name=current_user.name, journal = journal.query.all() ) # show_all doesn't use name yet but I'll add it. Also need to figure out how to only access the data from the individual user

@main.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['time'] or not request.form['entry']:
            flash('Please enter something in each field', 'error')
        else:
            jrnl_entry = journal(request.form['title'], request.form['time'], request.form['entry'])

            # Does this import actually work?
            jrnl_db.session.add(jrnl_entry)
            jrnl_db.session.commit()
            flash('Entry added to journal')
            return redirect(url_for('show_all'))
    return render_template('new.html')


# !! I haven't made this DB yet.
# if __name__ == '__main__':
#     jrnl_db.create_all()
