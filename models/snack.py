from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    diet = db.Column(db.Boolean, default=False, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "diet": self.diet,
            "date": self.date
        }
