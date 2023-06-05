"""Here we have balance operation"""
from flask import jsonify
from models.account import Account


def get_balance(account_id: int):
    """Get the account balance for an account_id"""

    account = Account.query.get(account_id)
    if account is not None:
        return jsonify(account.balance), 200
    return "0", 404
