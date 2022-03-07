from enum import Enum

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


class StatusValue(Enum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    FAIL = "FAIL"
