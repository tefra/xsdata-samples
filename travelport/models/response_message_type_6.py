from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class ResponseMessageType6(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
