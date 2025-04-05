from flask import Flask
from Application.database import db
app=None

def create_app():
    # global app
    app=Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ecard.sqlite" #step 3 Database
    db.init_app(app) #step 3 Database
    with app.app_context():
        import Application.controllers
    # with app.app_context():
    #     pass
    return app

app=create_app()
# with app.app_context():
    #from Application.controllers import * #step2 controllers
# from Application.models import * # making connection with models module using controllers so no need for this

if __name__ == "__main__":
    app.run()
