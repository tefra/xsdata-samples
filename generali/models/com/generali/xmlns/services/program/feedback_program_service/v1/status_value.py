from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


class StatusValue(StrEnum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    FAIL = "FAIL"
