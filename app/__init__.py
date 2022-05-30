from flask import Flask

from config import Config

app = Flask(__name__)

app.config.from_object(Config)


from .auth.routes import auth

app.register_blueprint(auth)

from .models import db, login
from flask_migrate import Migrate

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page'
login.login_message_category = 'danger'

from .import routes