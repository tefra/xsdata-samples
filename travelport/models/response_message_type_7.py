from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class ResponseMessageType7(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
