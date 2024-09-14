from flask import Flask
from routes.routes import bp
from flask_cors import CORS

app = Flask("wordle")
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()