"""Server for forever app."""

from flask import Flask

app = Flask(__name__)

#comming soon, functions and routes!


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)