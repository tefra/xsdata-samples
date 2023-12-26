from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CauseTypeEnum(Enum):
    """
    Types of causes of situations which are not managed or are off network.

    :cvar ACCIDENT: Accident.
    :cvar CONGESTION: Traffic congestion.
    :cvar EARLIER_ACCIDENT: An earlier accident.
    :cvar EARLIER_EVENT: An earlier event.
    :cvar EARLIER_INCIDENT: An earlier incident.
    :cvar EQUIPMENT_FAILURE: Failure of roadside equipment.
    :cvar EXCESSIVE_HEAT: Excessive heat.
    :cvar FROST: Frost.
    :cvar HOLIDAY_TRAFFIC: Holiday traffic.
    :cvar INFRASTRUCTURE_FAILURE: Failure of road infrastructure.
    :cvar LARGE_NUMBERS_OF_VISITORS: Large numbers of visitors.
    :cvar OBSTRUCTION: Obstruction (of unspecified type) on the roadway.
    :cvar POLLUTION_ALERT: An alert relating to dangerous levels of
        pollution.
    :cvar POOR_WEATHER: Poor weather conditions.
    :cvar PROBLEMS_AT_BORDER_POST: Problems at the border crossing.
    :cvar PROBLEMS_AT_CUSTOM_POST: Problems at the customs post on the
        border.
    :cvar PROBLEMS_ON_LOCAL_ROADS: Problems (of an unspecified nature)
        on the local roads.
    :cvar RADIOACTIVE_LEAK_ALERT: Radioactive leak alert.
    :cvar ROADSIDE_EVENT: A roadside event (of unspecified nature)
        whether planned or not.
    :cvar RUBBER_NECKING: Drivers being distracted and turning to look
        at an accident or other roadside event.
    :cvar SECURITY_INCIDENT: A security incident.
    :cvar SHEAR_WEIGHT_OF_TRAFFIC: Shear weight of traffic.
    :cvar TECHNICAL_PROBLEMS: Technical problems.
    :cvar TERRORISM: A terrorist incident.
    :cvar TOXIC_CLOUD_ALERT: An alert relating to the release of toxic
        gases and/or particulates.
    :cvar VANDALISM: A vandalism incident.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ACCIDENT = "accident"
    CONGESTION = "congestion"
    EARLIER_ACCIDENT = "earlierAccident"
    EARLIER_EVENT = "earlierEvent"
    EARLIER_INCIDENT = "earlierIncident"
    EQUIPMENT_FAILURE = "equipmentFailure"
    EXCESSIVE_HEAT = "excessiveHeat"
    FROST = "frost"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    INFRASTRUCTURE_FAILURE = "infrastructureFailure"
    LARGE_NUMBERS_OF_VISITORS = "largeNumbersOfVisitors"
    OBSTRUCTION = "obstruction"
    POLLUTION_ALERT = "pollutionAlert"
    POOR_WEATHER = "poorWeather"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOM_POST = "problemsAtCustomPost"
    PROBLEMS_ON_LOCAL_ROADS = "problemsOnLocalRoads"
    RADIOACTIVE_LEAK_ALERT = "radioactiveLeakAlert"
    ROADSIDE_EVENT = "roadsideEvent"
    RUBBER_NECKING = "rubberNecking"
    SECURITY_INCIDENT = "securityIncident"
    SHEAR_WEIGHT_OF_TRAFFIC = "shearWeightOfTraffic"
    TECHNICAL_PROBLEMS = "technicalProblems"
    TERRORISM = "terrorism"
    TOXIC_CLOUD_ALERT = "toxicCloudAlert"
    VANDALISM = "vandalism"
    OTHER = "other"
