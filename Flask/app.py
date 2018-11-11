# import sys
# sys.path.append("./")
from flask import Flask, request
from route.actor_route import actor_route
from route.film_route import film_route

import json

app = Flask(__name__)
app.register_blueprint(actor_route)
app.register_blueprint(film_route)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

