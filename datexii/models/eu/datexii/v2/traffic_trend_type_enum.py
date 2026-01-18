from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TrafficTrendTypeEnum(Enum):
    """
    List of terms used to describe the trend in traffic conditions.

    :cvar TRAFFIC_BUILDING_UP: Traffic conditions are changing from
        free-flow to heavy or slow service levels.  Queues may also be
        expected.
    :cvar TRAFFIC_EASING: Traffic conditions are changing from heavy or
        slow service levels to free-flow.
    :cvar TRAFFIC_STABLE: Traffic conditions are currently stable.
    :cvar UNKNOWN: The trend of traffic conditions is currently unknown.
    """

    TRAFFIC_BUILDING_UP = "trafficBuildingUp"
    TRAFFIC_EASING = "trafficEasing"
    TRAFFIC_STABLE = "trafficStable"
    UNKNOWN = "unknown"
