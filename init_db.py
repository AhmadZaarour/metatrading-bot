from modules import create_app, db
from modules.tables import *

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database initialized successfully!")
