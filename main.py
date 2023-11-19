from tumbrl import app
from tumbrl import database
from tumbrl import models


with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(debug=True)
