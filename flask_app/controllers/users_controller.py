from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.users import User

#Importación de BCrypt es la encarga de encriptar nuestra contraseña
#RECORDATORIO debo instalar la libreria de bcrypt por lo que sera : 
# pipenv install flask pymsql flask-bcrypt y luego todo lo demas 
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')