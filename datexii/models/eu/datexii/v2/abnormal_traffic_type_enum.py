from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AbnormalTrafficTypeEnum(Enum):
    """
    Collection of descriptive terms for abnormal traffic conditions
    specifically relating to the nature of the traffic movement.

    :cvar STATIONARY_TRAFFIC: Traffic is stationary, or very near
        stationary, at the specified location (i.e. average speed is
        less than 10% of its free-flow level).
    :cvar QUEUING_TRAFFIC: Traffic is queuing at the specified location,
        although there is still some traffic movement (i.e. average
        speed is between 10% and 25% of its free-flow level).
    :cvar SLOW_TRAFFIC: Traffic is slow moving at the specified
        location, but not yet forming queues (i.e. average speed is
        between 25% and 75% of its free-flow level).
    :cvar HEAVY_TRAFFIC: Traffic is heavy at the specified location
        (i.e. average speed is between 75% and 90% of its free-flow
        level).
    :cvar UNSPECIFIED_ABNORMAL_TRAFFIC: There are abnormal traffic
        conditions of an unspecified nature at the specified location.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    STATIONARY_TRAFFIC = "stationaryTraffic"
    QUEUING_TRAFFIC = "queuingTraffic"
    SLOW_TRAFFIC = "slowTraffic"
    HEAVY_TRAFFIC = "heavyTraffic"
    UNSPECIFIED_ABNORMAL_TRAFFIC = "unspecifiedAbnormalTraffic"
    OTHER = "other"
