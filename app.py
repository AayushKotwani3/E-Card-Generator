from flask import Flask
from Application.database import db
app=None

def create_app():
    app=Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ecard.sqlite" #step 3 Database
    db.init_app(app) #step 3 Database
    app.app_context.push()
    return app

app=create_app()
from Application.controllers import * #step2 controllers

if __name__ == "__main__":
    app.run
