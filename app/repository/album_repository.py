from sqlalchemy import select, update, delete

from app.logger import log_error, log
from app.models.album_model import Album
from app import db, cache
import uuid


class AlbumRepository:
    def __init__(self) -> None:
        self._session = db.session

    def add(self, name: str, description: str) -> dict:
        new_album = Album(str(uuid.uuid4()), name, description)
        db.session.add(new_album)
        db.session.commit()
        return dict(uuid=new_album.uuid, name=name, description=description)

    def get(self, uuid: str) -> dict:
        try:
            statement = select(Album).filter_by(uuid=uuid)
            results = self._session.execute(statement).first()
            if results:
                result = results[0]
                return dict(uuid=result.uuid, name=result.name, description=result.description)
        except Exception as e:
            log_error(e)

    @cache.cached(timeout=60, key_prefix='list_of_albums')
    def list(self) -> list:
        try:
            statement = select(Album)
            results = self._session.execute(statement).all()
            if results:
                return [dict(uuid=s[0].uuid, name=s[0].name, description=s[0].description) for s in results]
        except Exception as e:
            log_error(e)

    def update(self, uuid: str, name: str, description: str) -> dict:
        try:
            statement = update(Album).where(Album.uuid == uuid).values(description=description, name=name). \
                execution_options(synchronize_session="fetch")

            self._session.execute(statement)
            self._session.commit()
            album_db = self._session.query(Album).filter(Album.uuid == uuid).first()
            if album_db:
                return dict(uuid=album_db.uuid, name=album_db.name, description=album_db.description)
        except Exception as e:
            log_error(e)

    def delete(self, uuid: str) -> None:
        try:
            statement = delete(Album).where(Album.uuid == uuid)
            self._session.execute(statement)
            self._session.commit()
        except Exception as e:
            log_error(e)
