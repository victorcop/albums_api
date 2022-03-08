import sys

from flask import current_app


def log(message='', e=None):
    current_app.logger.info({'Message': message, 'Error': e})


def log_error(e):
    current_app.logger.error({'success': False, 'Message': 'An error occurred', 'Exception': sys.exc_info()})
