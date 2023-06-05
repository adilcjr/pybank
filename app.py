""" Application start """
import os
from flask_migrate import Migrate

from api.init import create_app
from models.account import db

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG", True))
