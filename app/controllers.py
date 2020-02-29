from .app import todos_list, logs
from datetime import datetime


def get_time_now():
    return datetime.utcnow()


def log_action(action_name):
    def wrap(f):
        def insider(*args, **kwargs):
            result = f(*args, **kwargs)
            if result is True:
                logs.append({
                    "time": get_time_now(),
                    "action_name": action_name
                })
            return result
        return insider
    return wrap


@log_action("insert")
def insert_todo(title, description=None, due_date=None):

    if title in todos_list.keys():
        return f"To Do {title} already exists"

    today = get_time_now()

    if due_date:
        due_date_obj = datetime.strptime(due_date, "%d/%m/%Y")

        if due_date_obj < today:
            due_date = today.strftime("%d/%m/%Y")

    todos_list[title] = {
        "description": description,
        "due_date": due_date
    }

    return True


@log_action("remove")
def remove_todo(title):
    if title not in todos_list.keys():
        return f"To Do {title} does not exist"

    del todos_list[title]

    return True
