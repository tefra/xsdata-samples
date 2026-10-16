from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class ResponseMessageType2(StrEnum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
