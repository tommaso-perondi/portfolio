import os

from flask import Flask
from flask_mail import Mail
from flask_cache import Cache
project_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, instance_relative_config=False)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

app.config.from_pyfile('config.py', silent=True)
app.config.from_pyfile('credentials.txt', silent=True)
mail = Mail(app)
mail_html = open(project_path + "/templates/mail.html", "r").read()

from core import routes
