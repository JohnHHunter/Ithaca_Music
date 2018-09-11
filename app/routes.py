from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    artists = [
        {
            'band': {'bandname': 'Band1'},
            'hometown': {'Ithaca'},
            'info': 'Beautiful day in Portland!',
            'events': 'asd'
        },
        {
            'band': {'bandname': 'Band2'},
            'hometown': {'Ithaca'},
            'info': 'Info!',
            'events': 'asdf'
        }
    ]
    return render_template('index.html', title='Home', artists=artists)

@app.route('/artists')
def artists():
    artists = ["asdf", "asdfasdf", "asdfasdfasfd"]
    return render_template('artists.html', title='Artists', artists=artists)

@app.route('/newartist')
def newartist():
    return render_template('newartist.html', title="New Artists")

@app.route('/artistpage')
def artistpage():
    return render_template('artistpage.html', title="Artist Page")