from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from datexii.models.datexii_3_common import (
    GlobalReference,
    GroupOfVehiclesInvolved,
    HeaderInformation,
    Humidity,
    InternationalIdentifier,
    MultilingualString,
    PayloadPublication,
    Pollution,
    PrecipitationDetail,
    Pressure,
    RoadSurfaceConditionMeasurements,
    Source,
    Temperature,
    UrlLink,
    Validity,
    Vehicle,
    VehicleCharacteristics,
    VersionedReference,
    Visibility,
    Wind,
    ConfidentialityValueEnum2,
    ExtensionType,
    PublicEventTypeEnum2,
    TrafficTrendTypeEnum2,
    VehicleTypeEnum2,
    WeatherRelatedRoadConditionTypeEnum2,
    WinterEquipmentManagementTypeEnum2,
)
from datexii.models.datexii_3_location_referencing import (
    Destination,
    Itinerary,
    LocationReference,
    DirectionEnum2,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/situation"


class AbnormalTrafficTypeEnum1(Enum):
    """
    Descriptive terms for abnormal traffic conditions specifically relating to
    the nature of the traffic movement, implying levels of service.

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
    :cvar EXTENDED:
    """
    STATIONARY_TRAFFIC = "stationaryTraffic"
    QUEUING_TRAFFIC = "queuingTraffic"
    SLOW_TRAFFIC = "slowTraffic"
    HEAVY_TRAFFIC = "heavyTraffic"
    UNSPECIFIED_ABNORMAL_TRAFFIC = "unspecifiedAbnormalTraffic"
    OTHER = "other"
    EXTENDED = "_extended"


class AccidentCauseEnum1(Enum):
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
    :cvar EXTENDED:
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
    EXTENDED = "_extended"


class AccidentTypeEnum1(Enum):
    """
    Collection of descriptive terms for types of accidents.

    :cvar ACCIDENT: Accidents are situations in which one or more
        vehicles lose control and do not recover.  They include
        collisions between vehicle(s) or other road user(s), between
        vehicle(s) and fixed obstacle(s), or they result from a vehicle
        running off the road.
    :cvar ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS: Includes all accidents
        involving at least one vehicle believed to be carrying
        materials, which could present an additional hazard to road
        users.
    :cvar ACCIDENT_INVOLVING_HEAVY_LORRIES: Includes all accidents
        involving at least one heavy goods vehicle.
    :cvar ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE: Includes all
        accidents involving at least one mass transit vehicle.
    :cvar ACCIDENT_INVOLVING_PUBLIC_TRANSPORT: Includes all accidents
        involving public transport
    :cvar ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL: Accident involving
        radioactive material.
    :cvar ACCIDENT_INVOLVING_TRAIN: Includes all accidents involving
        collision with a train.
    :cvar COLLISION: Collision of vehicle with another object of
        unspecified type.
    :cvar MULTIPLE_VEHICLE_ACCIDENT: Includes all accidents involving
        three or more vehicles.
    :cvar SECONDARY_ACCIDENT: Includes all situations resulting from
        vehicles avoiding or being distracted by earlier accidents.
    :cvar SERIOUS_INJURY_OR_FATAL_ACCIDENT: Includes all accidents
        believed to involve fatality or injury expected to require
        overnight hospitalisation.
    :cvar VEHICLE_STUCK_UNDER_BRIDGE: A vehicle is stuck under a bridge.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ACCIDENT = "accident"
    ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS = "accidentInvolvingHazardousMaterials"
    ACCIDENT_INVOLVING_HEAVY_LORRIES = "accidentInvolvingHeavyLorries"
    ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE = "accidentInvolvingMassTransitVehicle"
    ACCIDENT_INVOLVING_PUBLIC_TRANSPORT = "accidentInvolvingPublicTransport"
    ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL = "accidentInvolvingRadioactiveMaterial"
    ACCIDENT_INVOLVING_TRAIN = "accidentInvolvingTrain"
    COLLISION = "collision"
    MULTIPLE_VEHICLE_ACCIDENT = "multipleVehicleAccident"
    SECONDARY_ACCIDENT = "secondaryAccident"
    SERIOUS_INJURY_OR_FATAL_ACCIDENT = "seriousInjuryOrFatalAccident"
    VEHICLE_STUCK_UNDER_BRIDGE = "vehicleStuckUnderBridge"
    OTHER = "other"
    EXTENDED = "_extended"


class AnimalPresenceTypeEnum1(Enum):
    """
    Types of animal presence.

    :cvar ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to animals
        on the roadway.
    :cvar HERD_OF_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to a
        herd of animals on the roadway.
    :cvar LARGE_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to
        large animals on the roadway.
    :cvar SMALL_ANIMALS_ON_THE_ROAD: Small animals (that may fit
        underneath vehicle frames) are on the road
    :cvar WILD_ANIMALS_ON_THE_ROAD: Wild animals (not controlled by
        humans) are on the road
    :cvar EXTENDED:
    """
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    HERD_OF_ANIMALS_ON_THE_ROAD = "herdOfAnimalsOnTheRoad"
    LARGE_ANIMALS_ON_THE_ROAD = "largeAnimalsOnTheRoad"
    SMALL_ANIMALS_ON_THE_ROAD = "smallAnimalsOnTheRoad"
    WILD_ANIMALS_ON_THE_ROAD = "wildAnimalsOnTheRoad"
    EXTENDED = "_extended"


class AuthorityOperationTypeEnum1(Enum):
    """
    Types of authority operations.

    :cvar ACCIDENT_INVESTIGATION_WORK: An operation involving authorised
        investigation work connected to an earlier reported accident.
    :cvar BOMB_SQUAD_IN_ACTION: An operation where a bomb squad is in
        action to deal with suspected or actual explosive or incendiary
        devices which may cause disruption to traffic.
    :cvar CIVIL_EMERGENCY: A situation, perceived or actual, relating to
        a civil emergency which could disrupt traffic.  This includes
        large scale destruction, through events such as earthquakes,
        insurrection, and civil disobedience.
    :cvar CUSTOMS_OPERATION: A permanent or temporary operation
        established by customs and excise authorities on or adjacent to
        the carriageway.
    :cvar JURIDICAL_RECONSTRUCTION: An operation involving the juridical
        reconstruction of events for the purposes of judicial or legal
        proceedings.
    :cvar POLICE_CHECK_POINT: A permanent or temporary operation
        established on or adjacent to the carriageway for use by police
        or other authorities.
    :cvar POLICE_INVESTIGATION: A temporary operation established on or
        adjacent to the carriageway by the police associated with an
        ongoing investigation.
    :cvar ROAD_OPERATOR_CHECK_POINT: A permanent or temporary operation
        established on or adjacent to the carriageway for use by the
        road operator, such as for survey or inspection purposes, but
        not for traffic management purposes.
    :cvar SNOW_CHAIN_ON_BOARD_OR_SNOW_TYRES_MOUNTED_CHECK: the police
        are checking if snow chains are on board vehicles or vehicles
        have snow tyres mounted
    :cvar SNOW_CHAIN_OR_SNOW_TYRES_MOUNTED_CHECK: the police are
        checking if snow chains or snow tyres are mounted on vehicles
    :cvar SURVEY: A permanent or temporary operation established by
        authorities on or adjacent to the carriageway for the purpose of
        gathering statistics or other traffic related information.
    :cvar TRANSPORT_OF_VIP: An operation to transport one or more VIPs.
    :cvar UNDEFINED_AUTHORITY_ACTIVITY: An authority activity of
        undefined type.
    :cvar VEHICLE_INSPECTION_CHECK_POINT: A permanent or temporary
        operation established on or adjacent to the carriageway for
        inspection of vehicles by authorities (e.g. vehicle safety
        checks and tachograph checks).
    :cvar VEHICLE_WEIGHING: A permanent or temporary operation
        established on or adjacent to the carriageway for weighing of
        vehicles by authorities.
    :cvar WEIGH_IN_MOTION: A permanent or temporary facility established
        by authorities on the carriageway for weighing vehicles while in
        motion.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ACCIDENT_INVESTIGATION_WORK = "accidentInvestigationWork"
    BOMB_SQUAD_IN_ACTION = "bombSquadInAction"
    CIVIL_EMERGENCY = "civilEmergency"
    CUSTOMS_OPERATION = "customsOperation"
    JURIDICAL_RECONSTRUCTION = "juridicalReconstruction"
    POLICE_CHECK_POINT = "policeCheckPoint"
    POLICE_INVESTIGATION = "policeInvestigation"
    ROAD_OPERATOR_CHECK_POINT = "roadOperatorCheckPoint"
    SNOW_CHAIN_ON_BOARD_OR_SNOW_TYRES_MOUNTED_CHECK = "snowChainOnBoardOrSnowTyresMountedCheck"
    SNOW_CHAIN_OR_SNOW_TYRES_MOUNTED_CHECK = "snowChainOrSnowTyresMountedCheck"
    SURVEY = "survey"
    TRANSPORT_OF_VIP = "transportOfVip"
    UNDEFINED_AUTHORITY_ACTIVITY = "undefinedAuthorityActivity"
    VEHICLE_INSPECTION_CHECK_POINT = "vehicleInspectionCheckPoint"
    VEHICLE_WEIGHING = "vehicleWeighing"
    WEIGH_IN_MOTION = "weighInMotion"
    OTHER = "other"
    EXTENDED = "_extended"


class CauseTypeEnum1(Enum):
    """
    Types of causes of situations which are not managed or are off network.

    :cvar ABNORMAL_TRAFFIC: A traffic condition that is not normal.
    :cvar ACCIDENT: Accident.
    :cvar ANIMAL_PRESENCE: An obstruction on the road resulting from the
        presence of animals
    :cvar AUTHORITY_OPERATION: Authority initiated operation or activity
    :cvar CONSTRUCTION_WORK: Roadworks involving the construction of new
        infrastructure.
    :cvar DISTURBANCE: Deliberate human action of either a public
        disorder nature or of a situation alert type which could disrupt
        traffic.
    :cvar DRIVING_CONDITIONS: Degraded driving conditions.
    :cvar ENVIRONMENTAL_OBSTRUCTION: An obstruction on the road
        resulting from an environmental cause
    :cvar EQUIPMENT_OR_SYSTEM_FAULT: Equipment or system which is
        faulty, malfunctioning or not in a fully operational state
    :cvar INFRASTRUCTURE_DAMAGE_OBSTRUCTION: An obstruction on the road
        resulting from the failure or damage of infrastructure on,
        under, above or close to the road
    :cvar INSTRUCTION_TO_ROAD_USERS: Instruction and/or message issued
        by the network/road operator
    :cvar NETWORK_MANAGEMENT: Network management action which is
        applicable to the road network and its users.
    :cvar NON_WEATHER_RELATED_ROAD_CONDITIONS: Road surface conditions
        that are not related to the weather
    :cvar OBSTRUCTION: Obstruction on the roadway.
    :cvar POOR_ENVIRONMENT: Poor environmental conditions
    :cvar PUBLIC_EVENT: Organised public event
    :cvar REROUTING: Rerouting management action issued by the
        network/road operator
    :cvar ROAD_MAINTENANCE: Roadworks involving the maintenance or
        installation of infrastructure
    :cvar ROAD_OPERATOR_SERVICE_DISRUPTION: Disruption to normal road
        operator services
    :cvar ROAD_OR_CARRIAGEWAY_OR_LANE_MANAGEMENT: Road, carriageway or
        lane management action instigated by the network/road operator
    :cvar ROADSIDE_ASSISTANCE: Road side assistance
    :cvar ROADSIDE_SERVICE_DISRUPTION: Disruption to normal roadside
        services
    :cvar SPEED_MANAGEMENT: Speed management action instigated by the
        network/road operator
    :cvar TRANSIT_SERVICE_DISRUPTION: Disruption to transit services of
        direct relevance to road users, e.g. connecting rail or ferry
        services
    :cvar VEHICLE_OBSTRUCTION: An obstruction on the road caused by one
        or more vehicles.
    :cvar WEATHER_RELATED_ROAD_CONDITIONS: Road surface conditions
        related to the weather
    :cvar WINTER_EQUIPMENT_MANAGEMENT: Winter driving management action
        instigated by the network/road operator
    :cvar EARLIER_EVENT: An earlier event.
    :cvar EARLIER_INCIDENT: An earlier incident.
    :cvar HOLIDAY_TRAFFIC: Holiday traffic.
    :cvar PROBLEMS_AT_BORDER_POST: Problems at the border crossing.
    :cvar PROBLEMS_AT_CUSTOM_POST: Problems at the customs post on the
        border.
    :cvar PROBLEMS_ON_LOCAL_ROADS: Problems (of an unspecified nature)
        on the local roads.
    :cvar ROADSIDE_EVENT: A roadside event (of unspecified nature)
        whether planned or not.
    :cvar RUBBER_NECKING: Drivers being distracted and turning to look
        at an accident or other roadside event.
    :cvar TECHNICAL_PROBLEMS: Technical problems.
    :cvar VANDALISM: A vandalism incident.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ABNORMAL_TRAFFIC = "abnormalTraffic"
    ACCIDENT = "accident"
    ANIMAL_PRESENCE = "animalPresence"
    AUTHORITY_OPERATION = "authorityOperation"
    CONSTRUCTION_WORK = "constructionWork"
    DISTURBANCE = "disturbance"
    DRIVING_CONDITIONS = "drivingConditions"
    ENVIRONMENTAL_OBSTRUCTION = "environmentalObstruction"
    EQUIPMENT_OR_SYSTEM_FAULT = "equipmentOrSystemFault"
    INFRASTRUCTURE_DAMAGE_OBSTRUCTION = "infrastructureDamageObstruction"
    INSTRUCTION_TO_ROAD_USERS = "instructionToRoadUsers"
    NETWORK_MANAGEMENT = "networkManagement"
    NON_WEATHER_RELATED_ROAD_CONDITIONS = "nonWeatherRelatedRoadConditions"
    OBSTRUCTION = "obstruction"
    POOR_ENVIRONMENT = "poorEnvironment"
    PUBLIC_EVENT = "publicEvent"
    REROUTING = "rerouting"
    ROAD_MAINTENANCE = "roadMaintenance"
    ROAD_OPERATOR_SERVICE_DISRUPTION = "roadOperatorServiceDisruption"
    ROAD_OR_CARRIAGEWAY_OR_LANE_MANAGEMENT = "roadOrCarriagewayOrLaneManagement"
    ROADSIDE_ASSISTANCE = "roadsideAssistance"
    ROADSIDE_SERVICE_DISRUPTION = "roadsideServiceDisruption"
    SPEED_MANAGEMENT = "speedManagement"
    TRANSIT_SERVICE_DISRUPTION = "transitServiceDisruption"
    VEHICLE_OBSTRUCTION = "vehicleObstruction"
    WEATHER_RELATED_ROAD_CONDITIONS = "weatherRelatedRoadConditions"
    WINTER_EQUIPMENT_MANAGEMENT = "winterEquipmentManagement"
    EARLIER_EVENT = "earlierEvent"
    EARLIER_INCIDENT = "earlierIncident"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOM_POST = "problemsAtCustomPost"
    PROBLEMS_ON_LOCAL_ROADS = "problemsOnLocalRoads"
    ROADSIDE_EVENT = "roadsideEvent"
    RUBBER_NECKING = "rubberNecking"
    TECHNICAL_PROBLEMS = "technicalProblems"
    VANDALISM = "vandalism"
    OTHER = "other"
    EXTENDED = "_extended"


class CollisionTypeEnum1(Enum):
    """
    Identifies a type of collision.

    :cvar COLLISION_WITH_ANIMAL: Collision of vehicle with one or more
        animals.
    :cvar COLLISION_WITH_OBSTACLE: Collision of vehicle with an object
        of a stationary nature.
    :cvar COLLISION_WITH_PERSON: Collision of vehicle with one or more
        pedestrians.
    :cvar HEAD_ON_COLLISION: Collision of vehicle with another vehicle
        head on.
    :cvar HEAD_ON_OR_SIDE_COLLISION: Collision of vehicle with another
        vehicle either head on or sideways.
    :cvar MULTIPLE_VEHICLE_COLLISION: Collision involving multiple
        vehicles
    :cvar REAR_COLLISION: Includes all accidents where one or more
        vehicles have collided with the rear of one or more other
        vehicles.
    :cvar SIDE_COLLISION: Includes all accidents where one or more
        vehicles have collided with the side of one or more other
        vehicles.
    :cvar EXTENDED:
    """
    COLLISION_WITH_ANIMAL = "collisionWithAnimal"
    COLLISION_WITH_OBSTACLE = "collisionWithObstacle"
    COLLISION_WITH_PERSON = "collisionWithPerson"
    HEAD_ON_COLLISION = "headOnCollision"
    HEAD_ON_OR_SIDE_COLLISION = "headOnOrSideCollision"
    MULTIPLE_VEHICLE_COLLISION = "multipleVehicleCollision"
    REAR_COLLISION = "rearCollision"
    SIDE_COLLISION = "sideCollision"
    EXTENDED = "_extended"


class CommentTypeEnum1(Enum):
    """
    Classification of comment types.

    :cvar ABNORMAL_LOAD_MOVEMENT_NOTE: A free text human oriented note
        describing details of abnormal load movements associated with
        the SituationRecord.
    :cvar DATA_PROCESSING_NOTE: A free text human oriented note
        describing the way the information in the SituationRecord has
        been or should be processed.
    :cvar DESCRIPTION: A free text human oriented description of the
        situation element defined by the SituationRecord.
    :cvar INTERNAL_NOTE: A free text human oriented note that supports
        internal traffic control operations relating to the situation
        element defined by the SituationRecord.
    :cvar ROADWORKS_NAME: Human-readable name by which the associated
        roadworks is known
    :cvar WARNING: A free text human oriented warning relating to the
        SituationRecord, such as advising the recipient that an advanced
        warning on VMS should be activated.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ABNORMAL_LOAD_MOVEMENT_NOTE = "abnormalLoadMovementNote"
    DATA_PROCESSING_NOTE = "dataProcessingNote"
    DESCRIPTION = "description"
    INTERNAL_NOTE = "internalNote"
    ROADWORKS_NAME = "roadworksName"
    WARNING = "warning"
    OTHER = "other"
    EXTENDED = "_extended"


class ComplianceOptionEnum1(Enum):
    """
    Types of compliance.

    :cvar ADVISORY: Advisory compliance.
    :cvar MANDATORY: Mandatory compliance.
    :cvar EXTENDED:
    """
    ADVISORY = "advisory"
    MANDATORY = "mandatory"
    EXTENDED = "_extended"


class ConstructionWorkTypeEnum1(Enum):
    """
    Types of works relating to construction.

    :cvar BLASTING_WORK: Blasting or quarrying work at the specified
        location.
    :cvar CONSTRUCTION_WORK: Construction work of a general nature at
        the specified location.
    :cvar DEMOLITION_WORK: Demolition work associated with the
        construction work.
    :cvar ROAD_IMPROVEMENT_OR_UPGRADING: Construction work associated
        with improvements to the road or its layout or with it
        upgrading.
    :cvar ROAD_WIDENING_WORK: Road widening work at the specified
        location.
    :cvar EXTENDED:
    """
    BLASTING_WORK = "blastingWork"
    CONSTRUCTION_WORK = "constructionWork"
    DEMOLITION_WORK = "demolitionWork"
    ROAD_IMPROVEMENT_OR_UPGRADING = "roadImprovementOrUpgrading"
    ROAD_WIDENING_WORK = "roadWideningWork"
    EXTENDED = "_extended"


class DelayBandEnum1(Enum):
    """
    Classifications of a delay banded by length (i.e. the additional travel
    time).

    :cvar NEGLIGIBLE: Negligible delay.
    :cvar UP_TO_TEN_MINUTES: Delay up to ten minutes.
    :cvar BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES: Delay between ten
        minutes and thirty minutes.
    :cvar BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR: Delay between thirty
        minutes and one hour.
    :cvar BETWEEN_ONE_HOUR_AND_THREE_HOURS: Delay between one hour and
        three hours.
    :cvar BETWEEN_THREE_HOURS_AND_SIX_HOURS: Delay between three hours
        and six hours.
    :cvar LONGER_THAN_SIX_HOURS: Delay longer than six hours.
    :cvar EXTENDED:
    """
    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = "betweenTenMinutesAndThirtyMinutes"
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"
    EXTENDED = "_extended"


class DelaysTypeEnum1(Enum):
    """
    Course classifications of a delay.

    :cvar DELAYS: Delays on the road network as a result of any
        situation which causes hold-ups.
    :cvar DELAYS_OF_UNCERTAIN_DURATION: Delays on the road network whose
        predicted duration cannot be estimated.
    :cvar LONG_DELAYS: Delays on the road network of unusual severity.
    :cvar VERY_LONG_DELAYS: Delays on the road network of abnormally
        unusual severity.
    :cvar EXTENDED:
    """
    DELAYS = "delays"
    DELAYS_OF_UNCERTAIN_DURATION = "delaysOfUncertainDuration"
    LONG_DELAYS = "longDelays"
    VERY_LONG_DELAYS = "veryLongDelays"
    EXTENDED = "_extended"


class DisturbanceActivityTypeEnum1(Enum):
    """
    Types of disturbance activities.

    :cvar AIR_RAID: A situation relating to any threat from foreign air
        power.
    :cvar ALTERCATION_OF_VEHICLE_OCCUPANTS: An altercation (argument,
        dispute or fight) between two or more vehicle occupants.
    :cvar ASSAULT: A situation where an assault has taken place on one
        or more persons.
    :cvar ASSET_DESTRUCTION: A situation where assets of one or more
        persons or authorities have been destroyed.
    :cvar ATTACK: A situation where an attack on a group of people or
        properties has taken place.
    :cvar ATTACK_ON_VEHICLE: A situation where an attack on a vehicle or
        its occupants has taken place.
    :cvar BLOCKADE_OR_BARRIER: A manned blockade or barrier across a
        road stopping vehicles passing.
    :cvar BOMB_ALERT: An alert to a situation where suspected or actual
        explosive or incendiary devices may cause disruption to traffic.
    :cvar CROWD: A major gathering of people that could disrupt traffic.
    :cvar DEMONSTRATION: A public protest with the potential to disrupt
        traffic.
    :cvar EVACUATION: A situation where a definite area is being cleared
        due to dangerous conditions or for security reasons.
    :cvar FILTER_BLOCKADE: A manned blockade of a road where only
        certain vehicles are allowed through.
    :cvar GO_SLOW_OPERATION: As a form of protest, several vehicles are
        driving in a convoy at a low speed which is affecting the normal
        traffic flow.
    :cvar GUNFIRE_ON_ROADWAY: A situation involving gunfire, perceived
        or actual, on or near the roadway through an act of terrorism or
        crime, which could disrupt traffic.
    :cvar ILL_VEHICLE_OCCUPANTS: One or more occupants of a vehicle are
        seriously ill, possibly requiring specialist services or
        assistance. This may disrupt normal traffic flow.
    :cvar MARCH: A situation where people are walking together in large
        groups for a common purpose, with potential to disrupt traffic.
    :cvar PEOPLE_THROWING_OBJECTS_ON_THE_ROAD: People throwing objects
        on the road
    :cvar PUBLIC_DISTURBANCE: A situation of public disorder, with
        potential to disrupt traffic.
    :cvar RADIOACTIVE_LEAK_ALERT: An alert to a radioactive leak which
        may endanger the public and hence may cause traffic disruption.
    :cvar RIOT: A situation of public disorder involving violent
        behaviour and/or destruction of property with the potential to
        disrupt traffic.
    :cvar SABOTAGE: A situation resulting from any act of sabotage.
    :cvar SECURITY_ALERT: An official alert to a perceived or actual
        threat of crime or terrorism, which could disrupt traffic.
    :cvar SECURITY_INCIDENT: A situation related to a perceived or
        actual threat of crime or terrorism, which could disrupt
        traffic.
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS: Attendees or sightseers to
        reported event(s) causing obstruction to access.
    :cvar STRIKE: A situation resulting from industrial action that
        could disrupt traffic.
    :cvar TERRORIST_INCIDENT: A situation related to a perceived or
        actual threat of terrorism, which could disrupt traffic.
    :cvar THEFT: A situation where assets of one or more persons or
        authorities have been stolen.
    :cvar TOXIC_CLOUD_ALERT: An alert to a toxic release of gases and/or
        particulates into the environment which may endanger the public
        and hence may cause traffic disruption.
    :cvar UNSPECIFIED_ALERT: An alert to a perceived or actual threat of
        an unspecified nature, which could disrupt traffic.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AIR_RAID = "airRaid"
    ALTERCATION_OF_VEHICLE_OCCUPANTS = "altercationOfVehicleOccupants"
    ASSAULT = "assault"
    ASSET_DESTRUCTION = "assetDestruction"
    ATTACK = "attack"
    ATTACK_ON_VEHICLE = "attackOnVehicle"
    BLOCKADE_OR_BARRIER = "blockadeOrBarrier"
    BOMB_ALERT = "bombAlert"
    CROWD = "crowd"
    DEMONSTRATION = "demonstration"
    EVACUATION = "evacuation"
    FILTER_BLOCKADE = "filterBlockade"
    GO_SLOW_OPERATION = "goSlowOperation"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    MARCH = "march"
    PEOPLE_THROWING_OBJECTS_ON_THE_ROAD = "peopleThrowingObjectsOnTheRoad"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    RADIOACTIVE_LEAK_ALERT = "radioactiveLeakAlert"
    RIOT = "riot"
    SABOTAGE = "sabotage"
    SECURITY_ALERT = "securityAlert"
    SECURITY_INCIDENT = "securityIncident"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    STRIKE = "strike"
    TERRORIST_INCIDENT = "terroristIncident"
    THEFT = "theft"
    TOXIC_CLOUD_ALERT = "toxicCloudAlert"
    UNSPECIFIED_ALERT = "unspecifiedAlert"
    OTHER = "other"
    EXTENDED = "_extended"


class DrivingConditionTypeEnum1(Enum):
    """
    Types of the perceived driving conditions.

    :cvar IMPOSSIBLE: Current conditions are making driving impossible.
    :cvar HAZARDOUS: Driving conditions are hazardous due to
        environmental conditions.
    :cvar NORMAL: Driving conditions are normal.
    :cvar PASSABLE_WITH_CARE: The roadway is passable to vehicles with
        driver care.
    :cvar UNKNOWN: Driving conditions are unknown.
    :cvar VERY_HAZARDOUS: Driving conditions are very hazardous due to
        environmental conditions.
    :cvar WINTER_CONDITIONS: Driving conditions are consistent with
        those expected in winter.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"
    EXTENDED = "_extended"


class EnvironmentalObstructionTypeEnum1(Enum):
    """
    Types of environmental obstructions.

    :cvar AVALANCHES: The road may be obstructed or partially obstructed
        due to snow slides.
    :cvar EARTHQUAKE_DAMAGE: The road may be obstructed or partially
        obstructed because of damage caused by an earthquake.
    :cvar FALLEN_TREES: The road is obstructed or partially obstructed
        by one or more fallen trees.
    :cvar FALLING_ICE: Falling ice off trees, power lines or structures
        which may cause traffic disruption.
    :cvar FALLING_LIGHT_ICE_OR_SNOW: Falling light ice or snow off
        trees, power lines or structures which may cause traffic
        disruption.
    :cvar FLASH_FLOODS: The road may become quickly inundated by
        powerful floodwaters due to heavy rain nearby.
    :cvar FLOODING: The road is obstructed or partially obstructed by
        flood water.
    :cvar FOREST_FIRE: Traffic may be disrupted due to a forest fire
        adjacent to the roadway.
    :cvar GRASS_FIRE: Traffic may be disrupted due to a grass fire
        adjacent to the roadway.
    :cvar LANDSLIPS: The road may be obstructed or partially obstructed
        due to landslides.
    :cvar MUD_SLIDE: The road may be obstructed or partially obstructed
        due to mudslides.
    :cvar SEWER_OVERFLOW: The road is obstructed or partially obstructed
        by overflows from one or more sewers.
    :cvar ROCKFALLS: The road may be obstructed or partially obstructed
        due to fallen rocks.
    :cvar SERIOUS_FIRE: Traffic may be disrupted due to a fire (other
        than a vehicle fire) adjacent to the roadway.
    :cvar SMOKE_OR_FUMES: Smoke or fumes which may hinder driving
        conditions or distract drivers.
    :cvar STORM_DAMAGE: The road may be obstructed or partially
        obstructed by debris caused by strong winds.
    :cvar SUBSIDENCE: The road surface has sunken or collapsed in
        places.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AVALANCHES = "avalanches"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    FALLEN_TREES = "fallenTrees"
    FALLING_ICE = "fallingIce"
    FALLING_LIGHT_ICE_OR_SNOW = "fallingLightIceOrSnow"
    FLASH_FLOODS = "flashFloods"
    FLOODING = "flooding"
    FOREST_FIRE = "forestFire"
    GRASS_FIRE = "grassFire"
    LANDSLIPS = "landslips"
    MUD_SLIDE = "mudSlide"
    SEWER_OVERFLOW = "sewerOverflow"
    ROCKFALLS = "rockfalls"
    SERIOUS_FIRE = "seriousFire"
    SMOKE_OR_FUMES = "smokeOrFumes"
    STORM_DAMAGE = "stormDamage"
    SUBSIDENCE = "subsidence"
    OTHER = "other"
    EXTENDED = "_extended"


class EquipmentOrSystemFaultTypeEnum1(Enum):
    """
    Types of fault, malfunctioning or non operational conditions of equipment
    or systems.

    :cvar NOT_WORKING: Not working or functioning.
    :cvar OUT_OF_SERVICE: Out of service (usually for operational
        reasons).
    :cvar WORKING_INCORRECTLY: Working incorrectly.
    :cvar WORKING_INTERMITTENTLY: Working intermittently.
    :cvar EXTENDED:
    """
    NOT_WORKING = "notWorking"
    OUT_OF_SERVICE = "outOfService"
    WORKING_INCORRECTLY = "workingIncorrectly"
    WORKING_INTERMITTENTLY = "workingIntermittently"
    EXTENDED = "_extended"


class EquipmentOrSystemTypeEnum1(Enum):
    """
    Types of equipment and systems used to support the operation of the road
    network.

    :cvar ANPR_CAMERAS: Automatic number plate recognition cameras.
    :cvar AUTOMATED_TOLL_SYSTEM: Automated toll system.
    :cvar CCTV_CAMERAS: Closed-circuit television cameras.
    :cvar EMERGENCY_ROADSIDE_TELEPHONES: Emergency roadside telephones.
    :cvar FIRE_DETECTION_EQUIPMENT: Fire detection equipment
    :cvar GALLERY_LIGHTS: Gallery lights.
    :cvar LANE_CONTROL_SIGNS: Signs used to control lane usage (e.g. in
        tidal flow systems or hard shoulder running).
    :cvar LEVEL_CROSSING: Level crossing (barriers and signals).
    :cvar MATRIX_SIGNS: Matrix signs. These normally comprise a symbol
        display area surrounded by four lights (usually amber) which
        flash when a symbol is displayed.
    :cvar RAMP_CONTROLS: Ramp control equipment.
    :cvar ROADSIDE_COMMUNICATIONS_SYSTEM: Roadside communications system
        which is used by one or more roadside equipments or systems.
    :cvar ROADSIDE_POWER_SYSTEM: Roadside power system which is used by
        one or more roadside equipments or systems.
    :cvar SPEED_CONTROL_SIGNS: Signs used to control traffic speed.
    :cvar STREET_LIGHTING: Street or road lighting.
    :cvar TEMPORARY_TRAFFIC_LIGHTS: Temporary traffic lights.
    :cvar TOLL_GATES: Toll gates.
    :cvar TRAFFIC_LIGHT_SETS: Sets of traffic lights.
    :cvar TRAFFIC_SIGNALS: Traffic signals.
    :cvar TUNNEL_EMERGENCY_PHONES: Tunnel emergency telephones
    :cvar TUNNEL_FIRE_FIGHTING_EQUIPMENT: Tunnel fire fighting equipment
    :cvar TUNNEL_LIGHTS: Tunnel lights.
    :cvar TUNNEL_MOBILE_COMMUNICATION: Tunnel mobile coverage
        communication equipment
    :cvar TUNNEL_RADIO_COMMUNICATION: Tunnel radio communication
        equipment
    :cvar TUNNEL_SAFETY_SYSTEM: Any tunnel safety system
    :cvar TUNNEL_VENTILATION: Tunnel ventilation system.
    :cvar VARIABLE_MESSAGE_SIGNS: Variable message signs.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ANPR_CAMERAS = "anprCameras"
    AUTOMATED_TOLL_SYSTEM = "automatedTollSystem"
    CCTV_CAMERAS = "cctvCameras"
    EMERGENCY_ROADSIDE_TELEPHONES = "emergencyRoadsideTelephones"
    FIRE_DETECTION_EQUIPMENT = "fireDetectionEquipment"
    GALLERY_LIGHTS = "galleryLights"
    LANE_CONTROL_SIGNS = "laneControlSigns"
    LEVEL_CROSSING = "levelCrossing"
    MATRIX_SIGNS = "matrixSigns"
    RAMP_CONTROLS = "rampControls"
    ROADSIDE_COMMUNICATIONS_SYSTEM = "roadsideCommunicationsSystem"
    ROADSIDE_POWER_SYSTEM = "roadsidePowerSystem"
    SPEED_CONTROL_SIGNS = "speedControlSigns"
    STREET_LIGHTING = "streetLighting"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES = "tollGates"
    TRAFFIC_LIGHT_SETS = "trafficLightSets"
    TRAFFIC_SIGNALS = "trafficSignals"
    TUNNEL_EMERGENCY_PHONES = "tunnelEmergencyPhones"
    TUNNEL_FIRE_FIGHTING_EQUIPMENT = "tunnelFireFightingEquipment"
    TUNNEL_LIGHTS = "tunnelLights"
    TUNNEL_MOBILE_COMMUNICATION = "tunnelMobileCommunication"
    TUNNEL_RADIO_COMMUNICATION = "tunnelRadioCommunication"
    TUNNEL_SAFETY_SYSTEM = "tunnelSafetySystem"
    TUNNEL_VENTILATION = "tunnelVentilation"
    VARIABLE_MESSAGE_SIGNS = "variableMessageSigns"
    OTHER = "other"
    EXTENDED = "_extended"


class GeneralInstructionToRoadUsersTypeEnum1(Enum):
    """
    General instructions that may be issued to road users (specifically drivers
    and sometimes passengers) by an operator or operational system in support
    of network management activities or emergency situations.

    :cvar ALLOW_EMERGENCY_VEHICLES_TO_PASS: Allow emergency vehicles to
        pass.
    :cvar APPROACH_WITH_CARE: Approach with care.
    :cvar AVOID_THE_AREA: Drivers are to avoid the area.
    :cvar CLOSE_ALL_WINDOWS_TURN_OFF_HEATER_AND_VENTS: Close all windows
        and turn off heater and vents.
    :cvar CROSS_JUNCTION_WITH_CARE: Cross junction with care.
    :cvar DO_NOT_ALLOW_UNNECESSARY_GAPS: Do not allow unnecessary gaps.
    :cvar DO_NOT_LEAVE_YOUR_VEHICLE: Do not leave your vehicle.
    :cvar DO_NOT_THROW_OUT_ANY_BURNING_OBJECTS: Do not throw out any
        burning objects.
    :cvar DO_NOT_USE_NAVIGATION_SYSTEMS: Do not use navigation systems
        to determine routing.
    :cvar DRIVE_CAREFULLY: Drive carefully.
    :cvar DRIVE_WITH_EXTREME_CAUTION: Drive with extreme caution.
    :cvar FLASH_YOUR_LIGHTS: Flash your lights to warn oncoming traffic
        of hazard ahead.
    :cvar FOLLOW_THE_VEHICLE_IN_FRONT_SMOOTHLY: Follow the vehicle in
        front, smoothly.
    :cvar INCREASE_NORMAL_FOLLOWING_DISTANCE: Increase normal following
        distance.
    :cvar IN_EMERGENCY_WAIT_FOR_PATROL_SERVICE: In emergency, wait for
        patrol service (either road operator or police patrol service).
    :cvar KEEP_YOUR_DISTANCE: Keep your distance.
    :cvar LEAVE_YOUR_VEHICLE_PROCEED_TO_NEXT_SAFE_PLACE: Leave your
        vehicle and proceed to next safe place.
    :cvar NO_NAKED_FLAMES: No naked flames.
    :cvar NO_OVERTAKING: No overtaking on the specified section of road.
    :cvar NO_SMOKING: No smoking.
    :cvar NO_STOPPING: No stopping.
    :cvar NO_UTURNS: No U-turns.
    :cvar OBSERVE_AMBER_ALERT: Observe current amber alert (an emergency
        alert issued for a missing or abducted child).
    :cvar OBSERVE_SIGNALS: Observe signals.
    :cvar OBSERVE_SIGNS: Observe signs.
    :cvar ONLY_TRAVEL_IF_ABSOLUTELY_NECESSARY: Only travel if absolutely
        necessary.
    :cvar OVERTAKE_WITH_CARE: Overtake with care.
    :cvar PULL_OVER_TO_THE_EDGE_OF_THE_ROADWAY: Pull over to the edge of
        the roadway.
    :cvar STOP_AT_NEXT_SAFE_PLACE: Stop at next safe place.
    :cvar STOP_AT_NEXT_SERVICE_AREA: Stop at next rest service area or
        car park.
    :cvar SWITCH_OFF_ENGINE: Switch off engine.
    :cvar SWITCH_OFF_MOBILE_PHONES_AND_TWO_WAY_RADIOS: Switch off mobile
        phones and two-way radios.
    :cvar TEST_YOUR_BRAKES: Test your brakes.
    :cvar USE_BUS_SERVICE: Use bus service.
    :cvar USE_FOG_LIGHTS: Use fog lights.
    :cvar USE_HAZARD_WARNING_LIGHTS: Use hazard warning lights.
    :cvar USE_HEADLIGHTS: Use headlights.
    :cvar USE_RAIL_SERVICE: Use rail service.
    :cvar USE_TRAM_SERVICE: Use tram service.
    :cvar USE_UNDERGROUND_SERVICE: Use underground service.
    :cvar WAIT_FOR_ESCORT_VEHICLE: Wait for escort vehicle.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ALLOW_EMERGENCY_VEHICLES_TO_PASS = "allowEmergencyVehiclesToPass"
    APPROACH_WITH_CARE = "approachWithCare"
    AVOID_THE_AREA = "avoidTheArea"
    CLOSE_ALL_WINDOWS_TURN_OFF_HEATER_AND_VENTS = "closeAllWindowsTurnOffHeaterAndVents"
    CROSS_JUNCTION_WITH_CARE = "crossJunctionWithCare"
    DO_NOT_ALLOW_UNNECESSARY_GAPS = "doNotAllowUnnecessaryGaps"
    DO_NOT_LEAVE_YOUR_VEHICLE = "doNotLeaveYourVehicle"
    DO_NOT_THROW_OUT_ANY_BURNING_OBJECTS = "doNotThrowOutAnyBurningObjects"
    DO_NOT_USE_NAVIGATION_SYSTEMS = "doNotUseNavigationSystems"
    DRIVE_CAREFULLY = "driveCarefully"
    DRIVE_WITH_EXTREME_CAUTION = "driveWithExtremeCaution"
    FLASH_YOUR_LIGHTS = "flashYourLights"
    FOLLOW_THE_VEHICLE_IN_FRONT_SMOOTHLY = "followTheVehicleInFrontSmoothly"
    INCREASE_NORMAL_FOLLOWING_DISTANCE = "increaseNormalFollowingDistance"
    IN_EMERGENCY_WAIT_FOR_PATROL_SERVICE = "inEmergencyWaitForPatrolService"
    KEEP_YOUR_DISTANCE = "keepYourDistance"
    LEAVE_YOUR_VEHICLE_PROCEED_TO_NEXT_SAFE_PLACE = "leaveYourVehicleProceedToNextSafePlace"
    NO_NAKED_FLAMES = "noNakedFlames"
    NO_OVERTAKING = "noOvertaking"
    NO_SMOKING = "noSmoking"
    NO_STOPPING = "noStopping"
    NO_UTURNS = "noUturns"
    OBSERVE_AMBER_ALERT = "observeAmberAlert"
    OBSERVE_SIGNALS = "observeSignals"
    OBSERVE_SIGNS = "observeSigns"
    ONLY_TRAVEL_IF_ABSOLUTELY_NECESSARY = "onlyTravelIfAbsolutelyNecessary"
    OVERTAKE_WITH_CARE = "overtakeWithCare"
    PULL_OVER_TO_THE_EDGE_OF_THE_ROADWAY = "pullOverToTheEdgeOfTheRoadway"
    STOP_AT_NEXT_SAFE_PLACE = "stopAtNextSafePlace"
    STOP_AT_NEXT_SERVICE_AREA = "stopAtNextServiceArea"
    SWITCH_OFF_ENGINE = "switchOffEngine"
    SWITCH_OFF_MOBILE_PHONES_AND_TWO_WAY_RADIOS = "switchOffMobilePhonesAndTwoWayRadios"
    TEST_YOUR_BRAKES = "testYourBrakes"
    USE_BUS_SERVICE = "useBusService"
    USE_FOG_LIGHTS = "useFogLights"
    USE_HAZARD_WARNING_LIGHTS = "useHazardWarningLights"
    USE_HEADLIGHTS = "useHeadlights"
    USE_RAIL_SERVICE = "useRailService"
    USE_TRAM_SERVICE = "useTramService"
    USE_UNDERGROUND_SERVICE = "useUndergroundService"
    WAIT_FOR_ESCORT_VEHICLE = "waitForEscortVehicle"
    OTHER = "other"
    EXTENDED = "_extended"


class GeneralNetworkManagementTypeEnum1(Enum):
    """
    Types of network management actions.

    :cvar BRIDGE_SWING_IN_OPERATION: The bridge at the specified
        location has swung or lifted and is therefore temporarily closed
        to traffic.
    :cvar CONVOY_SERVICE: A vehicle convoy service is in operation, for
        example with a snowplough running ahead due to bad weather
        conditions.
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
    :cvar EXTENDED:
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
    EXTENDED = "_extended"


class InfrastructureDamageTypeEnum1(Enum):
    """
    Types of infrastructure damage which may have an effect on the road
    network.

    :cvar BURST_PIPE: The road surface has sunken or collapsed in places
        due to burst pipes.
    :cvar BURST_WATER_MAIN: Traffic may be disrupted due to local
        flooding and/or subsidence because of a broken water main.
    :cvar COLLAPSED_SEWER: The road surface has sunken or collapsed in
        places due to sewer failure.
    :cvar DAMAGED_BRIDGE: Damage to a bridge that may cause traffic
        disruption.
    :cvar DAMAGED_CRASH_BARRIER: Damage to a crash barrier that may
        cause traffic disruption.
    :cvar DAMAGED_FLYOVER: Damage to an elevated section of the
        carriageway over another carriageway that may cause traffic
        disruption.
    :cvar DAMAGED_GALLERY: Damage to a gallery that may cause traffic
        disruption.
    :cvar DAMAGED_GANTRY: Damage to a gantry above the roadway that may
        cause traffic disruption.
    :cvar DAMAGED_ROAD_SURFACE: Damage to the road surface that may
        cause traffic disruption.
    :cvar DAMAGED_TUNNEL: Damage to a tunnel that may cause traffic
        disruption.
    :cvar DAMAGED_VIADUCT: Damage to a viaduct that may cause traffic
        disruption.
    :cvar FALLEN_POWER_CABLES: The road is obstructed or partially
        obstructed by one or more fallen power cables.
    :cvar GAS_LEAK: Traffic may be disrupted due to an explosion hazard
        from gas escaping in or near the roadway.
    :cvar WEAK_BRIDGE: Weak bridge capable of carrying a reduced load,
        typically with a reduced weight limit restriction imposed.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    BURST_PIPE = "burstPipe"
    BURST_WATER_MAIN = "burstWaterMain"
    COLLAPSED_SEWER = "collapsedSewer"
    DAMAGED_BRIDGE = "damagedBridge"
    DAMAGED_CRASH_BARRIER = "damagedCrashBarrier"
    DAMAGED_FLYOVER = "damagedFlyover"
    DAMAGED_GALLERY = "damagedGallery"
    DAMAGED_GANTRY = "damagedGantry"
    DAMAGED_ROAD_SURFACE = "damagedRoadSurface"
    DAMAGED_TUNNEL = "damagedTunnel"
    DAMAGED_VIADUCT = "damagedViaduct"
    FALLEN_POWER_CABLES = "fallenPowerCables"
    GAS_LEAK = "gasLeak"
    WEAK_BRIDGE = "weakBridge"
    OTHER = "other"
    EXTENDED = "_extended"


class InjuryStatusTypeEnum1(Enum):
    """
    Types of injury status of people.

    :cvar DEAD: Dead.
    :cvar INJURED: Injured requiring medical treatment.
    :cvar SERIOUSLY_INJURED: Seriously injured requiring urgent hospital
        treatment.
    :cvar SLIGHTLY_INJURED: Slightly injured requiring medical
        treatment.
    :cvar UNINJURED: Uninjured.
    :cvar UNKNOWN: Injury status unknown.
    :cvar EXTENDED:
    """
    DEAD = "dead"
    INJURED = "injured"
    SERIOUSLY_INJURED = "seriouslyInjured"
    SLIGHTLY_INJURED = "slightlyInjured"
    UNINJURED = "uninjured"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class InvolvementRolesEnum1(Enum):
    """
    Involvement role of a person in event.

    :cvar CYCLIST: Cyclist.
    :cvar MOTORCYCLIST: Motorcyclist
    :cvar PEDESTRIAN: Pedestrian.
    :cvar UNKNOWN: Involvement role is unknown.
    :cvar VEHICLE_DRIVER: Vehicle driver.
    :cvar VEHICLE_OCCUPANT: Vehicle occupant (driver or passenger not
        specified).
    :cvar VEHICLE_PASSENGER: Vehicle passenger.
    :cvar WITNESS: Witness.
    :cvar EXTENDED:
    """
    CYCLIST = "cyclist"
    MOTORCYCLIST = "motorcyclist"
    PEDESTRIAN = "pedestrian"
    UNKNOWN = "unknown"
    VEHICLE_DRIVER = "vehicleDriver"
    VEHICLE_OCCUPANT = "vehicleOccupant"
    VEHICLE_PASSENGER = "vehiclePassenger"
    WITNESS = "witness"
    EXTENDED = "_extended"


class MaintenanceVehicleActionsEnum1(Enum):
    """
    Types of maintenance vehicle actions associated with roadworks.

    :cvar MAINTENANCE_ACTION: Maintenance vehicles are performing
        maintenance action
    :cvar MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW: Maintenance
        vehicles are merging into the traffic flow creating a potential
        hazard for road users.
    :cvar SLOW_MOVING: Maintenance vehicles are slow moving.
    :cvar STOPPING_TO_SERVICE_EQUIPMENTS: Maintenance vehicles are
        stopping to service equipments on or next to the roadway.
    :cvar EXTENDED:
    """
    MAINTENANCE_ACTION = "maintenanceAction"
    MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW = "maintenanceVehiclesMergingIntoTrafficFlow"
    SLOW_MOVING = "slowMoving"
    STOPPING_TO_SERVICE_EQUIPMENTS = "stoppingToServiceEquipments"
    EXTENDED = "_extended"


class MobilityTypeEnum1(Enum):
    """
    Types of mobility relating to a situation element defined by a
    SituationReord.

    :cvar MOBILE: The described element of a situation is moving.
    :cvar STATIONARY: The described element of a situation is
        stationary.
    :cvar UNKNOWN: The mobility of the described element of a situation
        is unknown.
    :cvar EXTENDED:
    """
    MOBILE = "mobile"
    STATIONARY = "stationary"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class NonWeatherRelatedRoadConditionTypeEnum1(Enum):
    """
    Types of road surface conditions which are not related to the weather.

    :cvar DIESEL_ON_ROAD: Increased skid risk due to diesel on the road.
    :cvar LEAVES_ON_ROAD: Increased skid risk due to leaves on road.
    :cvar LOOSE_CHIPPINGS: Increased skid risk and injury risk due to
        loose chippings on road.
    :cvar LOOSE_SAND_ON_ROAD: Increased skid risk due to loose sand on
        road.
    :cvar MUD_ON_ROAD: Increased skid risk due to mud on road.
    :cvar OIL_ON_ROAD: Increased skid risk due to oil on road.
    :cvar PETROL_ON_ROAD: Increased skid risk due to petrol on road.
    :cvar ROAD_MARKING_NOT_PRESENT: Road markings are not present due to
        maintenance works in progress
    :cvar ROAD_SURFACE_IN_POOR_CONDITION: The road surface is damaged,
        severely rutted or potholed (i.e. it is in a poor state of
        repair).
    :cvar SLIPPERY_ROAD: The road surface is slippery due to an
        unspecified non-weather related cause.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    DIESEL_ON_ROAD = "dieselOnRoad"
    LEAVES_ON_ROAD = "leavesOnRoad"
    LOOSE_CHIPPINGS = "looseChippings"
    LOOSE_SAND_ON_ROAD = "looseSandOnRoad"
    MUD_ON_ROAD = "mudOnRoad"
    OIL_ON_ROAD = "oilOnRoad"
    PETROL_ON_ROAD = "petrolOnRoad"
    ROAD_MARKING_NOT_PRESENT = "roadMarkingNotPresent"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"
    EXTENDED = "_extended"


class ObstructionTypeEnum1(Enum):
    """
    Types of obstructions on the roadway.

    :cvar AIR_CRASH: An air crash adjacent to the roadway which may
        cause traffic disruption.
    :cvar CHILDREN_ON_ROADWAY: Children on the roadway which may cause
        traffic disruption.
    :cvar CLEARANCE_WORK: Clearance work associated with an earlier
        traffic problem which may cause traffic disruption.
    :cvar CRANE_OPERATING: A crane is operating either on or adjacent to
        the road which may cause an obstruction to traffic.
    :cvar CYCLISTS_ON_ROADWAY: Cyclists on the roadway which may cause
        traffic disruption.
    :cvar DEBRIS: Scattered fragments of wreckage or other material on
        the road.
    :cvar EXPLOSION: A situation where an explosive or incendiary device
        has gone off.
    :cvar EXPLOSION_HAZARD: A situation where there is danger of an
        explosion which may cause disruption to traffic.
    :cvar HAZARDS_ON_THE_ROAD: Unspecified hazard(s) on the road which
        may cause traffic disruption.
    :cvar INCIDENT: Incidents are chance occurrences involving vehicles
        from the traffic stream, which could present potential hazards
        to road users.  This item excludes accidents.
    :cvar INDUSTRIAL_ACCIDENT: Industrial accident near the roadway
        which may cause traffic disruption.
    :cvar OBJECT_ON_THE_ROAD: The road may be obstructed or traffic
        hindered due to objects laying on the roadway.
    :cvar OBJECTS_FALLING_FROM_MOVING_VEHICLE: Objects falling from
        moving vehicles which are presenting a hazard to other vehicles.
    :cvar OBSTRUCTION_ON_THE_ROAD: Unspecified obstruction on the
        roadway which may cause traffic disruption.
    :cvar PEOPLE_ON_ROADWAY: People on the roadway which may cause
        traffic disruption.
    :cvar RAIL_CRASH: A rail crash adjacent to the roadway which may
        cause traffic disruption.
    :cvar RESCUE_AND_RECOVERY_WORK: Work is being undertaken by
        emergency services which may present a hazard to road users.
    :cvar SEVERE_FROST_DAMAGED_ROADWAY: Severe frost damage to the
        roadway causing an obstruction to traffic.
    :cvar SHED_LOAD: Spillage of transported goods on the roadway which
        may cause traffic disruption.
    :cvar SNOW_AND_ICE_DEBRIS: Snow and ice debris on the roadway which
        may present a hazard to road users.
    :cvar SPILLAGE_OCCURRING_FROM_MOVING_VEHICLE: Substances are
        spilling out from a moving vehicle which is presenting a hazard
        to other road users.
    :cvar SPILLAGE_ON_THE_ROAD: Includes all situations where a spillage
        has occurred on the roadway due to an earlier incident.
    :cvar UNPROTECTED_ACCIDENT_AREA: An accident area which has not been
        protected and may present a hazard to road users.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AIR_CRASH = "airCrash"
    CHILDREN_ON_ROADWAY = "childrenOnRoadway"
    CLEARANCE_WORK = "clearanceWork"
    CRANE_OPERATING = "craneOperating"
    CYCLISTS_ON_ROADWAY = "cyclistsOnRoadway"
    DEBRIS = "debris"
    EXPLOSION = "explosion"
    EXPLOSION_HAZARD = "explosionHazard"
    HAZARDS_ON_THE_ROAD = "hazardsOnTheRoad"
    INCIDENT = "incident"
    INDUSTRIAL_ACCIDENT = "industrialAccident"
    OBJECT_ON_THE_ROAD = "objectOnTheRoad"
    OBJECTS_FALLING_FROM_MOVING_VEHICLE = "objectsFallingFromMovingVehicle"
    OBSTRUCTION_ON_THE_ROAD = "obstructionOnTheRoad"
    PEOPLE_ON_ROADWAY = "peopleOnRoadway"
    RAIL_CRASH = "railCrash"
    RESCUE_AND_RECOVERY_WORK = "rescueAndRecoveryWork"
    SEVERE_FROST_DAMAGED_ROADWAY = "severeFrostDamagedRoadway"
    SHED_LOAD = "shedLoad"
    SNOW_AND_ICE_DEBRIS = "snowAndIceDebris"
    SPILLAGE_OCCURRING_FROM_MOVING_VEHICLE = "spillageOccurringFromMovingVehicle"
    SPILLAGE_ON_THE_ROAD = "spillageOnTheRoad"
    UNPROTECTED_ACCIDENT_AREA = "unprotectedAccidentArea"
    OTHER = "other"
    EXTENDED = "_extended"


class OperatorActionOriginEnum1(Enum):
    """
    Origins of operator actions.

    :cvar EXTERNAL: Operator action originated externally to the
        authority which is taking the action.
    :cvar INTERNAL: Operator action originated within the authority
        which is taking the action.
    :cvar EXTENDED:
    """
    EXTERNAL = "external"
    INTERNAL = "internal"
    EXTENDED = "_extended"


class OperatorActionStatusEnum1(Enum):
    """
    List of statuses associated with operator actions.

    :cvar REQUESTED: A request, either internal or external, has been
        received to implement an action. It has neither been approved
        nor has any activity yet been undertaken to implement the
        action.
    :cvar APPROVED: The action has been approved by the recipient of the
        request but activity to implement the action has not yet
        commenced.
    :cvar BEING_IMPLEMENTED: The action is in the process of being
        implemented.
    :cvar IMPLEMENTED: The action is fully implemented.
    :cvar REJECTED: The action has been rejected by the recipient of the
        request and hence is not implemented.
    :cvar TERMINATION_REQUESTED: A request, either internal or external,
        has been received to terminate the action, but activity to
        terminate the action has not yet commenced.
    :cvar BEING_TERMINATED: The action is in the process of being
        terminated either because the action has reached the end of its
        validity period or because new circumstances have arisen and its
        termination has been requested, e.g. because of a traffic jam on
        the alternative route.
    :cvar EXTENDED:
    """
    REQUESTED = "requested"
    APPROVED = "approved"
    BEING_IMPLEMENTED = "beingImplemented"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"
    TERMINATION_REQUESTED = "terminationRequested"
    BEING_TERMINATED = "beingTerminated"
    EXTENDED = "_extended"


class PersonCategoryEnum1(Enum):
    """
    Categories of person.

    :cvar ADULT: Adult.
    :cvar CHILD: Child (age 4 to 17).
    :cvar EMERGENCY_SERVICES_PERSON: A member of the emergency services,
        other than the police.
    :cvar FIREMAN: A member of the fire service.
    :cvar INFANT: Infant (age 0 to 3).
    :cvar MEDICAL_STAFF: A member of the medical service.
    :cvar MEMBER_OF_THE_PUBLIC: A member of the general public.
    :cvar POLICEMAN: A member of the police force.
    :cvar POLITICIAN: A politician.
    :cvar PUBLIC_TRANSPORT_PASSENGER: A passenger on or from a public
        transport vehicle.
    :cvar SICK_PERSON: A sick person.
    :cvar TRAFFIC_OFFICER: A traffic patrol officer of the road
        authority.
    :cvar TRAFFIC_WARDEN: A member of the local traffic warden service.
    :cvar VERY_IMPORTANT_PERSON: A very important person.
    :cvar EXTENDED:
    """
    ADULT = "adult"
    CHILD = "child"
    EMERGENCY_SERVICES_PERSON = "emergencyServicesPerson"
    FIREMAN = "fireman"
    INFANT = "infant"
    MEDICAL_STAFF = "medicalStaff"
    MEMBER_OF_THE_PUBLIC = "memberOfThePublic"
    POLICEMAN = "policeman"
    POLITICIAN = "politician"
    PUBLIC_TRANSPORT_PASSENGER = "publicTransportPassenger"
    SICK_PERSON = "sickPerson"
    TRAFFIC_OFFICER = "trafficOfficer"
    TRAFFIC_WARDEN = "trafficWarden"
    VERY_IMPORTANT_PERSON = "veryImportantPerson"
    EXTENDED = "_extended"


class PlacesEnum1(Enum):
    """
    List of types of places.

    :cvar AROUND_BENDS_IN_THE_ROAD: Around bends in the road.
    :cvar AT_CUSTOMS_POSTS: At customs posts.
    :cvar AT_HIGH_ALTITUDES: At high altitudes.
    :cvar AT_REST_AREAS: At rest areas
    :cvar AT_SERVICE_AREAS: At service areas
    :cvar AT_TOLL_PLAZAS: At toll plazas.
    :cvar IN_BUILT_UP_AREAS: In built up areas, i.e. villages, towns and
        cities.
    :cvar IN_CONTRAFLOW_SECTIONS: In sections of the road where
        contraflow is in operation.
    :cvar IN_FORESTED_AREAS: On sections of the road where it runs
        through or adjacent to forested areas.
    :cvar IN_GALLERIES: In galleries.
    :cvar IN_LOW_LYING_AREAS: In low lying areas.
    :cvar IN_ROADWORKS_AREAS: In roadworks areas.
    :cvar IN_RURAL_AREAS: In rural areas, i.e. outside villages, towns
        and cities.
    :cvar IN_SHADED_AREAS: In shaded areas.
    :cvar IN_THE_INNER_CITY_AREAS: In the inner city areas.
    :cvar IN_THE_CITY_CENTRE: In the city centre.
    :cvar IN_TUNNELS: In tunnels.
    :cvar ON_BRIDGES: On bridges.
    :cvar ON_DOWN_HILL_SECTIONS: On down hill sections of the road.
    :cvar ON_DUAL_CARRIAGEWAY_SECTIONS: On dual carriageway sections of
        the road.
    :cvar ON_ELEVATED_SECTIONS: On elevated sections of the road.
    :cvar ON_ENTERING_OR_LEAVING_TUNNELS: On entering or leaving
        tunnels.
    :cvar ON_ENTERING_THE_COUNTRY: On entry into the country.
    :cvar ON_FLYOVERS: On flyover sections of the road, i.e. sections of
        the road which pass over another road.
    :cvar ON_LEAVING_THE_COUNTRY: On leaving the country.
    :cvar ON_MOTORWAYS: On motorways.
    :cvar ON_NON_MOTORWAYS: On non motorways.
    :cvar ON_PASSES: On mountain passes.
    :cvar ON_ROUNDABOUTS: On roundabouts.
    :cvar ON_SINGLE_CARRIAGEWAY_SECTIONS: On single carriageway sections
        of the road.
    :cvar ON_SLIP_ROADS: On slip roads.
    :cvar ON_UNDERGROUND_SECTIONS: On underground sections of the road.
    :cvar ON_UNDERPASSES: On underpasses, i.e. sections of the road
        which pass under another road.
    :cvar ON_UP_HILL_SECTIONS: On hill sections of the road.
    :cvar OVER_THE_CREST_OF_HILLS: Over the crest of hills.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AROUND_BENDS_IN_THE_ROAD = "aroundBendsInTheRoad"
    AT_CUSTOMS_POSTS = "atCustomsPosts"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    AT_REST_AREAS = "atRestAreas"
    AT_SERVICE_AREAS = "atServiceAreas"
    AT_TOLL_PLAZAS = "atTollPlazas"
    IN_BUILT_UP_AREAS = "inBuiltUpAreas"
    IN_CONTRAFLOW_SECTIONS = "inContraflowSections"
    IN_FORESTED_AREAS = "inForestedAreas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_ROADWORKS_AREAS = "inRoadworksAreas"
    IN_RURAL_AREAS = "inRuralAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
    IN_THE_CITY_CENTRE = "inTheCityCentre"
    IN_TUNNELS = "inTunnels"
    ON_BRIDGES = "onBridges"
    ON_DOWN_HILL_SECTIONS = "onDownHillSections"
    ON_DUAL_CARRIAGEWAY_SECTIONS = "onDualCarriagewaySections"
    ON_ELEVATED_SECTIONS = "onElevatedSections"
    ON_ENTERING_OR_LEAVING_TUNNELS = "onEnteringOrLeavingTunnels"
    ON_ENTERING_THE_COUNTRY = "onEnteringTheCountry"
    ON_FLYOVERS = "onFlyovers"
    ON_LEAVING_THE_COUNTRY = "onLeavingTheCountry"
    ON_MOTORWAYS = "onMotorways"
    ON_NON_MOTORWAYS = "onNonMotorways"
    ON_PASSES = "onPasses"
    ON_ROUNDABOUTS = "onRoundabouts"
    ON_SINGLE_CARRIAGEWAY_SECTIONS = "onSingleCarriagewaySections"
    ON_SLIP_ROADS = "onSlipRoads"
    ON_UNDERGROUND_SECTIONS = "onUndergroundSections"
    ON_UNDERPASSES = "onUnderpasses"
    ON_UP_HILL_SECTIONS = "onUpHillSections"
    OVER_THE_CREST_OF_HILLS = "overTheCrestOfHills"
    OTHER = "other"
    EXTENDED = "_extended"


class PoorEnvironmentTypeEnum1(Enum):
    """
    Types of poor environmental conditions.

    :cvar BAD_WEATHER: Adverse weather conditions are affecting driving
        conditions.
    :cvar BLIZZARD: Heavy snowfall in combination with strong winds,
        limiting visibility to 50m or less.
    :cvar BLOWING_DUST: Dust blowing across the roadway causing
        significantly reduced visibility.
    :cvar BLOWING_SNOW: Fallen snow moving due to the forces of wind.
    :cvar CROSSWINDS: Strong cross winds across the direction of the
        roadway (e.g. on a ridge or bridge).
    :cvar DAMAGING_HAIL: Large falling ice pellets or frozen rain
        capable of causing injury or damage to property.
    :cvar DENSE_FOG: Dense fog, limiting visibility to 50m or less.
    :cvar ECLIPSE: Eclipse, either partial or full, of the sun causing
        low light levels during normal daylight period.
    :cvar EXTREME_COLD: Abnormally low temperatures.
    :cvar EXTREME_HEAT: Abnormally high expected maximum temperature.
    :cvar FOG: Fog, visibility more than 50m.
    :cvar FREEZING_FOG: Fog, in conjunction with sub-zero air
        temperatures causing possible freezing of road surface.
    :cvar FROST: Frost can be expected.
    :cvar GALES: Winds between 60 km/h and 90 km/h.
    :cvar GUSTY_WINDS: Constantly varying winds, significant at times.
    :cvar HAIL: Falling ice pellets or frozen rain.
    :cvar HEAVY_FROST: A thick coating of frost can be expected.
    :cvar HEAVY_RAIN: Heavy rainfall, limiting visibility to 50m or
        less.
    :cvar HEAVY_SNOWFALL: Dense falling snow, limiting visibility to 50m
        or less.
    :cvar HURRICANE_FORCE_WINDS: Winds over 120 km/h.
    :cvar LOW_SUN_GLARE: Difficult visibility conditions created by low
        elevation sunlight.
    :cvar MODERATE_FOG: Misty conditions impairing vision over 100m.
    :cvar NEARBY_FIRE: Fire near the road affecting driving conditions
        and/or significantly reduced visibility
    :cvar NEARBY_FLOODING: Flooding near the road risking to affect
        driving conditions
    :cvar OZONE_POLLUTION: High concentrations of ozone are present.
    :cvar POLLUTION: Pollution of an unspecified nature.
    :cvar PATCHY_FOG: Fog, in which intermittent areas of dense fog may
        be encountered.
    :cvar PRECIPITATION_IN_THE_AREA: Unspecified precipitation is
        falling on the area.
    :cvar RAIN: Rain, visibility more than 50m.
    :cvar RAIN_CHANGING_TO_SNOW: Falling rain is changing to snow.
    :cvar SAND_STORMS: Sand blowing across the roadway causing
        significantly reduced visibility.
    :cvar SEVERE_EXHAUST_POLLUTION: Pollution from exhaust fumes has
        reached a level sufficient to cause concern.
    :cvar SEVERE_SMOG: Environmental warning of very poor air quality
        resulting from smog.
    :cvar SHOWERS: Light rain or intermittent rain.
    :cvar SLEET: Rain mingled with snow or hail.
    :cvar SMOG_ALERT: Environmental warning of poor air quality
        resulting from smog.
    :cvar SMOKE_HAZARD: Smoke drifting across the roadway causing
        significantly reduced visibility.
    :cvar SNOW_CHANGING_TO_RAIN: Falling snow is changing to rain.
    :cvar SNOWFALL: Falling snow, visibility more than 50m.
    :cvar SPRAY_HAZARD: Reduced visibility resulting from spray created
        by moving vehicles on a wet roadway.
    :cvar STORM_FORCE_WINDS: Winds between 90 km/h and 120 km/h.
    :cvar STRONG_GUSTS_OF_WIND: Constantly varying winds, strong at
        times.
    :cvar STRONG_WINDS: Winds between 40 km/h and 60 km/h.
    :cvar SWARMS_OF_INSECTS: Large numbers of insects which create a
        hazard for road users through reduced visibility.
    :cvar TEMPERATURE_FALLING: The temperature is falling significantly.
    :cvar THUNDERSTORMS: Electrical storms, generally with heavy rain.
    :cvar TORNADOES: Very violent, whirling windstorms affecting narrow
        strips of country.
    :cvar VERY_STRONG_GUSTS_OF_WIND: Constantly varying winds, very
        strong at times.
    :cvar VISIBILITY_REDUCED: Environmental conditions causing reduced
        visibility.
    :cvar WHITE_OUT: Falling snow in blizzard conditions resulting in
        very reduced visibility.
    :cvar WINTER_STORM: Heavy rain, sleet, hail and/or snow in
        combination with strong winds, limiting visibility to 50m or
        less.
    :cvar EXTENDED:
    """
    BAD_WEATHER = "badWeather"
    BLIZZARD = "blizzard"
    BLOWING_DUST = "blowingDust"
    BLOWING_SNOW = "blowingSnow"
    CROSSWINDS = "crosswinds"
    DAMAGING_HAIL = "damagingHail"
    DENSE_FOG = "denseFog"
    ECLIPSE = "eclipse"
    EXTREME_COLD = "extremeCold"
    EXTREME_HEAT = "extremeHeat"
    FOG = "fog"
    FREEZING_FOG = "freezingFog"
    FROST = "frost"
    GALES = "gales"
    GUSTY_WINDS = "gustyWinds"
    HAIL = "hail"
    HEAVY_FROST = "heavyFrost"
    HEAVY_RAIN = "heavyRain"
    HEAVY_SNOWFALL = "heavySnowfall"
    HURRICANE_FORCE_WINDS = "hurricaneForceWinds"
    LOW_SUN_GLARE = "lowSunGlare"
    MODERATE_FOG = "moderateFog"
    NEARBY_FIRE = "nearbyFire"
    NEARBY_FLOODING = "nearbyFlooding"
    OZONE_POLLUTION = "ozonePollution"
    POLLUTION = "pollution"
    PATCHY_FOG = "patchyFog"
    PRECIPITATION_IN_THE_AREA = "precipitationInTheArea"
    RAIN = "rain"
    RAIN_CHANGING_TO_SNOW = "rainChangingToSnow"
    SAND_STORMS = "sandStorms"
    SEVERE_EXHAUST_POLLUTION = "severeExhaustPollution"
    SEVERE_SMOG = "severeSmog"
    SHOWERS = "showers"
    SLEET = "sleet"
    SMOG_ALERT = "smogAlert"
    SMOKE_HAZARD = "smokeHazard"
    SNOW_CHANGING_TO_RAIN = "snowChangingToRain"
    SNOWFALL = "snowfall"
    SPRAY_HAZARD = "sprayHazard"
    STORM_FORCE_WINDS = "stormForceWinds"
    STRONG_GUSTS_OF_WIND = "strongGustsOfWind"
    STRONG_WINDS = "strongWinds"
    SWARMS_OF_INSECTS = "swarmsOfInsects"
    TEMPERATURE_FALLING = "temperatureFalling"
    THUNDERSTORMS = "thunderstorms"
    TORNADOES = "tornadoes"
    VERY_STRONG_GUSTS_OF_WIND = "veryStrongGustsOfWind"
    VISIBILITY_REDUCED = "visibilityReduced"
    WHITE_OUT = "whiteOut"
    WINTER_STORM = "winterStorm"
    EXTENDED = "_extended"


class ProbabilityOfOccurrenceEnum1(Enum):
    """
    Levels of confidence that the sender has in the information, ordered
    {certain, probable, risk of}.

    :cvar CERTAIN: The source is completely certain of the occurrence of
        the situation record version content.
    :cvar PROBABLE: The source has a reasonably high level of confidence
        of the occurrence of the situation record version content.
    :cvar RISK_OF: The source has a moderate level of confidence of the
        occurrence of the situation record version content.
    :cvar EXTENDED:
    """
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"
    EXTENDED = "_extended"


class RelativeTrafficFlowEnum1(Enum):
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
    :cvar EXTENDED:
    """
    TRAFFIC_VERY_MUCH_HEAVIER_THAN_NORMAL = "trafficVeryMuchHeavierThanNormal"
    TRAFFIC_HEAVIER_THAN_NORMAL = "trafficHeavierThanNormal"
    TRAFFIC_FLOW_NORMAL = "trafficFlowNormal"
    TRAFFIC_LIGHTER_THAN_NORMAL = "trafficLighterThanNormal"
    TRAFFIC_VERY_MUCH_LIGHTER_THAN_NORMAL = "trafficVeryMuchLighterThanNormal"
    EXTENDED = "_extended"


class ReroutingManagementTypeEnum1(Enum):
    """
    Management actions relating to rerouting.

    :cvar DO_NOT_FOLLOW_DIVERSION_SIGNS: Do not follow diversion signs.
    :cvar DO_NOT_USE_ENTRY: Rerouted traffic is not to use the specified
        entry onto the identified road to commence the alternative
        route.
    :cvar DO_NOT_USE_EXIT: Rerouted traffic is not to use the specified
        exit from the identified road to commence the alternative route.
    :cvar DO_NOT_USE_INTERSECTION_OR_JUNCTION: Rerouted traffic is not
        to use the specified intersection or junction.
    :cvar FOLLOW_DIVERSION_SIGNS: Rerouted traffic is to follow the
        diversion signs.
    :cvar FOLLOW_LOCAL_DIVERSION: Rerouted traffic is to follow local
        diversion.
    :cvar FOLLOW_SPECIAL_MARKERS: Rerouted traffic is to follow the
        special diversion markers.
    :cvar USE_ENTRY: Rerouted traffic is to use the specified entry onto
        the identified road to commence the alternative route.
    :cvar USE_EXIT: Rerouted traffic is to use the specified exit from
        the identified road to commence the alternative route.
    :cvar USE_INTERSECTION_OR_JUNCTION: Rerouted traffic is to use the
        specified intersection or junction to commence the alternative
        route.
    :cvar EXTENDED:
    """
    DO_NOT_FOLLOW_DIVERSION_SIGNS = "doNotFollowDiversionSigns"
    DO_NOT_USE_ENTRY = "doNotUseEntry"
    DO_NOT_USE_EXIT = "doNotUseExit"
    DO_NOT_USE_INTERSECTION_OR_JUNCTION = "doNotUseIntersectionOrJunction"
    FOLLOW_DIVERSION_SIGNS = "followDiversionSigns"
    FOLLOW_LOCAL_DIVERSION = "followLocalDiversion"
    FOLLOW_SPECIAL_MARKERS = "followSpecialMarkers"
    USE_ENTRY = "useEntry"
    USE_EXIT = "useExit"
    USE_INTERSECTION_OR_JUNCTION = "useIntersectionOrJunction"
    EXTENDED = "_extended"


class RoadMaintenanceTypeEnum1(Enum):
    """
    Types of road maintenance.

    :cvar ACCIDENT_REPAIR_WORK: repairing works after an accident, not
        clearance work but rebuilding of infrastructure
    :cvar CLEARANCE_WORK: Clearance work of an unspecified nature.
    :cvar CONTROLLED_AVALANCHE: Controlled avalanche work.
    :cvar INSTALLATION_WORK: Installation of new equipments or systems
        on or along-side the roadway.
    :cvar GRASS_CUTTING_WORK: Grass cutting work.
    :cvar LITTER_CLEARANCE: Work to collect litter from the roadway
        and/or adjacent verges.
    :cvar MAINTENANCE_WORK: Maintenance of road, associated
        infrastructure or equipments.
    :cvar MAINTENANCE_PEOPLE_ON_ROAD: People on road for general
        maintenance purpose
    :cvar OVERHEAD_WORKS: Works which are overhead of the carriageway.
    :cvar REPAIR_WORK: Repair work to road, associated infrastructure or
        equipments.
    :cvar RESURFACING_WORK: Work associated with relaying or renewal of
        worn-out road surface (pavement).
    :cvar ROAD_MARKING_WORK: Striping and repainting of road markings,
        plus placement or replacement of reflecting studs (cats' eyes).
    :cvar ROADSIDE_WORK: Road side work of an unspecified nature.
    :cvar ROADWORKS_CLEARANCE: Roadworks are completed and are being
        cleared.
    :cvar ROADWORKS: Road maintenance or improvement activity of an
        unspecified nature which may potentially cause traffic
        disruption.
    :cvar ROCK_FALL_PREVENTATIVE_MAINTENANCE: Rock fall preventative
        maintenance.
    :cvar SALTING_IN_PROGRESS: Spreading of salt and / or grit on the
        road surface to prevent or melt snow or ice.
    :cvar SNOWPLOUGHS_IN_USE: Snowploughs or other similar mechanical
        devices in use to clear snow from the road.
    :cvar SWEEPING_OF_ROAD: Sweeping of the roadway.
    :cvar TREE_AND_VEGETATION_CUTTING_WORK: Tree and vegetation cutting
        work adjacent to the roadway.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ACCIDENT_REPAIR_WORK = "accidentRepairWork"
    CLEARANCE_WORK = "clearanceWork"
    CONTROLLED_AVALANCHE = "controlledAvalanche"
    INSTALLATION_WORK = "installationWork"
    GRASS_CUTTING_WORK = "grassCuttingWork"
    LITTER_CLEARANCE = "litterClearance"
    MAINTENANCE_WORK = "maintenanceWork"
    MAINTENANCE_PEOPLE_ON_ROAD = "maintenancePeopleOnRoad"
    OVERHEAD_WORKS = "overheadWorks"
    REPAIR_WORK = "repairWork"
    RESURFACING_WORK = "resurfacingWork"
    ROAD_MARKING_WORK = "roadMarkingWork"
    ROADSIDE_WORK = "roadsideWork"
    ROADWORKS_CLEARANCE = "roadworksClearance"
    ROADWORKS = "roadworks"
    ROCK_FALL_PREVENTATIVE_MAINTENANCE = "rockFallPreventativeMaintenance"
    SALTING_IN_PROGRESS = "saltingInProgress"
    SNOWPLOUGHS_IN_USE = "snowploughsInUse"
    SWEEPING_OF_ROAD = "sweepingOfRoad"
    TREE_AND_VEGETATION_CUTTING_WORK = "treeAndVegetationCuttingWork"
    OTHER = "other"
    EXTENDED = "_extended"


class RoadOperatorServiceDisruptionTypeEnum1(Enum):
    """
    Types of disruption to road operator services relevant to road users.

    :cvar EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE: Emergency telephone
        number for use by public to report incidents is out of service.
    :cvar INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE: Road
        information service telephone number is out of service.
    :cvar NO_TRAFFIC_OFFICER_PATROL_SERVICE: No traffic officer patrol
        service is operating.
    :cvar EXTENDED:
    """
    EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE = "emergencyTelephoneNumberOutOfService"
    INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE = "informationServiceTelephoneNumberOutOfService"
    NO_TRAFFIC_OFFICER_PATROL_SERVICE = "noTrafficOfficerPatrolService"
    EXTENDED = "_extended"


class RoadOrCarriagewayOrLaneManagementTypeEnum1(Enum):
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
    :cvar HARD_SHOULDER_RUNNING_NOT_IN_OPERATION: the hardshoulder used
        for dynamic hardshoulder management is closed to vehicles i.e.
        not running
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
    :cvar EXTENDED:
    """
    CAR_POOL_LANE_IN_OPERATION = "carPoolLaneInOperation"
    CARRIAGEWAY_CLOSURES = "carriagewayClosures"
    CLEAR_ALANE_FOR_EMERGENCY_VEHICLES = "clearALaneForEmergencyVehicles"
    CLEAR_ALANE_FOR_SNOWPLOUGHS_AND_GRITTING_VEHICLES = "clearALaneForSnowploughsAndGrittingVehicles"
    CLOSED_PERMANENTLY_FOR_THE_WINTER = "closedPermanentlyForTheWinter"
    CONTRAFLOW = "contraflow"
    DO_NOT_USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "doNotUseSpecifiedLanesOrCarriageways"
    HARD_SHOULDER_RUNNING_IN_OPERATION = "hardShoulderRunningInOperation"
    HARD_SHOULDER_RUNNING_NOT_IN_OPERATION = "hardShoulderRunningNotInOperation"
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
    USE_OF_SPECIFIED_LANES_OR_CARRIAGEWAYS_ALLOWED = "useOfSpecifiedLanesOrCarriagewaysAllowed"
    USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "useSpecifiedLanesOrCarriageways"
    VEHICLE_STORAGE_IN_OPERATION = "vehicleStorageInOperation"
    WEIGHT_RESTRICTION_IN_OPERATION = "weightRestrictionInOperation"
    OTHER = "other"
    EXTENDED = "_extended"


class RoadsideAssistanceTypeEnum1(Enum):
    """
    Types of road side assistance.

    :cvar AIR_AMBULANCE: Air ambulance assistance.
    :cvar BUS_PASSENGER_ASSISTANCE: Bus passenger assistance.
    :cvar EMERGENCY_SERVICES: Emergency services assistance.
    :cvar FIRST_AID: First aid assistance.
    :cvar FOOD_DELIVERY: Food delivery.
    :cvar HELICOPTER_RESCUE: Helicopter rescue.
    :cvar VEHICLE_REPAIR: Vehicle repair assistance.
    :cvar VEHICLE_RECOVERY: Vehicle recovery.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AIR_AMBULANCE = "airAmbulance"
    BUS_PASSENGER_ASSISTANCE = "busPassengerAssistance"
    EMERGENCY_SERVICES = "emergencyServices"
    FIRST_AID = "firstAid"
    FOOD_DELIVERY = "foodDelivery"
    HELICOPTER_RESCUE = "helicopterRescue"
    VEHICLE_REPAIR = "vehicleRepair"
    VEHICLE_RECOVERY = "vehicleRecovery"
    OTHER = "other"
    EXTENDED = "_extended"


class RoadworksDurationEnum1(Enum):
    """
    Expected durations of roadworks in general terms.

    :cvar LONG_TERM: The roadworks are expected to last for a long term
        (according to a classification scheme used by the responsible
        road operator)
    :cvar MEDIUM_TERM: The roadworks are expected to last for a medium
        term (according to a classification scheme used by the
        responsible road operator)
    :cvar SHORT_TERM: The roadworks are expected to last for a short
        term (according to a classification scheme used by the
        responsible road operator)
    :cvar EXTENDED:
    """
    LONG_TERM = "longTerm"
    MEDIUM_TERM = "mediumTerm"
    SHORT_TERM = "shortTerm"
    EXTENDED = "_extended"


class RoadworksScaleEnum1(Enum):
    """Grade of complexity of the roadworks according to the responsible road
    operator.

    For example determined by size, duration and/or traffic disruption.

    :cvar MAJOR: The roadworks scale is major according to the
        responsible road operator.
    :cvar MEDIUM: The roadworks scale is medium according to the
        responsible road operator.
    :cvar MINOR: The roadworks scale is minor according to the
        responsible road operator.
    :cvar EXTENDED:
    """
    MAJOR = "major"
    MEDIUM = "medium"
    MINOR = "minor"
    EXTENDED = "_extended"


class ServiceDisruptionTypeEnum1(Enum):
    """
    Types of disruption to services relevant to road users.

    :cvar BAR_CLOSED: Bar closed.
    :cvar DIESEL_SHORTAGE: There is a shortage of diesel at the
        specified location.
    :cvar FUEL_SHORTAGE: There is a shortage of fuel (of one or more
        types) at the specified location.
    :cvar LPG_SHORTAGE: There is a shortage of liquid petroleum gas at
        the specified location.
    :cvar METHANE_SHORTAGE: There is a shortage of methane at the
        specified location.
    :cvar NO_DIESEL_FOR_HEAVY_VEHICLES: There is no diesel available for
        heavy goods vehicles at the specified location.
    :cvar NO_DIESEL_FOR_LIGHT_VEHICLES: There is no diesel available for
        light vehicles at the specified location.
    :cvar NO_PARKING_AVAILABILITY: There is little or no availbility of
        parking
    :cvar NO_PUBLIC_TELEPHONES: There are no available public telephones
        at the specified location.
    :cvar NO_TOILET_FACILITIES: There are no available public toilet
        facilities at the specified location.
    :cvar NO_VEHICLE_REPAIR_FACILITIES: There are no available vehicle
        repair facilities at the specified location.
    :cvar PETROL_SHORTAGE: There is a shortage of petrol at the
        specified location.
    :cvar REST_AREA_BUSY: The rest area at the specified location is
        busy.
    :cvar REST_AREA_CLOSED: The rest area at the specified location is
        closed.
    :cvar REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA: The rest
        area at the specified location is close to capacity and
        motorists are advised to seek an alternative.
    :cvar SERVICE_AREA_BUSY: The service area at the specified location
        is close to capacity.
    :cvar SERVICE_AREA_CLOSED: The service area at the specified
        location is closed.
    :cvar SERVICE_AREA_FUEL_STATION_CLOSED: The fuel station at the
        specified service area is closed.
    :cvar SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA: The
        service area at the specified location is close to capacity and
        motorists are advised to seek an alternative.
    :cvar SERVICE_AREA_RESTAURANT_CLOSED: The restaurant at the
        specified service area is closed.
    :cvar SOME_COMMERCIAL_SERVICES_CLOSED: Some commercial services are
        closed at the specified location.
    :cvar WATER_SHORTAGE: There is a shortage of water at the specified
        location.
    :cvar EXTENDED:
    """
    BAR_CLOSED = "barClosed"
    DIESEL_SHORTAGE = "dieselShortage"
    FUEL_SHORTAGE = "fuelShortage"
    LPG_SHORTAGE = "lpgShortage"
    METHANE_SHORTAGE = "methaneShortage"
    NO_DIESEL_FOR_HEAVY_VEHICLES = "noDieselForHeavyVehicles"
    NO_DIESEL_FOR_LIGHT_VEHICLES = "noDieselForLightVehicles"
    NO_PARKING_AVAILABILITY = "noParkingAvailability"
    NO_PUBLIC_TELEPHONES = "noPublicTelephones"
    NO_TOILET_FACILITIES = "noToiletFacilities"
    NO_VEHICLE_REPAIR_FACILITIES = "noVehicleRepairFacilities"
    PETROL_SHORTAGE = "petrolShortage"
    REST_AREA_BUSY = "restAreaBusy"
    REST_AREA_CLOSED = "restAreaClosed"
    REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA = "restAreaOvercrowdedDriveToAnotherRestArea"
    SERVICE_AREA_BUSY = "serviceAreaBusy"
    SERVICE_AREA_CLOSED = "serviceAreaClosed"
    SERVICE_AREA_FUEL_STATION_CLOSED = "serviceAreaFuelStationClosed"
    SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA = "serviceAreaOvercrowdedDriveToAnotherServiceArea"
    SERVICE_AREA_RESTAURANT_CLOSED = "serviceAreaRestaurantClosed"
    SOME_COMMERCIAL_SERVICES_CLOSED = "someCommercialServicesClosed"
    WATER_SHORTAGE = "waterShortage"
    EXTENDED = "_extended"


class SeverityEnum1(Enum):
    """
    Levels of severity of a situation as whole assessed by the impact that the
    situation may have on traffic flow as perceived by the supplier.

    :cvar HIGHEST: Perceived by supplier as being of the highest level.
    :cvar HIGH: Perceived by supplier as being of a high level.
    :cvar MEDIUM: Perceived by supplier as being of a medium level.
    :cvar LOW: Perceived by supplier as being of a low level.
    :cvar LOWEST: Perceived by supplier as being of the lowest
        discernible level.
    :cvar NONE_VALUE: Perceived by supplier as having a severity rating
        of none.
    :cvar UNKNOWN: Perceived by supplier as being of an unknown level.
    :cvar EXTENDED:
    """
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class SpeedManagementTypeEnum1(Enum):
    """
    Management actions relating to speed.

    :cvar ACTIVE_SPEED_CONTROL_IN_OPERATION: Automatic speed control
        measures are in place at the specified location, whereby speed
        limits are set by an automatic system which is triggered by
        traffic sensing equipment.
    :cvar DO_NOT_SLOWDOWN_UNNECESSARILY: Do not slow down unnecessarily.
    :cvar OBSERVE_SPEED_LIMIT: Observe speed limit.
    :cvar POLICE_SPEED_CHECKS_IN_OPERATION: Police speed checks are in
        operation.
    :cvar REDUCE_YOUR_SPEED: Reduce your speed.
    :cvar SPEED_RESTRICTION_IN_OPERATION: A speed restriction is in
        operation.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ACTIVE_SPEED_CONTROL_IN_OPERATION = "activeSpeedControlInOperation"
    DO_NOT_SLOWDOWN_UNNECESSARILY = "doNotSlowdownUnnecessarily"
    OBSERVE_SPEED_LIMIT = "observeSpeedLimit"
    POLICE_SPEED_CHECKS_IN_OPERATION = "policeSpeedChecksInOperation"
    REDUCE_YOUR_SPEED = "reduceYourSpeed"
    SPEED_RESTRICTION_IN_OPERATION = "speedRestrictionInOperation"
    OTHER = "other"
    EXTENDED = "_extended"


class SubjectTypeOfWorksEnum1(Enum):
    """
    Subject types of construction or maintenance work.

    :cvar BRIDGE: Bridge on, over or under the highway.
    :cvar BURIED_CABLES: Buried cables under or along the highway.
    :cvar BURIED_SERVICES: Unspecified buried services on, under or
        along the highway.
    :cvar CRASH_BARRIER: Crash barrier.
    :cvar CYCLE_TRACK: Cycle track adjacent to the road
    :cvar FOOTPATH: a footpath
    :cvar GALLERY: Gallery.
    :cvar GANTRY: Gantry over or above the roadway.
    :cvar GAS_MAIN_WORK: Gas mains.
    :cvar HEATING_PIPE: a heating pipe
    :cvar INTERCHANGE: Motorway or major road interchange.
    :cvar JUNCTION: Motorway or major road junction.
    :cvar LEVEL_CROSSING: Level-crossing or associated equipment.
    :cvar LIGHTING_SYSTEM: Road lighting system.
    :cvar LOCK: lock on a waterway adjacent to the road
    :cvar MEASUREMENT_EQUIPMENT: Equipment used for determining traffic
        measurements.
    :cvar METRO: passenger railway system, typically underground, in a
        metropolitan area
    :cvar NOISE_PROTECTION: Installations along the roadway designed to
        reduce road noise in the surrounding environment.
    :cvar PARKING: parking facilities
    :cvar PUBLIC_TRANSPORT_INFRASTRUCTURE: public transport
        infrastructure
    :cvar PUBLIC_TRANSPORT_STOP: public transport stop (including but
        not limited to bus stops, trams stops, taxi stops)
    :cvar ROAD: Road.
    :cvar ROAD_SIGNS: Road signs.
    :cvar ROADSIDE_DRAINS: Roadside drains.
    :cvar ROADSIDE_EMBANKMENT: Roadside embankment.
    :cvar ROADSIDE_EQUIPMENT: Roadside equipment.
    :cvar ROUNDABOUT: Roundabout.
    :cvar SEWER: a sewer
    :cvar STREET_PARKING: street parking places
    :cvar TOLL_GATE: Toll gate.
    :cvar TRAFFIC_SIGNALS: traffic signals
    :cvar TUNNEL: Road tunnel.
    :cvar WATER_BANK: bank of a waterway adjacent to the road
    :cvar WATER_MAIN: Water main under or along the highway.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    BRIDGE = "bridge"
    BURIED_CABLES = "buriedCables"
    BURIED_SERVICES = "buriedServices"
    CRASH_BARRIER = "crashBarrier"
    CYCLE_TRACK = "cycleTrack"
    FOOTPATH = "footpath"
    GALLERY = "gallery"
    GANTRY = "gantry"
    GAS_MAIN_WORK = "gasMainWork"
    HEATING_PIPE = "heatingPipe"
    INTERCHANGE = "interchange"
    JUNCTION = "junction"
    LEVEL_CROSSING = "levelCrossing"
    LIGHTING_SYSTEM = "lightingSystem"
    LOCK = "lock"
    MEASUREMENT_EQUIPMENT = "measurementEquipment"
    METRO = "metro"
    NOISE_PROTECTION = "noiseProtection"
    PARKING = "parking"
    PUBLIC_TRANSPORT_INFRASTRUCTURE = "publicTransportInfrastructure"
    PUBLIC_TRANSPORT_STOP = "publicTransportStop"
    ROAD = "road"
    ROAD_SIGNS = "roadSigns"
    ROADSIDE_DRAINS = "roadsideDrains"
    ROADSIDE_EMBANKMENT = "roadsideEmbankment"
    ROADSIDE_EQUIPMENT = "roadsideEquipment"
    ROUNDABOUT = "roundabout"
    SEWER = "sewer"
    STREET_PARKING = "streetParking"
    TOLL_GATE = "tollGate"
    TRAFFIC_SIGNALS = "trafficSignals"
    TUNNEL = "tunnel"
    WATER_BANK = "waterBank"
    WATER_MAIN = "waterMain"
    OTHER = "other"
    EXTENDED = "_extended"


class TrafficConstrictionTypeEnum1(Enum):
    """
    Types of constriction to which traffic is subjected as a result of an
    event.

    :cvar CARRIAGEWAY_BLOCKED: The carriageway is totally obstructed in
        the specified direction due to an unplanned event.
    :cvar CARRIAGEWAY_PARTIALLY_OBSTRUCTED: The carriageway is partially
        obstructed in the specified direction due to an unplanned event.
    :cvar LANES_BLOCKED: One or more lanes is totally obstructed in the
        specified direction due to an unplanned event.
    :cvar LANES_PARTIALLY_OBSTRUCTED: One or more lanes is partially
        obstructed in the specified direction due to an unplanned event.
    :cvar ROAD_BLOCKED: The road is totally obstructed, for all vehicles
        in both directions, due to an unplanned event.
    :cvar ROAD_PARTIALLY_OBSTRUCTED: The road is partially obstructed in
        both directions due to an unplanned event.
    :cvar EXTENDED:
    """
    CARRIAGEWAY_BLOCKED = "carriagewayBlocked"
    CARRIAGEWAY_PARTIALLY_OBSTRUCTED = "carriagewayPartiallyObstructed"
    LANES_BLOCKED = "lanesBlocked"
    LANES_PARTIALLY_OBSTRUCTED = "lanesPartiallyObstructed"
    ROAD_BLOCKED = "roadBlocked"
    ROAD_PARTIALLY_OBSTRUCTED = "roadPartiallyObstructed"
    EXTENDED = "_extended"


class TrafficFlowCharacteristicsEnum1(Enum):
    """
    Types of consistency (steadiness) of traffic flow.

    :cvar ERRATIC_FLOW: Traffic flow is of an irregular nature, subject
        to sudden changes in rates.
    :cvar SMOOTH_FLOW: Traffic flow is smooth.
    :cvar STOP_AND_GO: Traffic flow is of a stop and go nature with
        queues forming and ending continuously on the specified section
        of road.
    :cvar TRAFFIC_BLOCKED: Traffic is blocked at the specified location
        and in the specified direction due to an unplanned event.
    :cvar EXTENDED:
    """
    ERRATIC_FLOW = "erraticFlow"
    SMOOTH_FLOW = "smoothFlow"
    STOP_AND_GO = "stopAndGo"
    TRAFFIC_BLOCKED = "trafficBlocked"
    EXTENDED = "_extended"


class TrafficTypeEnum1(Enum):
    """
    Types of traffic, mostly classified by its destination type.

    :cvar ACCESS_ONLY_TRAFFIC: Traffic destined for local access only.
    :cvar DESTINED_FOR_AIRPORT: Traffic destined for the airport.
    :cvar DESTINED_FOR_AIRPORT_ARRIVALS: Traffic destined for airport
        arrivals.
    :cvar DESTINED_FOR_AIRPORT_DEPARTURES: Traffic destined for airport
        departures.
    :cvar DESTINED_FOR_FERRY_SERVICE: Traffic destined for the ferry
        service.
    :cvar DESTINED_FOR_RAIL_SERVICE: Traffic destined for the rail
        service.
    :cvar HOLIDAY_TRAFFIC: Traffic heading towards holiday destinations.
    :cvar LOCAL_TRAFFIC: Traffic heading towards local destinations.
    :cvar LONG_DISTANCE_TRAFFIC: Traffic heading towards destinations
        which are a long distance away.
    :cvar REGIONAL_TRAFFIC: Traffic heading towards local regional
        destinations.
    :cvar RESIDENTS_ONLY_TRAFFIC: Local residents only traffic.
    :cvar THROUGH_TRAFFIC: Traffic which is not for local access, i.e.
        traffic not destined for local town, city or built up area but
        for transit though the area.
    :cvar VISITOR_TRAFFIC: Traffic heading towards local visitor
        attraction.
    :cvar EXTENDED:
    """
    ACCESS_ONLY_TRAFFIC = "accessOnlyTraffic"
    DESTINED_FOR_AIRPORT = "destinedForAirport"
    DESTINED_FOR_AIRPORT_ARRIVALS = "destinedForAirportArrivals"
    DESTINED_FOR_AIRPORT_DEPARTURES = "destinedForAirportDepartures"
    DESTINED_FOR_FERRY_SERVICE = "destinedForFerryService"
    DESTINED_FOR_RAIL_SERVICE = "destinedForRailService"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    LOCAL_TRAFFIC = "localTraffic"
    LONG_DISTANCE_TRAFFIC = "longDistanceTraffic"
    REGIONAL_TRAFFIC = "regionalTraffic"
    RESIDENTS_ONLY_TRAFFIC = "residentsOnlyTraffic"
    THROUGH_TRAFFIC = "throughTraffic"
    VISITOR_TRAFFIC = "visitorTraffic"
    EXTENDED = "_extended"


class TransitServiceInformationEnum1(Enum):
    """
    Types of public transport information.

    :cvar CANCELLATIONS: Public transport, park-and-ride, rail or bus
        services are cancelled.
    :cvar DELAY_DUE_TO_BAD_WEATHER: The specified service is delayed due
        to bad weather.
    :cvar DELAY_DUE_TO_REPAIRS: The specified service is delayed due to
        the need for repairs.
    :cvar DELAYED_UNTIL_FURTHER_NOTICE: The specified public transport
        service will be delayed until further notice.
    :cvar DELAYS_DUE_TO_FLOTSAM: The departure of the specified ferry
        service is delayed due to flotsam.
    :cvar DEPARTURE_ON_SCHEDULE: The departure of the specified service
        is on schedule.
    :cvar FERRY_REPLACED_BY_ICE_ROAD: The ferry service has been
        replaced by an ice road.
    :cvar FREE_SHUTTLE_SERVICE_OPERATING: A shuttle service is operating
        at no charge between specified locations.
    :cvar INFORMATION_SERVICE_NOT_AVAILABLE: The information service
        relating to the specified transport system is not currently
        available.
    :cvar IRREGULAR_SERVICE_DELAYS: The specified service is subject to
        irregular delays.
    :cvar LOAD_CAPACITY_CHANGED: The load capacity for the specified
        service has been changed.
    :cvar RESTRICTIONS_FOR_LONGER_VEHICLES: Long vehicles are subject to
        restrictions on the specified service.
    :cvar SERVICE_DELAYS: The specified service is subject to delays.
    :cvar SERVICE_DELAYS_OF_UNCERTAIN_DURATION: The specified service is
        subject to delays whose predicted duration cannot be estimated
        accurately.
    :cvar SERVICE_FULLY_BOOKED: The departure of the specified service
        is fully booked.
    :cvar SERVICE_NOT_OPERATING: The specified service is not operating.
    :cvar SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE: The
        specified service is not operating but an alternative service is
        available.
    :cvar SERVICE_SUSPENDED: The specified service has been suspended.
    :cvar SERVICE_WITHDRAWN: The specified service has been cancelled.
    :cvar SHUTTLE_SERVICE_OPERATING: A shuttle service is operating
        between the specified locations.
    :cvar TEMPORARY_CHANGES_TO_TIMETABLES: The timetable for the
        specified service is subject to temporary changes.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    CANCELLATIONS = "cancellations"
    DELAY_DUE_TO_BAD_WEATHER = "delayDueToBadWeather"
    DELAY_DUE_TO_REPAIRS = "delayDueToRepairs"
    DELAYED_UNTIL_FURTHER_NOTICE = "delayedUntilFurtherNotice"
    DELAYS_DUE_TO_FLOTSAM = "delaysDueToFlotsam"
    DEPARTURE_ON_SCHEDULE = "departureOnSchedule"
    FERRY_REPLACED_BY_ICE_ROAD = "ferryReplacedByIceRoad"
    FREE_SHUTTLE_SERVICE_OPERATING = "freeShuttleServiceOperating"
    INFORMATION_SERVICE_NOT_AVAILABLE = "informationServiceNotAvailable"
    IRREGULAR_SERVICE_DELAYS = "irregularServiceDelays"
    LOAD_CAPACITY_CHANGED = "loadCapacityChanged"
    RESTRICTIONS_FOR_LONGER_VEHICLES = "restrictionsForLongerVehicles"
    SERVICE_DELAYS = "serviceDelays"
    SERVICE_DELAYS_OF_UNCERTAIN_DURATION = "serviceDelaysOfUncertainDuration"
    SERVICE_FULLY_BOOKED = "serviceFullyBooked"
    SERVICE_NOT_OPERATING = "serviceNotOperating"
    SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE = "serviceNotOperatingSubstituteServiceAvailable"
    SERVICE_SUSPENDED = "serviceSuspended"
    SERVICE_WITHDRAWN = "serviceWithdrawn"
    SHUTTLE_SERVICE_OPERATING = "shuttleServiceOperating"
    TEMPORARY_CHANGES_TO_TIMETABLES = "temporaryChangesToTimetables"
    OTHER = "other"
    EXTENDED = "_extended"


class TransitServiceTypeEnum1(Enum):
    """
    Types of transport services available to the general public.

    :cvar AIR: Air service.
    :cvar BUS: Bus service.
    :cvar FERRY: Ferry service.
    :cvar HYDROFOIL: Hydrofoil service.
    :cvar RAIL: Rail service.
    :cvar TRAM: Tram service.
    :cvar UNDERGROUND_METRO: Underground or metro service.
    :cvar EXTENDED:
    """
    AIR = "air"
    BUS = "bus"
    FERRY = "ferry"
    HYDROFOIL = "hydrofoil"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND_METRO = "undergroundMetro"
    EXTENDED = "_extended"


class VehicleObstructionTypeEnum1(Enum):
    """
    Types of obstructions involving vehicles.

    :cvar ABANDONED_VEHICLE: Abandoned vehicle(s) on the roadway which
        may cause traffic disruption.
    :cvar ABNORMAL_LOAD: Vehicle(s) carrying exceptional load(s) which
        may cause traffic disruption.
    :cvar BROKEN_DOWN_VEHICLE: Broken down vehicle(s) on the carriageway
        which may cause traffic disruption.
    :cvar CONVOY: A group of vehicles moving together in formation which
        may cause traffic disruption.
    :cvar DAMAGED_VEHICLE: Damaged vehicle(s) on the carriageway which
        may cause traffic disruption.
    :cvar DANGEROUS_SLOW_MOVING_VEHICLE: Dangerous slow moving vehicles
        which may cause traffic disruption.
    :cvar EMERGENCY_VEHICLE: Emergency service vehicles on the roadway
        in response to an emergency situation.
    :cvar HIGH_SPEED_EMERGENCY_VEHICLE: Emergency service vehicles
        progressing at high speed along the roadway in response to or en
        route from an emergency situation.
    :cvar LONG_LOAD: A vehicle of length greater than that normally
        allowed which may cause traffic disruption.
    :cvar HIGH_SPEED_CHASE: Authorised and unauthorised vehicles are
        travelling at high speeds along the roadway.  This may present a
        hazard to other vehicles.
    :cvar MEDICAL_EMERGENCY: Vehicle has stopped due a medical issue of
        a driver or passenger
    :cvar MILITARY_CONVOY: A group of military vehicles moving together
        in formation which may cause traffic disruption.
    :cvar OVERHEIGHT_VEHICLE: Vehicles of height greater than normally
        allowed which may cause traffic disruption.
    :cvar PROHIBITED_VEHICLE_ON_THE_ROAD: Vehicles not normally
        permitted on the motorway are present which may cause traffic
        disruption.
    :cvar RECKLESS_DRIVER: A vehicle being driven without due care and
        attention is causing a hazard to other vehicles.
    :cvar SLOW_VEHICLE: A vehicle travelling at well below normal
        highway speeds which may cause traffic disruption.
    :cvar SPECIAL_PERMIT_TRANSPORT: Special type of load or vehicle
        size, or even speed, that is allowed on the road only with
        special permission. The presence of this transport may cause
        traffic disruption.
    :cvar TRACKED_VEHICLE: Carterpillar tracked vehicles are in use
        which may cause traffic disruption.
    :cvar UNLIT_VEHICLE_ON_THE_ROAD: Vehicles without lights are in use
        which may present a hazard to road users.
    :cvar VEHICLE_ON_FIRE: A vehicle is or has been on fire and may
        cause traffic disruption.
    :cvar VEHICLE_CARRYING_HAZARDOUS_MATERIALS: Vehicles carrying
        materials of a hazardous nature are present and these could
        expose road users to additional hazards.
    :cvar VEHICLE_IN_DIFFICULTY: A vehicle is experiencing difficulties
        (e.g. manoeuvring or propulsion difficulties) which may cause
        traffic disruption.
    :cvar VEHICLE_ON_WRONG_CARRIAGEWAY: A vehicle is travelling the
        wrong way along a divided highway (i.e. on the wrong side).
    :cvar VEHICLE_STUCK: One or more vehicles are stuck (i.e. unable to
        move) due to environmental conditions such as a snow drift or
        severe icy road.
    :cvar VEHICLE_WITH_OVERHEIGHT_LOAD: An over-height vehicle which may
        present a hazard to road users.
    :cvar VEHICLE_WITH_OVERWIDE_LOAD: A vehicle of width greater than
        that normally allowed which may cause traffic disruption.
    :cvar WINTER_MAINTETANCE_VEHICLE_IN_TRANSFER: Winter maintenance
        vehicle is on the road, not doing its specific work. Its
        presence may cause traffic disruption.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ABANDONED_VEHICLE = "abandonedVehicle"
    ABNORMAL_LOAD = "abnormalLoad"
    BROKEN_DOWN_VEHICLE = "brokenDownVehicle"
    CONVOY = "convoy"
    DAMAGED_VEHICLE = "damagedVehicle"
    DANGEROUS_SLOW_MOVING_VEHICLE = "dangerousSlowMovingVehicle"
    EMERGENCY_VEHICLE = "emergencyVehicle"
    HIGH_SPEED_EMERGENCY_VEHICLE = "highSpeedEmergencyVehicle"
    LONG_LOAD = "longLoad"
    HIGH_SPEED_CHASE = "highSpeedChase"
    MEDICAL_EMERGENCY = "medicalEmergency"
    MILITARY_CONVOY = "militaryConvoy"
    OVERHEIGHT_VEHICLE = "overheightVehicle"
    PROHIBITED_VEHICLE_ON_THE_ROAD = "prohibitedVehicleOnTheRoad"
    RECKLESS_DRIVER = "recklessDriver"
    SLOW_VEHICLE = "slowVehicle"
    SPECIAL_PERMIT_TRANSPORT = "specialPermitTransport"
    TRACKED_VEHICLE = "trackedVehicle"
    UNLIT_VEHICLE_ON_THE_ROAD = "unlitVehicleOnTheRoad"
    VEHICLE_ON_FIRE = "vehicleOnFire"
    VEHICLE_CARRYING_HAZARDOUS_MATERIALS = "vehicleCarryingHazardousMaterials"
    VEHICLE_IN_DIFFICULTY = "vehicleInDifficulty"
    VEHICLE_ON_WRONG_CARRIAGEWAY = "vehicleOnWrongCarriageway"
    VEHICLE_STUCK = "vehicleStuck"
    VEHICLE_WITH_OVERHEIGHT_LOAD = "vehicleWithOverheightLoad"
    VEHICLE_WITH_OVERWIDE_LOAD = "vehicleWithOverwideLoad"
    WINTER_MAINTETANCE_VEHICLE_IN_TRANSFER = "winterMaintetanceVehicleInTransfer"
    OTHER = "other"
    EXTENDED = "_extended"


class VehicleProblemCauseEnum1(Enum):
    """
    The component of the vehicle that has caused a problem.

    :cvar AIR_SYSTEM: Problem with the air system of a vehicle
    :cvar BATTERY: Problem with the battery of a vehicle
    :cvar BRAKING_SYSTEM: Problem with the braking system of a vehicle
    :cvar COOLING_SYSTEM: Problem with the cooling system of a vehicle
    :cvar DECOUPLED_TRAILER: Problem with the coupling of a trailer
    :cvar DIVER_PROBLEM: Problem with a vehicle driver
    :cvar ELECTRICAL_SYSTEM: Problem with the electrical system of a
        vehicle
    :cvar FLAT_TYRE: Vehicle has one or more flat tyres
    :cvar FUEL_SYSTEM: Problem with the fuel system of a vehicle
    :cvar GEAR: Problem with the gears of a vehicle
    :cvar LOAD_PROBLEM: Problem with the load of a vehicle
    :cvar LOST_WHEEL: Vehicle has lost a wheel
    :cvar MOTOR_MECHANICS: Problem with the motor mechanics of a vehicle
    :cvar OIL_LEAKAGE: Vehicle has an oil leak
    :cvar SUSPENSION: Problem with the suspension of a vehicle
    :cvar OTHER: Other vehicle problem source
    :cvar UNKNOWN: Unknown vehicle problem source
    :cvar EXTENDED:
    """
    AIR_SYSTEM = "airSystem"
    BATTERY = "battery"
    BRAKING_SYSTEM = "brakingSystem"
    COOLING_SYSTEM = "coolingSystem"
    DECOUPLED_TRAILER = "decoupledTrailer"
    DIVER_PROBLEM = "diverProblem"
    ELECTRICAL_SYSTEM = "electricalSystem"
    FLAT_TYRE = "flatTyre"
    FUEL_SYSTEM = "fuelSystem"
    GEAR = "gear"
    LOAD_PROBLEM = "loadProblem"
    LOST_WHEEL = "lostWheel"
    MOTOR_MECHANICS = "motorMechanics"
    OIL_LEAKAGE = "oilLeakage"
    SUSPENSION = "suspension"
    OTHER = "other"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


@dataclass
class AbnormalTrafficTypeEnum2:
    class Meta:
        name = "_AbnormalTrafficTypeEnum"

    value: Optional[AbnormalTrafficTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AccidentCauseEnum2:
    class Meta:
        name = "_AccidentCauseEnum"

    value: Optional[AccidentCauseEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AccidentTypeEnum2:
    class Meta:
        name = "_AccidentTypeEnum"

    value: Optional[AccidentTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AnimalPresenceTypeEnum2:
    class Meta:
        name = "_AnimalPresenceTypeEnum"

    value: Optional[AnimalPresenceTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AuthorityOperationTypeEnum2:
    class Meta:
        name = "_AuthorityOperationTypeEnum"

    value: Optional[AuthorityOperationTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CauseTypeEnum2:
    class Meta:
        name = "_CauseTypeEnum"

    value: Optional[CauseTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CollisionTypeEnum2:
    class Meta:
        name = "_CollisionTypeEnum"

    value: Optional[CollisionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CommentTypeEnum2:
    class Meta:
        name = "_CommentTypeEnum"

    value: Optional[CommentTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ComplianceOptionEnum2:
    class Meta:
        name = "_ComplianceOptionEnum"

    value: Optional[ComplianceOptionEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ConstructionWorkTypeEnum2:
    class Meta:
        name = "_ConstructionWorkTypeEnum"

    value: Optional[ConstructionWorkTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DelayBandEnum2:
    class Meta:
        name = "_DelayBandEnum"

    value: Optional[DelayBandEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DelaysTypeEnum2:
    class Meta:
        name = "_DelaysTypeEnum"

    value: Optional[DelaysTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DisturbanceActivityTypeEnum2:
    class Meta:
        name = "_DisturbanceActivityTypeEnum"

    value: Optional[DisturbanceActivityTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DrivingConditionTypeEnum2:
    class Meta:
        name = "_DrivingConditionTypeEnum"

    value: Optional[DrivingConditionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class EnvironmentalObstructionTypeEnum2:
    class Meta:
        name = "_EnvironmentalObstructionTypeEnum"

    value: Optional[EnvironmentalObstructionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class EquipmentOrSystemFaultTypeEnum2:
    class Meta:
        name = "_EquipmentOrSystemFaultTypeEnum"

    value: Optional[EquipmentOrSystemFaultTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class EquipmentOrSystemTypeEnum2:
    class Meta:
        name = "_EquipmentOrSystemTypeEnum"

    value: Optional[EquipmentOrSystemTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class GeneralInstructionToRoadUsersTypeEnum2:
    class Meta:
        name = "_GeneralInstructionToRoadUsersTypeEnum"

    value: Optional[GeneralInstructionToRoadUsersTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class GeneralNetworkManagementTypeEnum2:
    class Meta:
        name = "_GeneralNetworkManagementTypeEnum"

    value: Optional[GeneralNetworkManagementTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InfrastructureDamageTypeEnum2:
    class Meta:
        name = "_InfrastructureDamageTypeEnum"

    value: Optional[InfrastructureDamageTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InjuryStatusTypeEnum2:
    class Meta:
        name = "_InjuryStatusTypeEnum"

    value: Optional[InjuryStatusTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InvolvementRolesEnum2:
    class Meta:
        name = "_InvolvementRolesEnum"

    value: Optional[InvolvementRolesEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class MaintenanceVehicleActionsEnum2:
    class Meta:
        name = "_MaintenanceVehicleActionsEnum"

    value: Optional[MaintenanceVehicleActionsEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class MobilityTypeEnum2:
    class Meta:
        name = "_MobilityTypeEnum"

    value: Optional[MobilityTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class NonWeatherRelatedRoadConditionTypeEnum2:
    class Meta:
        name = "_NonWeatherRelatedRoadConditionTypeEnum"

    value: Optional[NonWeatherRelatedRoadConditionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ObstructionTypeEnum2:
    class Meta:
        name = "_ObstructionTypeEnum"

    value: Optional[ObstructionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OperatorActionOriginEnum2:
    class Meta:
        name = "_OperatorActionOriginEnum"

    value: Optional[OperatorActionOriginEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OperatorActionStatusEnum2:
    class Meta:
        name = "_OperatorActionStatusEnum"

    value: Optional[OperatorActionStatusEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PersonCategoryEnum2:
    class Meta:
        name = "_PersonCategoryEnum"

    value: Optional[PersonCategoryEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PlacesEnum2:
    class Meta:
        name = "_PlacesEnum"

    value: Optional[PlacesEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PoorEnvironmentTypeEnum2:
    class Meta:
        name = "_PoorEnvironmentTypeEnum"

    value: Optional[PoorEnvironmentTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ProbabilityOfOccurrenceEnum2:
    class Meta:
        name = "_ProbabilityOfOccurrenceEnum"

    value: Optional[ProbabilityOfOccurrenceEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RelativeTrafficFlowEnum2:
    class Meta:
        name = "_RelativeTrafficFlowEnum"

    value: Optional[RelativeTrafficFlowEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ReroutingManagementTypeEnum2:
    class Meta:
        name = "_ReroutingManagementTypeEnum"

    value: Optional[ReroutingManagementTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadMaintenanceTypeEnum2:
    class Meta:
        name = "_RoadMaintenanceTypeEnum"

    value: Optional[RoadMaintenanceTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadOperatorServiceDisruptionTypeEnum2:
    class Meta:
        name = "_RoadOperatorServiceDisruptionTypeEnum"

    value: Optional[RoadOperatorServiceDisruptionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadOrCarriagewayOrLaneManagementTypeEnum2:
    class Meta:
        name = "_RoadOrCarriagewayOrLaneManagementTypeEnum"

    value: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadsideAssistanceTypeEnum2:
    class Meta:
        name = "_RoadsideAssistanceTypeEnum"

    value: Optional[RoadsideAssistanceTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadworksDurationEnum2:
    class Meta:
        name = "_RoadworksDurationEnum"

    value: Optional[RoadworksDurationEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RoadworksScaleEnum2:
    class Meta:
        name = "_RoadworksScaleEnum"

    value: Optional[RoadworksScaleEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ServiceDisruptionTypeEnum2:
    class Meta:
        name = "_ServiceDisruptionTypeEnum"

    value: Optional[ServiceDisruptionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SeverityEnum2:
    class Meta:
        name = "_SeverityEnum"

    value: Optional[SeverityEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SituationRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="sit:SituationRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SituationVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationVersionedReference"

    target_class: str = field(
        init=False,
        default="sit:Situation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SpeedManagementTypeEnum2:
    class Meta:
        name = "_SpeedManagementTypeEnum"

    value: Optional[SpeedManagementTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SubjectTypeOfWorksEnum2:
    class Meta:
        name = "_SubjectTypeOfWorksEnum"

    value: Optional[SubjectTypeOfWorksEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TrafficConstrictionTypeEnum2:
    class Meta:
        name = "_TrafficConstrictionTypeEnum"

    value: Optional[TrafficConstrictionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TrafficFlowCharacteristicsEnum2:
    class Meta:
        name = "_TrafficFlowCharacteristicsEnum"

    value: Optional[TrafficFlowCharacteristicsEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TrafficTypeEnum2:
    class Meta:
        name = "_TrafficTypeEnum"

    value: Optional[TrafficTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TransitServiceInformationEnum2:
    class Meta:
        name = "_TransitServiceInformationEnum"

    value: Optional[TransitServiceInformationEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TransitServiceTypeEnum2:
    class Meta:
        name = "_TransitServiceTypeEnum"

    value: Optional[TransitServiceTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleObstructionTypeEnum2:
    class Meta:
        name = "_VehicleObstructionTypeEnum"

    value: Optional[VehicleObstructionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleProblemCauseEnum2:
    class Meta:
        name = "_VehicleProblemCauseEnum"

    value: Optional[VehicleProblemCauseEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class Comment:
    """
    A free text comment with an optional date/time stamp that can be used by
    the operator to convey un-coded observations/information.

    :ivar comment: A free text comment that can be used by the operator
        to convey un-coded observations/information.
    :ivar comment_date_time: The date/time at which the comment was
        made.
    :ivar comment_type: A classification of the the type of comment.
    :ivar comment_extension:
    """
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    comment_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    comment_type: Optional[CommentTypeEnum2] = field(
        default=None,
        metadata={
            "name": "commentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    comment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Delays:
    """The details of the delays being caused by the situation element defined
    in the situation record.

    It is recommended to only use one of the optional attributes to
    avoid confusion.

    :ivar delay_band: The time band within which the additional travel
        time due to adverse travel conditions of any kind falls, when
        compared to "normal conditions".
    :ivar delays_type: Coarse classification of the delay.
    :ivar delay_time_value: The value of the additional travel time due
        to adverse travel conditions of any kind, when compared to
        "normal conditions", given in seconds.
    :ivar delays_extension:
    """
    delay_band: Optional[DelayBandEnum2] = field(
        default=None,
        metadata={
            "name": "delayBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    delays_type: Optional[DelaysTypeEnum2] = field(
        default=None,
        metadata={
            "name": "delaysType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    delay_time_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "delayTimeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    delays_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_delaysExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class DetailedCauseType:
    """The type of influence that may be the cause of components of a
    situation.

    At least one attribute must be populated.

    :ivar abnormal_traffic_type: A characterization of the nature of
        abnormal traffic flow, i.e. specifically relating to the nature
        of the traffic movement.
    :ivar accident_type: A characterization of the nature of the
        accident.
    :ivar animal_presence_type: Indicates the nature of animals present
        on or near the roadway.
    :ivar authority_operation_type: Type of authority initiated
        operation or activity that could disrupt traffic.
    :ivar construction_work_type: The type of construction work being
        performed.
    :ivar disturbance_activity_type: Includes all situations of a public
        disorder type or of an alert type, with potential to disrupt
        traffic.
    :ivar driving_condition_type: Description of the driving conditions
        at the specified location.
    :ivar environmental_obstruction_type: Characterization of an
        obstruction on the road resulting from an environmental cause.
    :ivar equipment_or_system_fault_type: Failure, malfunction or non
        operational condition of equipment or system.
    :ivar general_instruction_to_road_users_type: General instruction
        that is issued by the network/road operator which is applicable
        to drivers and sometimes passengers.
    :ivar general_network_management_type: The type of traffic
        management action instigated by the network/road operator.
    :ivar infrastructure_damage_type: Characterization of an obstruction
        on the road resulting from the failure or damage of
        infrastructure on, under, above or close to the road.
    :ivar non_weather_related_road_condition_type: The type of road
        conditions which are not related to the weather.
    :ivar obstruction_type: Characterization of the type of general
        obstruction.
    :ivar poor_environment_type: The type of environment condition which
        is affecting driving conditions.
    :ivar public_event_type: Type of public event which could disrupt
        traffic.
    :ivar rerouting_management_type: Type of rerouting management action
        instigated by operator.
    :ivar road_maintenance_type: The type of road maintenance or
        installation work at the specified location.
    :ivar road_operator_service_disruption_type: The type of road
        operator service which is disrupted.
    :ivar road_or_carriageway_or_lane_management_type: Type of road,
        carriageway or lane management action instigated by operator.
    :ivar roadside_assistance_type: Indicates the nature of the road
        side assistance that will be, is or has been provided.
    :ivar roadside_service_disruption_type: The type of roadside service
        which is disrupted.
    :ivar speed_management_type: Type of speed management action
        instigated by operator.
    :ivar transit_service_information: Information about transit
        services.
    :ivar vehicle_obstruction_type: Characterization of an obstruction
        on the road caused by one or more vehicles.
    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar winter_equipment_management_type: Type of winter equipment
        management action instigated by operator.
    :ivar detailed_cause_type_extension:
    """
    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum2] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    accident_type: List[AccidentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    animal_presence_type: Optional[AnimalPresenceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    authority_operation_type: Optional[AuthorityOperationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    construction_work_type: Optional[ConstructionWorkTypeEnum2] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    disturbance_activity_type: Optional[DisturbanceActivityTypeEnum2] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    driving_condition_type: Optional[DrivingConditionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    environmental_obstruction_type: Optional[EnvironmentalObstructionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    equipment_or_system_fault_type: Optional[EquipmentOrSystemFaultTypeEnum2] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_instruction_to_road_users_type: Optional[GeneralInstructionToRoadUsersTypeEnum2] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_network_management_type: Optional[GeneralNetworkManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    infrastructure_damage_type: Optional[InfrastructureDamageTypeEnum2] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    non_weather_related_road_condition_type: List[NonWeatherRelatedRoadConditionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    obstruction_type: List[ObstructionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    poor_environment_type: List[PoorEnvironmentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    public_event_type: Optional[PublicEventTypeEnum2] = field(
        default=None,
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    rerouting_management_type: List[ReroutingManagementTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    road_maintenance_type: List[RoadMaintenanceTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    road_operator_service_disruption_type: List[RoadOperatorServiceDisruptionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    road_or_carriageway_or_lane_management_type: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    roadside_service_disruption_type: List[ServiceDisruptionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadsideServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    speed_management_type: Optional[SpeedManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    transit_service_information: Optional[TransitServiceInformationEnum2] = field(
        default=None,
        metadata={
            "name": "transitServiceInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    winter_equipment_management_type: Optional[WinterEquipmentManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    detailed_cause_type_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_detailedCauseTypeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class GroupOfPeopleInvolved:
    """
    Group of people involved in the event having common characteristics and/or
    status.

    :ivar number_of_people: The number of people of this group that are
        involved.
    :ivar injury_status_type: The injury status of the people involved.
    :ivar involvement_role: The involvement role of the people.
    :ivar category_of_people_involved: The category of persons involved.
    :ivar group_of_people_involved_extension:
    """
    number_of_people: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    injury_status_type: Optional[InjuryStatusTypeEnum2] = field(
        default=None,
        metadata={
            "name": "injuryStatusType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    involvement_role: Optional[InvolvementRolesEnum2] = field(
        default=None,
        metadata={
            "name": "involvementRole",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    category_of_people_involved: Optional[PersonCategoryEnum2] = field(
        default=None,
        metadata={
            "name": "categoryOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    group_of_people_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_groupOfPeopleInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class MaintenanceVehicles:
    """
    Details of the maintenance vehicles involved in the roadworks activity.

    :ivar number_of_maintenance_vehicles: The number of maintenance
        vehicles associated with the roadworks activities at the
        specified location.
    :ivar maintenance_vehicle_actions: The actions of the maintenance
        vehicles associated with the roadworks activities.
    :ivar maintenance_vehicles_extension:
    """
    number_of_maintenance_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfMaintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    maintenance_vehicle_actions: List[MaintenanceVehicleActionsEnum2] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceVehicleActions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    maintenance_vehicles_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_maintenanceVehiclesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Mobility:
    """
    An indication of whether the associated instance of a SituationRecord is
    mobile (e.g. a march or parade moving along a road) or stationary.

    :ivar mobility_type: An indication of whether the associated
        instance of a SituationRecord is mobile (e.g. a march or parade
        moving along a road) or stationary.
    :ivar speed: Speed of the mobile entity.
    :ivar mobility_extension:
    """
    mobility_type: Optional[MobilityTypeEnum2] = field(
        default=None,
        metadata={
            "name": "mobilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    mobility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_mobilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class SituationRecordReference(GlobalReference):
    """
    Reference to a SituationRecord.

    :ivar object_reference: A reference to a specific versioned
        identifiable object, which may be in this publication or an
        external publication
    :ivar situation_record_reference_extension:
    """
    object_reference: Optional[SituationRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "objectReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    situation_record_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationRecordReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class SituationReference(GlobalReference):
    """
    Reference to a Situation.

    :ivar object_reference: A reference to a specific versioned
        identifiable object, which may be in this publication or an
        external publication
    :ivar situation_reference_extension:
    """
    object_reference: Optional[SituationVersionedReference] = field(
        default=None,
        metadata={
            "name": "objectReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    situation_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Subjects:
    """
    The subjects with which the roadworks are associated.

    :ivar subject_type_of_works: The subject type of the roadworks (i.e.
        on what the construction or maintenance work is being
        performed).
    :ivar number_of_subjects: The number of subjects on which the
        roadworks (construction or maintenance) are being performed.
    :ivar subjects_extension:
    """
    subject_type_of_works: Optional[SubjectTypeOfWorksEnum2] = field(
        default=None,
        metadata={
            "name": "subjectTypeOfWorks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    number_of_subjects: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubjects",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    subjects_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_subjectsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Cause:
    """
    Contains details of the cause of a record within a situation.

    :ivar cause_description: Description of a cause which is not managed
        by the publication creator (e.g. an off network cause).
    :ivar cause_type: Indicates an external influence that may be the
        causation of components of a situation.
    :ivar detailed_cause_type: The type of cause, expressed in more
        detail than the NonManagedCause causeType. If both are present
        then they must be consistent.
    :ivar managed_cause: A reference to another situation record which
        defines a cause of the event defined here.
    :ivar cause_extension:
    """
    cause_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "causeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    cause_type: Optional[CauseTypeEnum2] = field(
        default=None,
        metadata={
            "name": "causeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    detailed_cause_type: Optional[DetailedCauseType] = field(
        default=None,
        metadata={
            "name": "detailedCauseType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    managed_cause: Optional[SituationRecordReference] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_causeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Impact:
    """
    An assessment of the impact that an event or operator action defined by the
    situation record has on the driving conditions.

    :ivar capacity_remaining: The ratio of current capacity to the
        normal (free flow) road capacity in the defined direction,
        expressed as a percentage. Capacity is the maximum number of
        vehicles that can pass a specified point on the road, in unit
        time given the specified conditions.
    :ivar number_of_lanes_restricted: The number of normally usable
        lanes on the carriageway which are now restricted either fully
        or partially (this may include the hard shoulder if it is
        normally available for operational use, e.g. in hard shoulder
        running schemes).
    :ivar number_of_operational_lanes: The number of usable lanes in the
        specified direction which remain fully operational (this may
        include the hard shoulder if it is being used as an operational
        lane).
    :ivar residual_lane_width: The width of lanes after any lane
        narrowing
    :ivar residual_road_width: The total width of the combined
        operational lanes in the specified direction.
    :ivar delays:
    :ivar impact_extension:
    """
    capacity_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacityRemaining",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    number_of_lanes_restricted: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLanesRestricted",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    number_of_operational_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfOperationalLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    residual_lane_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualLaneWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    residual_road_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualRoadWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    delays: Optional[Delays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    impact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_impactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class SituationRecord:
    """
    An identifiable versioned instance of a single record/element within a
    situation.

    :ivar situation_record_creation_reference: A unique alphanumeric
        reference (either an external reference or GUID) of the
        SituationRecord object (the first version of the record) that
        was created by the original supplier.
    :ivar situation_record_creation_time: The date/time that the
        SituationRecord object (the first version of the record) was
        created by the original supplier.
    :ivar situation_record_observation_time: The date/time that the
        information represented by the current version of the
        SituationRecord was observed by the original (potentially
        external) source of the information.
    :ivar situation_record_version_time: The date/time that this current
        version of the SituationRecord within the situation was written
        into the database of the supplier which is involved in the data
        exchange. Identity and version of record are defined by the
        class stereotype implementation.
    :ivar situation_record_first_supplier_version_time: The date/time
        that the current version of the Situation Record was written
        into the database of the original supplier in the supply chain.
    :ivar confidentiality_override: The extent to which the related
        information may be circulated, according to the recipient type.
        Recipients must comply with this confidentiality statement. This
        overrides any confidentiality defined for the situation as a
        whole in the header information.
    :ivar probability_of_occurrence: An assessment of the degree of
        likelihood that the reported event will occur.
    :ivar severity: The assessment of the impact (in terms of severity)
        that this element of the situation is having, or will have, on
        the traffic flow as perceived by the supplier.
    :ivar safety_related_message: Indicates, whether this
        SituationRecord specifies a safety related message according to
        Commission Delegated Regulation (EU) No 886/2013.
    :ivar source:
    :ivar validity:
    :ivar impact: Impact of the situation element
    :ivar cause:
    :ivar general_public_comment: A comment which may be freely
        distributed to the general public
    :ivar non_general_public_comment: A comment which should not be
        distributed to the general public.
    :ivar url_link:
    :ivar location_reference:
    :ivar information_manager_override: Organisation that manages the
        information content (is responsible for updates of this
        information) typically the organisation that first made the
        DATEX II publication of this content. This value overrides any
        value specified at a more general level.
    :ivar impact_on_opposite_direction: impact of the situation element
        on driving conditions in the opposite direction
    :ivar situation_record_extension:
    :ivar id:
    :ivar version:
    """
    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    confidentiality_override: Optional[ConfidentialityValueEnum2] = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum2] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    severity: Optional[SeverityEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    safety_related_message: Optional[bool] = field(
        default=None,
        metadata={
            "name": "safetyRelatedMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    information_manager_override: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManagerOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    impact_on_opposite_direction: Optional[Impact] = field(
        default=None,
        metadata={
            "name": "impactOnOppositeDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GenericSituationRecord(SituationRecord):
    """
    A generic SituationRecord for use when adding level B extensions at the
    SituationRecord level.

    :ivar generic_situation_record_name: The name of the
        GenericSituationRecord.
    :ivar generic_situation_record_extension:
    """
    generic_situation_record_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_genericSituationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class OperatorAction(SituationRecord):
    """
    Actions that an authorised operator can decide to implement to prevent or
    help correct dangerous or poor driving conditions, or any actions affecting
    normal operation of a road.

    :ivar action_origin: Indicates whether the actions to be undertaken
        by the operator are the result of an internal operation or
        external influence.
    :ivar action_plan_identifier: The identifier of the traffic
        management action plan to which this action relates.
    :ivar operator_action_status: The status of the defined operator
        action.
    :ivar operator_action_extension:
    """
    action_origin: Optional[OperatorActionOriginEnum2] = field(
        default=None,
        metadata={
            "name": "actionOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    action_plan_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionPlanIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    operator_action_status: Optional[OperatorActionStatusEnum2] = field(
        default=None,
        metadata={
            "name": "operatorActionStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    operator_action_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class ServiceInformation(SituationRecord):
    """
    Information about a service which may influence the behaviour of drivers
    and hence the characteristics of the traffic flow.
    """
    service_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_serviceInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Situation:
    """An identifiable instance of a traffic/travel situation comprising one or
    more traffic/travel circumstances which are linked by one or more causal
    relationships.

    Each traffic/travel circumstance is represented by a Situation
    Record.

    :ivar overall_severity: The overall assessment of the impact (in
        terms of severity) that the situation as a whole is having, or
        will have, on the traffic flow as perceived by the supplier.
    :ivar situation_version_time: The date/time that this current
        version of the Situation was written into the database of the
        supplier which is involved in the data exchange. Identity and
        version of the situation are defined by the class stereotype
        implementation.
    :ivar header_information:
    :ivar situation_record: Details of the Situation
    :ivar related_situation: Reference to related situations via unique
        identifiers.
    :ivar information_manager: Organisation that manages the information
        content (is responsible for updates of this information)
        typically the organisation that first made the DATEX II
        publication of this content.
    :ivar situation_summary: A SituationRecord that provides a summary
        of the information described by the corresponding Situation,
        i.e. a superset of at least the location and validity
        information of all (other) SituationRecords in this Situation.
    :ivar situation_extension:
    :ivar id:
    """
    overall_severity: Optional[SeverityEnum2] = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    situation_record: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    related_situation: List[SituationReference] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    information_manager: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManager",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_summary: Optional[SituationRecord] = field(
        default=None,
        metadata={
            "name": "situationSummary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TrafficElement(SituationRecord):
    """
    An event which is not planned by the traffic operator, which is affecting,
    or has the potential to affect traffic flow.

    :ivar traffic_constriction_type: The type of constriction to which
        traffic is subjected as a result of an unplanned event
    :ivar traffic_element_extension:
    """
    traffic_constriction_type: Optional[TrafficConstrictionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "trafficConstrictionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class AbnormalTraffic(TrafficElement):
    """
    A traffic condition which is not normal.

    :ivar abnormal_traffic_type: A characterization of the nature of
        abnormal traffic flow, i.e. specifically relating to the nature
        of the traffic movement, implying a level of service.
    :ivar number_of_vehicles_waiting: The number of vehicles waiting in
        a queue.
    :ivar queue_length: The length of a queue or the average length of
        queues in separate lanes due to a situation.
    :ivar relative_traffic_flow: Assessment of the traffic flow
        conditions relative to normally expected conditions at this
        date/time.
    :ivar traffic_flow_characteristics: The consistency (steadiness) of
        the traffic flow.
    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar abnormal_traffic_extension:
    """
    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum2] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    number_of_vehicles_waiting: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehiclesWaiting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    queue_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "queueLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    relative_traffic_flow: Optional[RelativeTrafficFlowEnum2] = field(
        default=None,
        metadata={
            "name": "relativeTrafficFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    traffic_flow_characteristics: Optional[TrafficFlowCharacteristicsEnum2] = field(
        default=None,
        metadata={
            "name": "trafficFlowCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum2] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    abnormal_traffic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_abnormalTrafficExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Accident(TrafficElement):
    """Accidents are events where one or more vehicles are involved in
    collisions or in leaving the roadway.

    These include collisions between vehicles or with other road users
    or obstacles.

    :ivar accident_cause: A descriptor indicating the most significant
        factor causing an accident.
    :ivar accident_type: A characterization of the nature of the
        accident.
    :ivar collision_type: Identifies a type of collision
    :ivar total_number_of_people_involved: The total number of people
        that are involved.
    :ivar total_number_of_vehicles_involved: The total number of
        vehicles that are involved.
    :ivar vehicle_involved: The vehicle involved in the accident.
    :ivar group_of_vehicles_involved:
    :ivar group_of_people_involved:
    :ivar accident_extension:
    """
    accident_cause: Optional[AccidentCauseEnum2] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    accident_type: List[AccidentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    collision_type: Optional[CollisionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "collisionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    vehicle_involved: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    group_of_vehicles_involved: List[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Activity(TrafficElement):
    """
    Deliberate human action external to the traffic stream or roadway which
    could disrupt traffic.

    :ivar mobility_of_activity: Mobility of the activity.
    :ivar activity_extension:
    """
    mobility_of_activity: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfActivity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_activityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Conditions(TrafficElement):
    """
    Any conditions which have the potential to degrade normal driving
    conditions.

    :ivar driving_condition_type: Description of the driving conditions
        at the specified location.
    :ivar conditions_extension:
    """
    driving_condition_type: Optional[DrivingConditionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class EquipmentOrSystemFault(TrafficElement):
    """
    Equipment or system which is faulty, malfunctioning or not in a fully
    operational state that may be of interest or concern to road operators and
    road users.

    :ivar equipment_or_system_fault_type: Failure, malfunction or non
        operational condition of equipment or system.
    :ivar faulty_equipment_or_system_type: The type of equipment or
        system which is faulty, malfunctioning or not in a fully
        operational state.
    :ivar equipment_or_system_fault_extension:
    """
    equipment_or_system_fault_type: Optional[EquipmentOrSystemFaultTypeEnum2] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    faulty_equipment_or_system_type: Optional[EquipmentOrSystemTypeEnum2] = field(
        default=None,
        metadata={
            "name": "faultyEquipmentOrSystemType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    equipment_or_system_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class NetworkManagement(OperatorAction):
    """
    Network management action which is applicable to the road network and its
    users.

    :ivar compliance_option: Defines whether the network management
        instruction or the control resulting from a network management
        action is advisory or mandatory.
    :ivar applicable_for_traffic_direction: The ultimate traffic
        direction to which the network management is applicable.
    :ivar applicable_for_traffic_type: The type of traffic to which the
        network management is applicable.
    :ivar places_at_which_applicable: Places, in generic terms, at which
        the network management applies.
    :ivar automatically_initiated: Defines whether the network
        management is initiated by an automatic system.
    :ivar for_vehicles_with_characteristics_of: The characteristics of
        those vehicles for which the network management is applicable.
    :ivar network_management_extension:
    """
    compliance_option: Optional[ComplianceOptionEnum2] = field(
        default=None,
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    applicable_for_traffic_direction: List[DirectionEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    applicable_for_traffic_type: List[TrafficTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    places_at_which_applicable: List[PlacesEnum2] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    automatically_initiated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Obstruction(TrafficElement):
    """
    Any stationary or moving obstacle of a physical nature (e.g. obstacles or
    vehicles from an earlier accident, shed loads on carriageway, rock fall,
    abnormal or dangerous loads, or animals etc.) which could disrupt or
    endanger traffic.

    :ivar number_of_obstructions: The number of obstructions that are
        partly or wholly blocking the road.
    :ivar mobility_of_obstruction: The mobility of the obstruction.
    :ivar obstruction_extension:
    """
    number_of_obstructions: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfObstructions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    mobility_of_obstruction: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfObstruction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class RoadOperatorServiceDisruption(ServiceInformation):
    """
    Details of disruption to normal road operator services.

    :ivar road_operator_service_disruption_type: The type of road
        operator service which is disrupted.
    :ivar road_operator_service_disruption_extension:
    """
    road_operator_service_disruption_type: List[RoadOperatorServiceDisruptionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadOperatorServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class RoadsideAssistance(OperatorAction):
    """
    Details of road side assistance required or being given.

    :ivar roadside_assistance_type: Indicates the nature of the road
        side assistance that will be, is or has been provided.
    :ivar roadside_assistance_extension:
    """
    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class Roadworks(OperatorAction):
    """
    Road maintenance, installation and construction activities, works in the
    road, or other construction or maintenance actions that may affect normal
    operation of a road.

    :ivar public_transport_alternative: Describes an available public
        transport alternative to the normal route
    :ivar roadworks_duration_classification: Indicates in general terms
        the expected duration of the roadworks.
    :ivar roadworks_identifier: An external identifier for the roadworks
    :ivar roadworks_scale: Grade of complexity of the roadworks
        according to the responsible road operator. For example
        determined by size, duration and/or traffic disruption.
    :ivar under_traffic: Indicates that the road section where the
        roadworks are located is under traffic or not under traffic.
        'True' indicates the road is under traffic.
    :ivar urgent_roadworks: Indication of whether the roadworks are
        considered to be urgent whereby emergency work is being, or
        needs to be, undertaken to mitigate safety concerns. 'True'
        indicates they are urgent.
    :ivar mobility:
    :ivar subjects:
    :ivar maintenance_vehicles:
    :ivar roadworks_extension:
    """
    public_transport_alternative: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "publicTransportAlternative",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    roadworks_duration_classification: Optional[RoadworksDurationEnum2] = field(
        default=None,
        metadata={
            "name": "roadworksDurationClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    roadworks_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadworksIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    roadworks_scale: Optional[RoadworksScaleEnum2] = field(
        default=None,
        metadata={
            "name": "roadworksScale",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    under_traffic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "underTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    urgent_roadworks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "urgentRoadworks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    mobility: Optional[Mobility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    subjects: Optional[Subjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    maintenance_vehicles: Optional[MaintenanceVehicles] = field(
        default=None,
        metadata={
            "name": "maintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    roadworks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class ServiceDisruption(ServiceInformation):
    """
    Details of disruption to normal services which may include roadside
    services such as those available at designated service areas, or any other
    relevant services such as nearby parking.

    :ivar service_disruption_type: The type of service which is
        disrupted.
    :ivar service_disruption_extension:
    """
    service_disruption_type: List[ServiceDisruptionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "serviceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_serviceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class SituationPublication(PayloadPublication):
    """
    A publication containing zero or more traffic/travel situations.
    """
    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class TransitInformation(ServiceInformation):
    """The availability of transit services and information relating to their
    departures.

    This is limited to those transit services which are of direct
    relevance to road users, e.g. connecting rail or ferry services.

    :ivar journey_destination: Indicates the stated termination point of
        the transit journey.
    :ivar journey_origin: Indicates the stated starting point of the
        transit journey.
    :ivar journey_reference: Indicates a transit service journey number.
    :ivar transit_service_information: Information about transit
        services.
    :ivar transit_service_type: The type of transit service to which the
        information relates.
    :ivar scheduled_departure_time: Indicates the timetabled departure
        time of a transit service for a specified location.
    :ivar transit_information_extension:
    """
    journey_destination: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    journey_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    journey_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "journeyReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    transit_service_information: Optional[TransitServiceInformationEnum2] = field(
        default=None,
        metadata={
            "name": "transitServiceInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    transit_service_type: Optional[TransitServiceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "transitServiceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    scheduled_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "scheduledDepartureTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    transit_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_transitInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class AnimalPresenceObstruction(Obstruction):
    """
    An obstruction on the road resulting from the presence of animals.

    :ivar alive: Indicates whether the identified animals are dead
        (immobile) or alive (potentially mobile).
    :ivar animal_presence_type: Indicates the nature of animals present
        on or near the roadway.
    :ivar animal_presence_obstruction_extension:
    """
    alive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    animal_presence_type: Optional[AnimalPresenceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class AuthorityOperation(Activity):
    """
    Authority initiated operation or activity that could disrupt traffic.

    :ivar authority_operation_type: Type of authority initiated
        operation or activity that could disrupt traffic.
    :ivar authority_operation_extension:
    """
    authority_operation_type: Optional[AuthorityOperationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    authority_operation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class ConstructionWorks(Roadworks):
    """
    Roadworks involving the construction of new infrastructure.

    :ivar construction_work_type: The type of construction work being
        performed.
    :ivar construction_works_extension:
    """
    construction_work_type: Optional[ConstructionWorkTypeEnum2] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    construction_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class DisturbanceActivity(Activity):
    """
    Deliberate human action of either a public disorder nature or of a
    situation alert type which could disrupt traffic.

    :ivar disturbance_activity_type: Includes all situations of a public
        disorder type or of an alert type, with potential to disrupt
        traffic.
    :ivar disturbance_activity_extension:
    """
    disturbance_activity_type: Optional[DisturbanceActivityTypeEnum2] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    disturbance_activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class EnvironmentalObstruction(Obstruction):
    """
    An obstruction on the road resulting from an environmental cause.

    :ivar depth: The depth of flooding or of snow on the road.
    :ivar environmental_obstruction_type: Characterization of an
        obstruction on the road resulting from an environmental cause.
    :ivar environmental_obstruction_extension:
    """
    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    environmental_obstruction_type: Optional[EnvironmentalObstructionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class GeneralInstructionOrMessageToRoadUsers(NetworkManagement):
    """
    General instruction and/or message that is issued by the network/road
    operator which is applicable to drivers and sometimes passengers.

    :ivar general_instruction_to_road_users_type: General instruction
        that is issued by the network/road operator which is applicable
        to drivers and sometimes passengers.
    :ivar general_message_to_road_users: General message that is issued
        by the network/road operator which is applicable to drivers and
        sometimes passengers, e.g. details about an amber alert (missing
        or abducted child alert).
    :ivar general_instruction_or_message_to_road_users_extension:
    """
    general_instruction_to_road_users_type: Optional[GeneralInstructionToRoadUsersTypeEnum2] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_message_to_road_users: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "generalMessageToRoadUsers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_instruction_or_message_to_road_users_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_generalInstructionOrMessageToRoadUsersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class GeneralNetworkManagement(NetworkManagement):
    """Network management action that is instigated either manually or
    automatically by the network/road operator.

    Compliance with any resulting control may be advisory or mandatory.

    :ivar general_network_management_type: The type of traffic
        management action instigated by the network/road operator.
    :ivar traffic_manually_directed_by: Type of person that is manually
        directing traffic (applicable if generalNetworkManagementType is
        set to "trafficBeingManuallyDirected").
    :ivar general_network_management_extension:
    """
    general_network_management_type: Optional[GeneralNetworkManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    traffic_manually_directed_by: Optional[PersonCategoryEnum2] = field(
        default=None,
        metadata={
            "name": "trafficManuallyDirectedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_generalNetworkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class GeneralObstruction(Obstruction):
    """
    Any stationary or moving obstacle of a physical nature, other than of an
    animal, vehicle, environmental, or damaged equipment nature.

    :ivar obstruction_type: Characterization of the type of general
        obstruction.
    :ivar group_of_people_involved:
    :ivar general_obstruction_extension:
    """
    obstruction_type: List[ObstructionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class InfrastructureDamageObstruction(Obstruction):
    """
    An obstruction on the road resulting from the failure or damage of
    infrastructure on, under, above or close to the road.

    :ivar infrastructure_damage_type: Characterization of an obstruction
        on the road resulting from the failure or damage of
        infrastructure on, under, above or close to the road.
    :ivar infrastructure_damage_obstruction_extension:
    """
    infrastructure_damage_type: Optional[InfrastructureDamageTypeEnum2] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    infrastructure_damage_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_infrastructureDamageObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class MaintenanceWorks(Roadworks):
    """
    Roadworks involving the maintenance or installation of infrastructure.

    :ivar road_maintenance_type: The type of road maintenance or
        installation work at the specified location.
    :ivar maintenance_works_extension:
    """
    road_maintenance_type: List[RoadMaintenanceTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    maintenance_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class PoorEnvironmentConditions(Conditions):
    """
    Any environmental conditions which may be affecting the driving conditions
    on the road.

    :ivar poor_environment_type: The type of environment condition which
        is affecting driving conditions.
    :ivar precipitation_detail:
    :ivar visibility:
    :ivar pollution:
    :ivar temperature:
    :ivar wind:
    :ivar humidity:
    :ivar pressure:
    :ivar poor_environment_conditions_extension:
    """
    poor_environment_type: List[PoorEnvironmentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    pollution: Optional[Pollution] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    pressure: Optional[Pressure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class PublicEvent(Activity):
    """
    Organised public event which could disrupt traffic.

    :ivar public_event_type: Type of public event which could disrupt
        traffic.
    :ivar venue_name: Name of the venue at which the public event is
        being held
    :ivar public_event_extension:
    """
    public_event_type: Optional[PublicEventTypeEnum2] = field(
        default=None,
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    venue_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "venueName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    public_event_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_publicEventExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class ReroutingManagement(NetworkManagement):
    """
    Rerouting management action that is issued by the network/road operator.

    :ivar rerouting_management_type: Type of rerouting management action
        instigated by operator.
    :ivar rerouting_itinerary_description: A description of the
        rerouting itinerary.
    :ivar signed_rerouting: Indication of whether the rerouting is
        signed.
    :ivar alternative_route_identifier: Identity used on signs to
        identify the alternative route, typically a very short sequence
        of letters and/or digits
    :ivar entry: The specified entry on to another road at which the
        alternative route commences.
    :ivar exit: The specified exit from the normal route/road at which
        the alternative route commences.
    :ivar road_or_junction_number: The intersecting road or the junction
        at which the alternative route commences.
    :ivar alternative_route: The definition of the alternative route
        (rerouting) specified as an ordered set of locations (itinerary)
        which may be specific to one or more defined destinations.
    :ivar destination: The destination of the rerouting. Use this direct
        property when there is no detailed Itinerary available.
    :ivar rerouting_management_extension:
    """
    rerouting_management_type: List[ReroutingManagementTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    rerouting_itinerary_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reroutingItineraryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    signed_rerouting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "signedRerouting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    alternative_route_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternativeRouteIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    entry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    exit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    road_or_junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadOrJunctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "max_length": 1024,
        }
    )
    alternative_route: List[Itinerary] = field(
        default_factory=list,
        metadata={
            "name": "alternativeRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    rerouting_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_reroutingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class RoadOrCarriagewayOrLaneManagement(NetworkManagement):
    """
    Road, carriageway or lane management action that is instigated by the
    network/road operator.

    :ivar road_or_carriageway_or_lane_management_type: Type of road,
        carriageway or lane management action instigated by operator.
    :ivar minimum_car_occupancy: The minimum number of persons required
        in a vehicle in order for it to be allowed to transit the
        specified road section.
    :ivar road_or_carriageway_or_lane_management_extension:
    """
    road_or_carriageway_or_lane_management_type: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    minimum_car_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumCarOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    road_or_carriageway_or_lane_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadOrCarriagewayOrLaneManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class RoadSurfaceConditions(Conditions):
    """Conditions of the road surface which may affect driving conditions.

    These may be related to the weather (e.g. ice, snow etc.) or to
    other conditions (e.g. oil, mud, leaves etc. on the road)
    """
    road_surface_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadSurfaceConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class SpeedManagement(NetworkManagement):
    """
    Speed management action that is instigated by the network/road operator.

    :ivar speed_management_type: Type of speed management action
        instigated by operator.
    :ivar temporary_speed_limit: Temporary limit defining the maximum
        advisory or mandatory speed of vehicles.
    :ivar speed_management_extension:
    """
    speed_management_type: Optional[SpeedManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    temporary_speed_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "temporarySpeedLimit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    speed_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_speedManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class VehicleObstruction(Obstruction):
    """
    An obstruction on the road caused by one or more vehicles.

    :ivar vehicle_obstruction_type: Characterization of an obstruction
        on the road caused by one or more vehicles.
    :ivar involved_vehicle_type: Type of vehicle involved
    :ivar vehicle_problem_cause: The component of the vehicle that has
        the problem
    :ivar obstructing_vehicle: The obstructing vehicle.
    :ivar vehicle_obstruction_extension:
    """
    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    involved_vehicle_type: Optional[VehicleTypeEnum2] = field(
        default=None,
        metadata={
            "name": "involvedVehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    vehicle_problem_cause: Optional[VehicleProblemCauseEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleProblemCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class WinterDrivingManagement(NetworkManagement):
    """
    Winter driving management action that is instigated by the network/road
    operator.

    :ivar winter_equipment_management_type: Type of winter equipment
        management action instigated by operator.
    :ivar winter_driving_management_extension:
    """
    winter_equipment_management_type: Optional[WinterEquipmentManagementTypeEnum2] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        }
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class NonWeatherRelatedRoadConditions(RoadSurfaceConditions):
    """
    Road surface conditions that are not related to the weather but which may
    affect driving conditions.

    :ivar non_weather_related_road_condition_type: The type of road
        conditions which are not related to the weather.
    :ivar non_weather_related_road_conditions_extension:
    """
    non_weather_related_road_condition_type: List[NonWeatherRelatedRoadConditionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_nonWeatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )


@dataclass
class WeatherRelatedRoadConditions(RoadSurfaceConditions):
    """
    Road surface conditions that are related to the weather which may affect
    the driving conditions, such as ice, snow or water.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar weather_related_road_conditions_extension:
    """
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        }
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        }
    )
