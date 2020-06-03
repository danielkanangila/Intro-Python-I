import sys
import requests as fetch
from flask import Flask, jsonify, request
from flask_bcrypt import check_password_hash
from models import *
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
app.config.from_object("settings.Settings")

# Database initialization
db.init_app(app)


# JWTManager initialization
jwt = JWTManager(app)


@app.route("/")
def index():
    return jsonify({
        "message": "Hello World!"
    })


@app.route("/register", methods=["POST"])
def register():
    try:
        new_u = User().create(request.json)

        return jsonify(new_u), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "An unexpected error occurred"}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if (not email) | (not password):
            return jsonify({"message": "'email' and 'password' are required"}), 400

        user = User.query.filter(User.email == email).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.email)
            return jsonify({"access_token": access_token})
        else:
            return jsonify({"message": "Invalid email or password."}), 403

    except Exception as e:
        print(e)
        return jsonify({"message": "An unexpected error occurred"}), 500


@app.route("/jokes/<int:page>")
@jwt_required
def index_posts(page):
    jokes = fetch.get(f"https://icanhazdadjoke.com/search?term=&page={page}",
                      headers={"accept": "application/json"})

    return jokes.json()


if __name__ == "__main__":
    app.run()
