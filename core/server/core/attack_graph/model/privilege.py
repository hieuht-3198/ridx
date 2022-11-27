


from enum import IntEnum


class Privilege(IntEnum):
    OS_ADMIN = 10
    OS_USER = 9
    APP_ADMIN = 8
    APP_USER = 7
    NONE = 1