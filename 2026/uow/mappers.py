from typing import Protocol

from uow.models import User


class DataMapper[T](Protocol):
    def insert(self, model: T) -> None: ...

    def update(self, model: T) -> None: ...

    def delete(self, model: T) -> None: ...


class UserMapper(DataMapper[User]):
    def insert(self, model: User) -> None:
        print(f"Insert model {model}")

    def update(self, model: User) -> None:
        print(f"Update model {model}")

    def delete(self, model: User) -> None:
        print(f"Delete model {model}")
