# web/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)       # SQLAlchemyを利用する場合
migrate = Migrate(app, db) # Flask-Migrateを利用する場合

from web import views
