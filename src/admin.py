from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Person, Planet, Favorite

class FavoriteView(ModelView):
    column_list = ["id", "user_id", "planet_id", "person_id"]
    column_labels = {
        "user_id": "User",
        "planet_id": "Planet",
        "person_id": "Person"
    }

def setup_admin(app):
    admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Person, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(FavoriteView(Favorite, db.session))
    