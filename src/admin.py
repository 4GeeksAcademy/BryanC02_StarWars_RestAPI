from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Person, Planet, Favorite

def setup_admin(app):
    admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Person, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Favorite, db.session))
    