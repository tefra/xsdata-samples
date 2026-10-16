from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


class ErrorElementTypeLevel(StrEnum):
    ERROR = "ERROR"
    WARN = "WARN"
