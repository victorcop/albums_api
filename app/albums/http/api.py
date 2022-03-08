from flask import jsonify, Blueprint, request

from app import db, cache
from app.errors import not_found, bad_request, no_content
from app.logger import log_error
from app.models.album_model import Album

from http import HTTPStatus

album = Blueprint('album', __name__)


@cache.cached(timeout=60, key_prefix='list_of_albums')
def get_albums():
    return Album.query.all()


@album.route('', methods=['GET'])
def get_all():
    """
    Gets all the albums
    :return: A list with all the albums
    """
    albums_db = get_albums()
    if not albums_db:
        return no_content()
    return jsonify([s.serialize() for s in albums_db])


@album.route('/<album_id>', methods=['GET'])
def get(album_id):
    """
    Gets an album by id
    :param album_id: Album ID
    :return: an album
    """
    album_db = Album.query.get(album_id)
    if not album_db:
        return not_found()
    return jsonify(album_db.serialize())


@album.route('', methods=['POST'])
def post():
    """
    Creates an album
    :return: 201 and the created album
    """
    try:
        data = request.json
        name = data['name']
        description = data['description']
        new_album = Album(name, description)
        db.session.add(new_album)
        db.session.commit()
        response_dict = dict(id=new_album.id, name=name, description=description)
        return response_dict, HTTPStatus.CREATED
    except KeyError as e:
        log_error(e)
        return bad_request()


@album.route('', methods=['PUT'])
def put():
    """
    Updates an album
    :return: Updated album
    """
    try:
        data = request.json
        name = data['name']
        album_db = Album.query.filter_by(name=name).first()
        if not album_db:
            return no_content()
        album_db.description = data['description']
        db.session.add(album_db)
        db.session.commit()
        response_dict = dict(id=album_db.id, name=album_db.name, description=album_db.description)
        return response_dict
    except KeyError as e:
        log_error(e)
        return bad_request()


@album.route('/<album_id>', methods=['DELETE'])
def delete(album_id):
    """
    Deletes an album
    :param album_id: Album ID
    :return: 200 success=True
    """
    album_db = Album.query.get(album_id)
    if not album_db:
        return not_found()
    db.session.delete(album_db)
    db.session.commit()
    response_dict = dict(success=True)
    return response_dict
