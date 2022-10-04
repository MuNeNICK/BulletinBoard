from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user


app = Flask(__name__)

app.config.from_object('config')

import views

if __name__ == '__main__':
    app.run(host='localhost')
