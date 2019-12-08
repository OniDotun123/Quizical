from flask import Flask

from .commands import create_tables
from .extensions import db, login_manager

def create_app(config_file='settings.py'):
  app = Flask(_name__)

  app.cofig.from_pyfile(config_file)

  db.init_app(app)
  
  login_manager.init_app(app)
  
  app.cli.add_command(create_tables)

  #login_manager.login_view=''

  #@login_manager.user.loader
  ##return User.query.get(user_id)

  

  return app