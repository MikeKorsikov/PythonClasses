# creating decorated function
from flask import session
from functools import wraps


def check_logged_in(func):
    # decorating function with decorator
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            # invoking decorated function
            return func(*args, **kwargs)
        return 'You are NOT logged in.'

    return wrapper
