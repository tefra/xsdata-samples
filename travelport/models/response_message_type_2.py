from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class ResponseMessageType2(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
