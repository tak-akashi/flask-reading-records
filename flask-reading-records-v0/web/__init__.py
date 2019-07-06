# web/__init__.py
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)

# db = SQLAlchemy(app)       # SQLAlchemyを利用する場合
# migrate = Migrate(app, db) # Flask-Migrateを利用する場合

from web import views
