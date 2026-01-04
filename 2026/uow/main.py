from typing import Any

from mappers import UserMapper
from models import User
from uow_ import UoW


def main():
    user_mapper = UserMapper()
    uow = UoW[Any](mapper=user_mapper)

    # v1
    new_user = User(name="Deep")
    uow.register_new(new_user)
    uow.commit()

    # v2
    with uow:
        new_user = User(name="Peter")
        uow.register_new(new_user)


if __name__ == '__main__':
    main()
