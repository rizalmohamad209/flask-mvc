
from flask import Flask  # import Flask
from flask_assets import Bundle, Environment


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:Rizalmohamad123@localhost/flask_crud'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *
assets = Environment(app)
css = Bundle('src/main.css', output='dist/main.css', filters='postcss')
assets.register('main_css', css)
css.build()
