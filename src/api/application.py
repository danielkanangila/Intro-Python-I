import sys
from flask import Flask, jsonify, request
from models import *

app = Flask(__name__)
app.config.from_object("settings.Settings")

db.init_app(app)


@app.route("/")
def index():
    return jsonify({
        "message": "Hello World!"
    })


@app.route("/register", methods=["POST"])
def register():
    try:
        u = User()
        u.create(request.json)
        return jsonify({"message": "ok"}), 200
    except:
        print(sys.exc_info())
        return jsonify({"message": "An unexpected error occurred"}), 500


def main():
    # Create tables based on table definition in `models`
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
