from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class ResponseMessageType4(StrEnum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
