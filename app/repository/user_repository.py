from sqlalchemy import select

from app import db
from app.logger import log_error
from app.models.user import User


class UserRepository:
    def __init__(self) -> None:
        self._session = db.session

    def add(self, username: str, email: str,  password: str) -> dict:
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
        return dict(uuid=new_user.uuid, username=new_user.username, password=new_user.email)

    def get(self, username) -> User:
        try:
            statement = select(User).filter_by(username=username)
            user = self._session.execute(statement).first()
            if user[0]:
                return user[0]
        except Exception as e:
            log_error(e)
