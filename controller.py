from flask import Flask, render_template, request, redirect, session
from models import User
from services import UserService

app = Flask(__name__)

@app.route('/')
def index():
    if 'email' in session:
        return redirect('/home')
    else:
        return redirect('/login')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        if UserService.authenticate(email, password):
            session['email'] = email
            return redirect('/home')
        else:
            return render_template('login.html', error='Mot de passe invalide')
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        email = request.form['email']
        password = request.form['password']
        if UserService.addUser(email, password):
            return redirect('/login')
        else:
            return render_template('register.html', error='Email already exists')
        
if __name__ == '__main__':
    app.run(debug=True)