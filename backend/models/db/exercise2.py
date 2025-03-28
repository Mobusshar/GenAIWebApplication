from . import db

class Exercise2(db.Model):
    __tablename__ = 'exercise2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    studentid = db.Column(db.String(50))
    prompt = db.Column(db.Text)
    image_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())