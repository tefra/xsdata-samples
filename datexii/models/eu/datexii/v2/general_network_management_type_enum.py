from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class GeneralNetworkManagementTypeEnum(Enum):
    """
    Types of network management actions.

    :cvar BRIDGE_SWING_IN_OPERATION: The bridge at the specified
        location has swung or lifted and is therefore temporarily closed
        to traffic.
    :cvar CONVOY_SERVICE: A convoy service is in operation.
    :cvar OBSTACLE_SIGNALLING: Signs are being put out before or around
        an obstacle to protect drivers.
    :cvar RAMP_METERING_IN_OPERATION: Ramp metering is now active at the
        specified location.
    :cvar TEMPORARY_TRAFFIC_LIGHTS: Traffic is being controlled by
        temporary traffic lights (red-yellow-green or red-green).
    :cvar TOLL_GATES_OPEN: Toll gates are open with no fee collection at
        the specified location.
    :cvar TRAFFIC_BEING_MANUALLY_DIRECTED: Traffic is being manually
        directed.
    :cvar TRAFFIC_HELD: Traffic in the specified direction is
        temporarily held up due to an unplanned event (e.g. for
        clearance of wreckage following an accident).
    :cvar OTHER: Other than as defined in this enumeration.
    """
    BRIDGE_SWING_IN_OPERATION = "bridgeSwingInOperation"
    CONVOY_SERVICE = "convoyService"
    OBSTACLE_SIGNALLING = "obstacleSignalling"
    RAMP_METERING_IN_OPERATION = "rampMeteringInOperation"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES_OPEN = "tollGatesOpen"
    TRAFFIC_BEING_MANUALLY_DIRECTED = "trafficBeingManuallyDirected"
    TRAFFIC_HELD = "trafficHeld"
    OTHER = "other"
