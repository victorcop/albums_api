from flask import jsonify, Blueprint, request

from app.errors import not_found, bad_request, no_content, internal_server
from app.logger import log_error

from http import HTTPStatus

from app.repository.album_repository import AlbumRepository

album = Blueprint('album', __name__)
album_repository = AlbumRepository()


@album.route('', methods=['GET'])
def get_all():
    """
    Gets all the albums
    :return: A list with all the albums
    """
    try:
        albums = album_repository.list()
        if not albums:
            return no_content()
        return jsonify(albums)
    except Exception as e:
        log_error(e)
        return internal_server(e)


@album.route('/<album_id>', methods=['GET'])
def get(album_id):
    """
    Gets an album by uuid
    :param album_id: Album ID
    :return: an album
    """
    try:
        album_db = album_repository.get(album_id)
        if not album_db:
            return not_found()
        return jsonify(album_db)
    except Exception as e:
        log_error(e)
        return internal_server(e)


@album.route('', methods=['POST'])
def post():
    """
    Creates an album
    :return: 201 and the created album
    """
    try:
        data = request.json
        response_dict = album_repository.add(data['name'], data['description'])
        id_album = response_dict['uuid']
        return response_dict, HTTPStatus.CREATED, {'location': f'api/album/{id_album}'}
    except KeyError as e:
        log_error(e)
        return bad_request()
    except Exception as e:
        log_error(e)
        return internal_server(e)


@album.route('/<album_id>', methods=['PUT'])
def put(album_id):
    """
    Updates an album
    :return: Updated album
    """
    try:
        data = request.json
        response_dict = album_repository.update(album_id, data['name'], data['description'])
        if not response_dict:
            return no_content()
        id_album = response_dict['uuid']
        return response_dict, HTTPStatus.OK, {'location': f'api/album/{id_album}'}
    except KeyError as e:
        log_error(e)
        return bad_request()
    except Exception as e:
        log_error(e)
        return internal_server(e)


@album.route('/<album_id>', methods=['DELETE'])
def delete(album_id):
    """
    Deletes an album
    :param album_id: Album ID
    :return: 200 success=True
    """
    try:
        album_db = album_repository.get(album_id)
        if not album_db:
            return not_found()
        album_repository.delete(album_id)
        response_dict = dict(success=True)
        return response_dict
    except Exception as e:
        log_error(e)
        return internal_server(e)

