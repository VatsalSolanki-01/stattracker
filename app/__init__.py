from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'stattrack_secret_key'

    app.config['MYSQL_HOST'] = 'mysql-db'
    app.config['MYSQL_USER'] = 'vatsal'
    app.config['MYSQL_PASSWORD'] = 'vatsal123'
    app.config['MYSQL_DB'] = 'stattracker'

    mysql.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
