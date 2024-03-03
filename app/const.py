from enum import Enum, unique


@unique
class ResponseFormat(Enum):
    default = "*/*"
    html = "text/html"
    json = "application/json"


class _ENV(Enum):
    test = "test"
    development = "development"
    production = "production"


@unique
class LogLevel(Enum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
