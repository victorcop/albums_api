from http import HTTPStatus

from app.logger import log


def not_found():
    log('Not Found!')
    return {'success': False, 'Message': 'Not Found!'}, HTTPStatus.NOT_FOUND, {'ContentType': 'application/json'}


def bad_request():
    log('Bad request!')
    return {'success': False, 'Message': 'Bad request!'}, HTTPStatus.BAD_REQUEST, {'ContentType': 'application/json'}


def not_allowed(e):
    log('The method is not allowed for the requested URL.', e)
    return {'success': False, 'Message': 'The method is not allowed for the requested URL.'}, \
           HTTPStatus.METHOD_NOT_ALLOWED, {'ContentType': 'application/json'}


def no_content():
    log('No Content!')
    return {'success': False, 'Message': 'No Content!'}, HTTPStatus.NO_CONTENT, {'ContentType': 'application/json'}


def internal_server(e):
    log('Internal Error.', e)
    return {'success': False, 'Message': 'Internal Error.'}, \
           HTTPStatus.INTERNAL_SERVER_ERROR, {'ContentType': 'application/json'}
