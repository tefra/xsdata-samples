from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class ObsDimensionsCodeType(Enum):
    """
    ObsDimensionsCodeType is an enumeration containing the values
    "TimeDimension" and "AllDimensions".

    :cvar ALL_DIMENSIONS: AllDimensions notes that the cross sectional
        format shall be flat; that is all dimensions should be contained
        at the observation level.
    :cvar TIME_PERIOD: TIME_PERIOD refers to the fixed identifier for
        the time dimension.
    """

    ALL_DIMENSIONS = "AllDimensions"
    TIME_PERIOD = "TIME_PERIOD"
