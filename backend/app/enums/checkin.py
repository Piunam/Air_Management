from enum import Enum


class CheckInStatus(str, Enum):
    NOT_CHECKED_IN = "Not Checked In"
    CHECKED_IN = "Checked In"