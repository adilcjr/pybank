"""Account model"""
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    """Account model"""

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Numeric(10, 2), nullable=False, default=False)

    def __init__(self, id, balance):
        """Account constructor"""

        self.id = id
        self.balance = balance

    def to_json(self):
        """Convert to JSON format representation"""

        return jsonify({"id": self.id, "balance": self.balance})

    def __repr__(self):
        return f"<account: {self.id}, {self.balance}>"
