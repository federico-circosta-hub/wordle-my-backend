from flask import Flask
from routes.routes import bp
from flask_cors import CORS

app = Flask("wordle")
app.register_blueprint(bp)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

if __name__ == "__main__":
    app.run()