from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeResultMessageType1(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
