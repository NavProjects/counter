from typing import Counter
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'Safe Information'


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")


@app.route('/add')
def add_two():
    session['count'] += 1
    return redirect('/')


@app.route('/own', methods=['POST'])
def add():
    add = int(request.form['increment'])
    session['count'] = session['count']-1+add
    return redirect('/')



@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)