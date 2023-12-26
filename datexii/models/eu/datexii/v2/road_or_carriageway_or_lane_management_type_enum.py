from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadOrCarriagewayOrLaneManagementTypeEnum(Enum):
    """
    Management actions relating to road, carriageway or lane usage.

    :cvar CAR_POOL_LANE_IN_OPERATION: Dedicated car pool lane(s) are in
        operation for vehicles carrying at least the specified number of
        occupants.
    :cvar CARRIAGEWAY_CLOSURES: Carriageway closures are in operation at
        the specified location.
    :cvar CLEAR_ALANE_FOR_EMERGENCY_VEHICLES: Clear a lane for emergency
        vehicles.
    :cvar CLEAR_ALANE_FOR_SNOWPLOUGHS_AND_GRITTING_VEHICLES: Clear a
        lane for snow ploughs and gritting vehicles.
    :cvar CLOSED_PERMANENTLY_FOR_THE_WINTER: The road is closed to
        vehicles with the specified characteristics or all, if none
        defined, for the duration of the winter.
    :cvar CONTRAFLOW: Two-way traffic is temporarily sharing a single
        carriageway.
    :cvar DO_NOT_USE_SPECIFIED_LANES_OR_CARRIAGEWAYS: Do not use the
        specified lane(s) or carriageway(s).
    :cvar HARD_SHOULDER_RUNNING_IN_OPERATION: The hard shoulder is open
        as an operational lane.
    :cvar HEIGHT_RESTRICTION_IN_OPERATION: A height restriction is in
        operation.
    :cvar INTERMITTENT_SHORT_TERM_CLOSURES: Road closures occur
        intermittently on the specified road in the specified direction
        for short durations.
    :cvar KEEP_TO_THE_LEFT: Keep to the left.
    :cvar KEEP_TO_THE_RIGHT: Keep to the right.
    :cvar LANE_CLOSURES: Lane closures are in operation at the specified
        location for vehicles with the specified characteristics or all,
        if none defined, in the specified direction.
    :cvar LANES_DEVIATED: Lane deviations are in operation at the
        specified location.
    :cvar NARROW_LANES: Normal lane widths are temporarily reduced.
    :cvar NEW_ROADWORKS_LAYOUT: A new layout of lanes/carriageway has
        been implemented associated with roadworks.
    :cvar OVERNIGHT_CLOSURES: Every night the road is closed to vehicles
        with the specified characteristics or all, if none defined, in
        the specified direction by decision of the appropriate
        authorities.
    :cvar ROAD_CLEARED: The road has been cleared of earlier reported
        problems.
    :cvar ROAD_CLOSED: The road is closed to vehicles with the specified
        characteristics or all, if none defined, in the specified
        direction.
    :cvar ROLLING_ROAD_BLOCK: Traffic officers or police are driving
        slowly in front of a queue of traffic to create a gap in the
        traffic to allow for clearance activities to take place in
        safety on the road ahead.
    :cvar RUSH_HOUR_LANE_IN_OPERATION: Dedicated rush (peak) hour
        lane(s) are in operation.
    :cvar SINGLE_ALTERNATE_LINE_TRAFFIC: Traffic is being controlled to
        move in alternate single lines. This control may be undertaken
        by traffic lights or flagman.
    :cvar TIDAL_FLOW_LANE_IN_OPERATION: Dedicated tidal flow lane(s) are
        in operation in the specified direction.
    :cvar TURN_AROUND_IN_OPERATION: Traffic is being directed back down
        the opposite carriageway, possibly requiring the temporary
        removal of the central crash barrier.
    :cvar USE_OF_SPECIFIED_LANES_OR_CARRIAGEWAYS_ALLOWED: The specified
        lane(s) or carriageway(s) may be used. The normal lane(s) or
        carriageway(s) restrictions are not currently in force.
    :cvar USE_SPECIFIED_LANES_OR_CARRIAGEWAYS: Use the specified lane(s)
        or carriageway(s).
    :cvar VEHICLE_STORAGE_IN_OPERATION: Vehicles are being stored on the
        roadway and/or at a rest area or service area at the specified
        location.
    :cvar WEIGHT_RESTRICTION_IN_OPERATION: A weight restriction is in
        operation.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    CAR_POOL_LANE_IN_OPERATION = "carPoolLaneInOperation"
    CARRIAGEWAY_CLOSURES = "carriagewayClosures"
    CLEAR_ALANE_FOR_EMERGENCY_VEHICLES = "clearALaneForEmergencyVehicles"
    CLEAR_ALANE_FOR_SNOWPLOUGHS_AND_GRITTING_VEHICLES = (
        "clearALaneForSnowploughsAndGrittingVehicles"
    )
    CLOSED_PERMANENTLY_FOR_THE_WINTER = "closedPermanentlyForTheWinter"
    CONTRAFLOW = "contraflow"
    DO_NOT_USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = (
        "doNotUseSpecifiedLanesOrCarriageways"
    )
    HARD_SHOULDER_RUNNING_IN_OPERATION = "hardShoulderRunningInOperation"
    HEIGHT_RESTRICTION_IN_OPERATION = "heightRestrictionInOperation"
    INTERMITTENT_SHORT_TERM_CLOSURES = "intermittentShortTermClosures"
    KEEP_TO_THE_LEFT = "keepToTheLeft"
    KEEP_TO_THE_RIGHT = "keepToTheRight"
    LANE_CLOSURES = "laneClosures"
    LANES_DEVIATED = "lanesDeviated"
    NARROW_LANES = "narrowLanes"
    NEW_ROADWORKS_LAYOUT = "newRoadworksLayout"
    OVERNIGHT_CLOSURES = "overnightClosures"
    ROAD_CLEARED = "roadCleared"
    ROAD_CLOSED = "roadClosed"
    ROLLING_ROAD_BLOCK = "rollingRoadBlock"
    RUSH_HOUR_LANE_IN_OPERATION = "rushHourLaneInOperation"
    SINGLE_ALTERNATE_LINE_TRAFFIC = "singleAlternateLineTraffic"
    TIDAL_FLOW_LANE_IN_OPERATION = "tidalFlowLaneInOperation"
    TURN_AROUND_IN_OPERATION = "turnAroundInOperation"
    USE_OF_SPECIFIED_LANES_OR_CARRIAGEWAYS_ALLOWED = (
        "useOfSpecifiedLanesOrCarriagewaysAllowed"
    )
    USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "useSpecifiedLanesOrCarriageways"
    VEHICLE_STORAGE_IN_OPERATION = "vehicleStorageInOperation"
    WEIGHT_RESTRICTION_IN_OPERATION = "weightRestrictionInOperation"
    OTHER = "other"
