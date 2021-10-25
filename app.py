from flask import Flask
from flask.templating import render_template
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class journal(db.Model):
    id = db.Column('entry_id', db.Integer, primary_key = True)
    time = db.Column(db.String(50))
    title = db.Column(db.String(100))
    entry = db.Column(db.String(200))

    def __init__(self, time, title, entry):
        self.time = time
        self.title = title
        self.entry = entry

@app.route('/')
def show_all():
    return render_template('show_all.html', journal = journal.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['time'] or not request.form['entry']:
            flash('Please enter something in each field', 'error')
        else:
            jrnl_entry = journal(request.form['title'], request.form['time'], request.form['entry'])

            db.session.add(jrnl_entry)
            db.session.commit()
            flash('Entry added to journal')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)