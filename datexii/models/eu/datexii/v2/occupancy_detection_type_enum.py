from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OccupancyDetectionTypeEnum(Enum):
    """Type of parking occupancy detection (balancing, single slot, ...

    ).

    :cvar NONE: No occupancy detection available.
    :cvar BALANCING: Counting and balancing incoming and outcoming
        traffic amount ('indirect' method).
    :cvar SINGLE_SPACE_DETECTION: There is a detector for every
        individual parking space ('direct' method).
    :cvar MODEL_BASED: Occupancy detection is based on some model, i.e.
        hydrograph, forecasting or estimation.
    :cvar MANUAL: Manual collection of occupancy information, i.e.
        operators count the vehicles.
    :cvar UNSPECIFIED: Unspecified.
    :cvar OTHER: Other.
    :cvar UNKNOWN: Unknown.
    """
    NONE = "none"
    BALANCING = "balancing"
    SINGLE_SPACE_DETECTION = "singleSpaceDetection"
    MODEL_BASED = "modelBased"
    MANUAL = "manual"
    UNSPECIFIED = "unspecified"
    OTHER = "other"
    UNKNOWN = "unknown"
