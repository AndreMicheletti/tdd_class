from flask import Flask
from flask_restful import Api


todos_list = {}

logs = []


def create_flask_app():
    from app.resources import ToDoAPI, LogsAPI

    flask_app = Flask(__name__)

    @flask_app.route("/hello")
    def hello_world():
        return "hello world"

    api = Api(flask_app)

    api.add_resource(ToDoAPI, '/todo')
    api.add_resource(LogsAPI, '/logs')

    return flask_app
