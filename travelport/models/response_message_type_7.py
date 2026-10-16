from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class ResponseMessageType7(StrEnum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
