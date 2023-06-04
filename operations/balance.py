"""Here we have balance operation"""


def get_balance(account_id: int):
    """Get the account balance for an account_id"""

    if account_id == 100:
        return "20", 200
    return "0", 404
