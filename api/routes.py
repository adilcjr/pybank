"""API routes"""
from flask import render_template, request
from operations.balance import get_balance
from operations.transactions import process_transaction
from models.event import Event


def init_routes(app):
    """Initilize API routes"""

    @app.get("/")
    def index():
        """A simple Home page"""
        return render_template("index.html")

    @app.post("/reset")
    def reset():
        """Reset state before starting tests"""
        return "OK", 200

    @app.get("/balance")
    def balance():
        """Get balance from an account"""
        account_id = request.args.get("account_id", 0, int)

        return get_balance(account_id)

    @app.post("/event")
    def event():
        """Deal with account transactions: deposit, transfer and withdraw"""

        event = Event()
        event.trx_type = request.json["type"]
        if "origin" in request.json:
            event.origin = request.json["origin"]
        if "destination" in request.json:
            event.destination = request.json["destination"]
        event.amount = request.json["amount"]

        return process_transaction(event)
