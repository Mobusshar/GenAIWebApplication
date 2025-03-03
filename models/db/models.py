from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exercise1(db.Model):
    __tablename__ = 'exercise1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    studentid = db.Column(db.String(50))
    prompt = db.Column(db.Text)
    image_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())