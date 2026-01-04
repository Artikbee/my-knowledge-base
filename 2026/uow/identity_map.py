from typing import Any


class IdentityMap:
    def __init__(self) -> None:
        self._entities = {}

    def get(self, cls: type, identity: Any) -> Any:
        return self._entities.get((cls, identity))

    def add(self, cls: type, identity: Any, obj: Any) -> None:
        self._entities[(cls, identity)] = obj

    def remove(self, cls: type, identity: Any) -> None:
        self._entities.pop((cls, identity), None)

    def clear(self) -> None:
        self._entities.clear()
