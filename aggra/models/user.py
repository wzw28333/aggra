from .mixin import Mixin


class User(Mixin, table=True):
    __tablename__ = 'users'
    name: str
    email: str
    password_hash: str
    