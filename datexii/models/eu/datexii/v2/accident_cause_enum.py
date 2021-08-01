from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AccidentCauseEnum(Enum):
    """
    Collection of the type of accident causes.

    :cvar AVOIDANCE_OF_OBSTACLES: Avoidance of obstacles on the roadway.
    :cvar DRIVER_DISTRACTION: Driver distraction.
    :cvar DRIVER_DRUG_ABUSE: Driver under the influence of drugs.
    :cvar DRIVER_ILLNESS: Driver illness.
    :cvar EXCEEDING_SPEEDS_LIMITS: Loss of vehicle control due to
        excessive vehicle speed.
    :cvar EXCESS_ALCOHOL: Driver abilities reduced due to driving under
        the influence of alcohol.  Alcohol levels above nationally
        accepted limit.
    :cvar EXCESSIVE_DRIVER_TIREDNESS: Excessive tiredness of the driver.
    :cvar IMPERMISSIBLE_MANOEUVRE: A driving manoeuvre which was not
        permitted.
    :cvar LIMITED_VISIBILITY: Limited or impaired visibility.
    :cvar NOT_KEEPING_ASAFE_DISTANCE: Not keeping a safe distance from
        the vehicle in front.
    :cvar ON_THE_WRONG_SIDE_OF_THE_ROAD: Driving on the wrong side of
        the road.
    :cvar PEDESTRIAN_IN_ROAD: Pedestrian in the roadway.
    :cvar POOR_LANE_ADHERENCE: Not keeping to lane.
    :cvar POOR_MERGE_ENTRY_OR_EXIT_JUDGEMENT: Poor judgement when
        merging at an entry or exit point of a carriageway or junction.
    :cvar POOR_ROAD_SURFACE_CONDITION: Poor road surface condition.
    :cvar POOR_SURFACE_ADHERENCE: Poor road surface adherence.
    :cvar UNDISCLOSED: Undisclosed cause.
    :cvar UNKNOWN: Unknown cause.
    :cvar VEHICLE_FAILURE: Malfunction or failure of vehicle function.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AVOIDANCE_OF_OBSTACLES = "avoidanceOfObstacles"
    DRIVER_DISTRACTION = "driverDistraction"
    DRIVER_DRUG_ABUSE = "driverDrugAbuse"
    DRIVER_ILLNESS = "driverIllness"
    EXCEEDING_SPEEDS_LIMITS = "exceedingSpeedsLimits"
    EXCESS_ALCOHOL = "excessAlcohol"
    EXCESSIVE_DRIVER_TIREDNESS = "excessiveDriverTiredness"
    IMPERMISSIBLE_MANOEUVRE = "impermissibleManoeuvre"
    LIMITED_VISIBILITY = "limitedVisibility"
    NOT_KEEPING_ASAFE_DISTANCE = "notKeepingASafeDistance"
    ON_THE_WRONG_SIDE_OF_THE_ROAD = "onTheWrongSideOfTheRoad"
    PEDESTRIAN_IN_ROAD = "pedestrianInRoad"
    POOR_LANE_ADHERENCE = "poorLaneAdherence"
    POOR_MERGE_ENTRY_OR_EXIT_JUDGEMENT = "poorMergeEntryOrExitJudgement"
    POOR_ROAD_SURFACE_CONDITION = "poorRoadSurfaceCondition"
    POOR_SURFACE_ADHERENCE = "poorSurfaceAdherence"
    UNDISCLOSED = "undisclosed"
    UNKNOWN = "unknown"
    VEHICLE_FAILURE = "vehicleFailure"
    OTHER = "other"
