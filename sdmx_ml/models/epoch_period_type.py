from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


class EpochPeriodType(StrEnum):
    """
    EpochPeriodType defines an enumeration of epoch period types.
    """

    NANOSECOND = "nanosecond"
    MILLISECOND = "millisecond"
    MICROSECOND = "microsecond"
    SECOND = "second"
    DAY = "day"
