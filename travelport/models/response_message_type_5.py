from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class ResponseMessageType5(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
