from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LaneEnum(Enum):
    """
    List of descriptors identifying specific lanes.

    :cvar ALL_LANES_COMPLETE_CARRIAGEWAY: In all lanes of the
        carriageway.
    :cvar BUS_LANE: In the bus lane.
    :cvar BUS_STOP: In the bus stop lane.
    :cvar CAR_POOL_LANE: In the carpool lane.
    :cvar CENTRAL_RESERVATION: On the central median separating the two
        directional carriageways of the highway.
    :cvar CRAWLER_LANE: In the crawler lane.
    :cvar EMERGENCY_LANE: In the emergency lane.
    :cvar ESCAPE_LANE: In the escape lane.
    :cvar EXPRESS_LANE: In the express lane.
    :cvar HARD_SHOULDER: On the hard shoulder.
    :cvar HEAVY_VEHICLE_LANE: In the heavy vehicle lane.
    :cvar LANE1: In the first lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE2: In the second lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE3: In the third lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE4: In the fourth lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE5: In the fifth lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE6: In the sixth lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE7: In the seventh lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE8: In the eighth lane numbered from nearest the hard
        shoulder to central median.
    :cvar LANE9: In the ninth lane numbered from nearest the hard
        shoulder to central median.
    :cvar LAY_BY: In a lay-by.
    :cvar LEFT_HAND_TURNING_LANE: In the left hand turning lane.
    :cvar LEFT_LANE: In the left lane.
    :cvar LOCAL_TRAFFIC_LANE: In the local traffic lane.
    :cvar MIDDLE_LANE: In the middle lane.
    :cvar OPPOSING_LANES: In the opposing lanes.
    :cvar OVERTAKING_LANE: In the overtaking lane.
    :cvar RIGHT_HAND_TURNING_LANE: In the right hand turning lane.
    :cvar RIGHT_LANE: In the right lane.
    :cvar RUSH_HOUR_LANE: In the lane dedicated for use during the rush
        (peak) hour.
    :cvar SET_DOWN_AREA: In the area/lane reserved for passenger pick-up
        or set-down.
    :cvar SLOW_VEHICLE_LANE: In the slow vehicle lane.
    :cvar THROUGH_TRAFFIC_LANE: In the through traffic lane.
    :cvar TIDAL_FLOW_LANE: In the lane dedicated for use as a tidal flow
        lane.
    :cvar TURNING_LANE: In the turning lane.
    :cvar VERGE: On the verge.
    """

    ALL_LANES_COMPLETE_CARRIAGEWAY = "allLanesCompleteCarriageway"
    BUS_LANE = "busLane"
    BUS_STOP = "busStop"
    CAR_POOL_LANE = "carPoolLane"
    CENTRAL_RESERVATION = "centralReservation"
    CRAWLER_LANE = "crawlerLane"
    EMERGENCY_LANE = "emergencyLane"
    ESCAPE_LANE = "escapeLane"
    EXPRESS_LANE = "expressLane"
    HARD_SHOULDER = "hardShoulder"
    HEAVY_VEHICLE_LANE = "heavyVehicleLane"
    LANE1 = "lane1"
    LANE2 = "lane2"
    LANE3 = "lane3"
    LANE4 = "lane4"
    LANE5 = "lane5"
    LANE6 = "lane6"
    LANE7 = "lane7"
    LANE8 = "lane8"
    LANE9 = "lane9"
    LAY_BY = "layBy"
    LEFT_HAND_TURNING_LANE = "leftHandTurningLane"
    LEFT_LANE = "leftLane"
    LOCAL_TRAFFIC_LANE = "localTrafficLane"
    MIDDLE_LANE = "middleLane"
    OPPOSING_LANES = "opposingLanes"
    OVERTAKING_LANE = "overtakingLane"
    RIGHT_HAND_TURNING_LANE = "rightHandTurningLane"
    RIGHT_LANE = "rightLane"
    RUSH_HOUR_LANE = "rushHourLane"
    SET_DOWN_AREA = "setDownArea"
    SLOW_VEHICLE_LANE = "slowVehicleLane"
    THROUGH_TRAFFIC_LANE = "throughTrafficLane"
    TIDAL_FLOW_LANE = "tidalFlowLane"
    TURNING_LANE = "turningLane"
    VERGE = "verge"
