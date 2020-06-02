from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, index=True, unique=True, nullable=False)
    password = db.Column(db.String, index=False, nullable=False)

    def create(self, user):
        user["password"] = generate_password_hash(
            user["password"]
        ).decode("utf8")

        new_user = User(**user)
        db.session.add(new_user)
        db.session.commit()

        del user['password']

        return user
