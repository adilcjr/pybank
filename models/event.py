""" Event model """


class Event:
    """This is the event class"""

    trx_type: str = ""
    origin: str = ""
    destination: str = ""
    amount: int = 0

    def __str__(self):
        return (
            f"Event: ({self.trx_type}, {self.origin}, {self.destination}, {self.amount}"
        )
