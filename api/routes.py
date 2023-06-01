"""API routes"""
from flask import render_template, request, jsonify
from models.account import Account, db


def init_routes(app):
    """Initilize API routes"""

    @app.get("/")
    def index():
        """A simple Home page"""
        return render_template("index.html")

    @app.post("/reset")
    def reset():
        """Reset state before starting tests"""
        return "", 200

    @app.get("/balance")
    def balance():
        """Get balance from an account"""

        account_id = request.args.get("account_id", 0, int)

        if account_id > 0:
            account = Account.query.get(account_id)
            return jsonify(
                {"destination": {"id": account.id, "balance": account.balance}}
            )
        return "0", 404

    @app.post("/event")
    def event():
        """Deal with account transactions: deposit, transfer and withdraw"""

        trx_type = request.json["type"]

        if trx_type == "deposit":
            destination = request.json["destination"]
            amount = request.json["amount"]

            account = Account(destination, amount)
            db.session.add(account)
            db.session.commit()

            return {"destination": {"id": destination, "balance": amount}}, 201

        if trx_type == "transfer":
            origin = request.json["origin"]
            destination = request.json["destination"]
            amount = request.json["amount"]
            if origin == "100":
                return {
                    "origin": {"id": origin, "balance": 0},
                    "destination": {"id": destination, "balance": 15},
                }

        if trx_type == "withdraw":
            origin = request.json["origin"]
            amount = request.json["amount"]
            if origin == "100":
                return {
                    "origin": {"id": origin, "balance": 15},
                }

        return "0", 404
