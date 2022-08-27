from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'not that important'
    #encrypts the cookies of web app

    return app
    