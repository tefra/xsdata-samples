from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class PredictionStateEnum(Enum):
    NOT_ANNOUNCED = "NOT_ANNOUNCED"
    ANNOUNCED = "ANNOUNCED"
    REALIZED = "REALIZED"
    REVOKED = "REVOKED"


PredictionStateEnum.NOT_ANNOUNCED.__doc__ = (
    "This value is not exposed, it can be present in the database though."
)
