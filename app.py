from flask import Flask # type: ignore
from routes.routes import bp

app = Flask("wordle")
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()