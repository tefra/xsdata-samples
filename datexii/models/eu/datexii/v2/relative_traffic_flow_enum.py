from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RelativeTrafficFlowEnum(Enum):
    """
    Levels of assessment of the traffic flow conditions relative to normally
    expected conditions at this date/time.

    :cvar TRAFFIC_VERY_MUCH_HEAVIER_THAN_NORMAL: Traffic is very much
        heavier than normally expected at the specified location at this
        date/time.
    :cvar TRAFFIC_HEAVIER_THAN_NORMAL: Traffic is heavier than normally
        expected at the specified location at this date/time.
    :cvar TRAFFIC_FLOW_NORMAL: Traffic flow is normal at the specified
        location at this date/time.
    :cvar TRAFFIC_LIGHTER_THAN_NORMAL: Traffic is lighter than normally
        expected at the specified location at this date/time.
    :cvar TRAFFIC_VERY_MUCH_LIGHTER_THAN_NORMAL: Traffic is very much
        lighter than normally expected at the specified location at this
        date/time.
    """

    TRAFFIC_VERY_MUCH_HEAVIER_THAN_NORMAL = "trafficVeryMuchHeavierThanNormal"
    TRAFFIC_HEAVIER_THAN_NORMAL = "trafficHeavierThanNormal"
    TRAFFIC_FLOW_NORMAL = "trafficFlowNormal"
    TRAFFIC_LIGHTER_THAN_NORMAL = "trafficLighterThanNormal"
    TRAFFIC_VERY_MUCH_LIGHTER_THAN_NORMAL = "trafficVeryMuchLighterThanNormal"
