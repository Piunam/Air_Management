from enum import Enum


class BoardingStatus(str, Enum):
    WAITING = "Waiting"
    BOARDING = "Boarding"
    COMPLETED = "Completed"