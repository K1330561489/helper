from enum import Enum 

class Status(Enum):
    INIT = 0
    STOP = 1
    RUNNING = 2
    ERROR = 3
    CLOSE = 4

class ButtonStat(Enum):
    RUNNING = 0
    STOP = 1
    INITIALIZING = 2