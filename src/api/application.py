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
        new_u = User().create(request.json)

        return jsonify(new_u), 200
    except:
        print(sys.exc_info())
        return jsonify({"message": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    app.run()
