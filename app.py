from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Cruel World"

# This file creates a new instance of the Flask application and defines a single route that
# returns the “Hello World!” statement. This is the most basic Flask application,
# but it will show that everything has been configured properly.
