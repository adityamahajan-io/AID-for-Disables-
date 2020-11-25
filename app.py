from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import pymongo

app = Flask(__name__)

testUser = {
    'name': "Virginia D Anderson",
    'sex': 'Female',
    'image': 'https://www.fairlandsdental.co.uk/wp-content/uploads/2014/03/person-placeholder-1.jpg',
    'birthday': '10/5/1967',
    'uid': 313644154,
    'height': "5' 8",
    'weight': '167.5',
    'blood_type': 'A+',
    'phone': 317-607-6054,
    'address': '775  Sharon Lane, Mishawaka, IN, Indiana'
}


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('dashboard.html', user=testUser)


@app.route('/patient-info')
def patientInfo():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('patient-info.html', user=testUser)


@app.route('/login', methods=['POST'])
def do_admin_login():
    # do mongo
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
