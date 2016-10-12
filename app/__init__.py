from flask import Flask
import flask_mongoengine
import mongoengine
import os


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'host': os.environ.get('MONGOLAB_URI', 'mongodb://localhost/fma')}
db = flask_mongoengine.MongoEngine(app)

from admin import admin
app.register_blueprint(admin)
