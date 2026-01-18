from __future__ import annotations

from enum import Enum

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


class ErrorElementTypeLevel(Enum):
    ERROR = "ERROR"
    WARN = "WARN"
