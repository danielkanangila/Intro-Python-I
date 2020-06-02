import os
import settings
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application import app, db

app.config.from_object("settings.Settings")

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", migrate)

if __name__ == 'main':
    manager.run()
