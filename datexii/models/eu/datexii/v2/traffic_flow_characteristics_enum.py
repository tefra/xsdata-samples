from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TrafficFlowCharacteristicsEnum(Enum):
    """
    A collection of terms for describing the characteristics of traffic flow.

    :cvar ERRATIC_FLOW: Traffic flow is of an irregular nature, subject
        to sudden changes in rates.
    :cvar SMOOTH_FLOW: Traffic flow is smooth.
    :cvar STOP_AND_GO: Traffic flow is of a stop and go nature with
        queues forming and ending continuously on the specified section
        of road.
    :cvar TRAFFIC_BLOCKED: Traffic is blocked at the specified location
        and in the specified direction due to an unplanned event.
    """

    ERRATIC_FLOW = "erraticFlow"
    SMOOTH_FLOW = "smoothFlow"
    STOP_AND_GO = "stopAndGo"
    TRAFFIC_BLOCKED = "trafficBlocked"
