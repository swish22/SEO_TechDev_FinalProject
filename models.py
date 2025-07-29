from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

if __name__ == '__main__':
    db.create_all()