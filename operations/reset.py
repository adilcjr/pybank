""" Reset database operation """
from models.account import Account

from models.account import db


def execute():
    """Executes the database reset"""
    # Clean database
    accounts = Account.query.all()
    for account in accounts:
        db.session.delete(account)
    db.session.commit()

    # Create the account 300
    account = Account(300, 0)
    db.session.add(account)
    db.session.commit()

    return "OK", 200
