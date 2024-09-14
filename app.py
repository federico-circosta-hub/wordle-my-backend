from flask import Flask # type: ignore
from routes.routes import bp

app = Flask("wordle")
app.register_blueprint(bp)

if __name__ == "wordle_routes":
    app.run()