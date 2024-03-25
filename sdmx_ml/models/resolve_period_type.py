from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class ResolvePeriodType(Enum):
    """
    ResolvePeriodType defines an enumeration of how date periods should be
    resolved.
    """

    START_OF_PERIOD = "startOfPeriod"
    END_OF_PERIOD = "endOfPeriod"
    MID_PERIOD = "midPeriod"
