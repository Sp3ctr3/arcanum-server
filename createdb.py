from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password =db.Column(db.String(120), unique=False)
    key = db.Column(db.String(200),unique=True)
    uuid = db.Column(db.String(200),unique=True)

    def __init__(self, username, email, passw, key,uuid):
        self.username = username
        self.email = email
        self.password = passw
        self.key = key
        self.uuid = uuid

    def __repr__(self):
        return '<User %r>' % self.username
if __name__ == '__main__':
    db.create_all()
    user=User("admin","adminemail","adminpass","123456789","test")
    db.session.add(user)
    db.session.commit()
