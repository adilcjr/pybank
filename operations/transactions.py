""" Transactions event processor """
from models.event import Event
from models.account import Account, db


def execute(event: Event):
    """Executes the transaction processor"""

    if event.trx_type == "deposit":
        account = Account.query.get(event.destination)
        if account is not None:
            new_amount = account.balance + event.amount
            account.balance = new_amount
        else:
            # new account
            account = Account(event.destination, event.amount)
            db.session.add(account)

        db.session.commit()
        return {"destination": {"id": str(account.id), "balance": account.balance}}, 201

    if event.trx_type == "transfer":
        origin_account = Account.query.get(event.origin)
        destination_account = Account.query.get(event.destination)
        if origin_account and destination_account is not None:
            origin_account.balance -= event.amount
            destination_account.balance += event.amount
            db.session.commit()
            return {
                "origin": {
                    "id": str(origin_account.id),
                    "balance": origin_account.balance,
                },
                "destination": {
                    "id": str(destination_account.id),
                    "balance": destination_account.balance,
                },
            }, 201

    if event.trx_type == "withdraw":
        account = Account.query.get(event.origin)
        if account is not None:
            new_amount = account.balance - event.amount
            account.balance = new_amount
            db.session.commit()
            return {"origin": {"id": str(account.id), "balance": account.balance}}, 201

    return "0", 404
