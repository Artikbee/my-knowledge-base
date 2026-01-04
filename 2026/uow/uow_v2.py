from dataclasses import dataclass
from typing import Any, Protocol, Self


class DataMapper[T](Protocol):
    def insert(self, model: T) -> None: ...

    def update(self, model: T) -> None: ...

    def delete(self, model: T) -> None: ...


class UoW[T]:
    def __init__(self, mapper: DataMapper[T]) -> None:
        self._new = {}
        self._dirty = {}
        self._delete = {}
        self._mapper = mapper

    def register_new(self, model: T) -> None:
        model_id = id(model)
        self._new[model_id] = model

    def register_dirty(self, model: T) -> None:
        model_id = id(model)
        if model_id not in self._dirty:
            self._dirty[model_id] = model

    def register_delete(self, model: T):
        model_id = id(model)
        if model_id not in self._delete:
            self._delete[model_id] = model

    def commit(self):
        for model in self._new.values():
            self._mapper.insert(model)
        for model in self._dirty.values():
            self._mapper.update(model)
        for model in self._delete.values():
            self._mapper.delete(model)

        self._new.clear()
        self._dirty.clear()
        self._delete.clear()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def rollback(self):
        self._new.clear()
        self._dirty.clear()
        self._delete.clear()


@dataclass
class User:
    name: str


class UserMapper(DataMapper[User]):
    def insert(self, model: User) -> None:
        print(f"Insert model {model}")

    def update(self, model: User) -> None:
        print(f"Update model {model}")

    def delete(self, model: User) -> None:
        print(f"Delete model {model}")


def main():
    user_mapper = UserMapper()
    uow = UoW[Any](mapper=user_mapper)
    with uow:
        new_user = User(name="Peter")
        uow.register_new(new_user)


if __name__ == "__main__":
    main()
