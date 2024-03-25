from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class EpochPeriodType(Enum):
    """
    EpochPeriodType defines an enumeration of epoch period types.
    """

    NANOSECOND = "nanosecond"
    MILLISECOND = "millisecond"
    MICROSECOND = "microsecond"
    SECOND = "second"
    DAY = "day"
