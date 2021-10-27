# main.py

from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

#==============================================

# I don't know if this should go here or in __init__. However, I do know that I will have to rename my db.
# I will probably also have to make a new db using the definition that I used in the original

class journal(db.Model):
    id = jrnl_db.Column('entry_id', jrnl_db.Integer, primary_key = True)
    time = jrnl_db.Column(jrnl_db.String(50))
    title = jrnl_db.Column(jrnl_db.String(100))
    entry = jrnl_db.Column(jrnl_db.String(200))

    def __init__(self, time, title, entry):
        self.time = time
        self.title = title
        self.entry = entry
# =============================================

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# Login stuff above this line, journal stuff below this line

# @main.route('/home')
# @login_required
# def homepage():
#     return render_template('show_all.html', name=current_user.name, journal = journal.query.all() ) # show_all doesn't use name yet but I'll add it. Also need to figure out how to only access the data from the individual user

# @main.route('/new', methods = ['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['title'] or not request.form['time'] or not request.form['entry']:
#             flash('Please enter something in each field', 'error')
#         else:
#             jrnl_entry = journal(request.form['title'], request.form['time'], request.form['entry'])

#             db.session.add(jrnl_entry)
#             db.session.commit()
#             flash('Entry added to journal')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')