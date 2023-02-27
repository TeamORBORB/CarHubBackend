from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''


class user(db.Model):
    email = db.Column(db.String(255), unique=True, nullable=False)
    uname = db.Column(db.String(255), unique=True, nullable=False)
    passowrd = db.Column(db.Integer, primary_key=True)
    def __repr__(self):
        return '<User %r>' % self.username





''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))