"""Account model"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    balance = db.Column(db.Numeric(10, 2), nullable=False, default=False)

    def __repr__(self):
        return f"<account {self.id}, {self.balance}>"
