# app/models.py

from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Clothe(UserMixin, db.Model):
    """
    Create a Clothe table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'clothes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    kind = db.Column(db.String(60), index=True)
    temp = db.Column(db.String(60), index=True)
    color = db.Column(db.String(60), index=True)
    # password_hash = db.Column(db.String(128))
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # is_admin = db.Column(db.Boolean, default=False)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Clothe.query.get(int(user_id))

class Outfit(db.Model):
    """
    Create an Outfit table
    """

    __tablename__ = 'outfits'

    id = db.Column(db.Integer, primary_key=True)
    top = db.relationship('Clothe', backref='kind',
                                lazy='dynamic')
    bottom = db.relationship('Clothe', backref='kind',
                                lazy='dynamic')
    shoe = db.relationship('Clothe', backref='kind',
				lazy='dynamic')
    accessories = db.relationship('Accessory', backref='kind',
				lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
