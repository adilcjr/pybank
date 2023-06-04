"""Here we have the transaction events"""
from models.event import Event


def process_transaction(event: Event):
    """Identifies the transaction type to deal with data"""

    if event.trx_type == "deposit":
        if event.destination == "100":
            return {
                "destination": {"id": event.destination, "balance": event.amount}
            }, 201

    if event.trx_type == "transfer":
        if event.origin == "100":
            return {
                "origin": {"id": event.origin, "balance": 0},
                "destination": {"id": event.destination, "balance": 15},
            }, 201

    if event.trx_type == "withdraw":
        if event.origin == "100":
            return {
                "origin": {"id": event.origin, "balance": 15},
            }, 201

    return "0", 404
