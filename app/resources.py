from flask_restful import Resource, reqparse
import json

from .app import todos_list, logs
from .controllers import insert_todo, remove_todo


class ToDoAPI(Resource):

    def get(self):
        return todos_list

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("title", location="json", required=True)
        parser.add_argument("description", location="json", required=False, default="")
        parser.add_argument("due_date", location="json", required=False, default=None)

        args = parser.parse_args()
        title = args["title"]
        description = args["description"]
        due_date = args["due_date"]

        result = insert_todo(title, description, due_date)

        if result is True:
            return "inserted", 200
        else:
            return result, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", location="json", required=True)

        args = parser.parse_args()
        title = args["title"]

        result = remove_todo(title)

        if result is True:
            return "deleted", 200
        else:
            return result, 500


class LogsAPI(Resource):

    def get(self):
        return {
            "logs": logs
        }
