from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

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


class AccessCategoryEnum(Enum):
    """
    Specifies the category of the access.

    :cvar VEHICLE_ENTRANCE_AND_EXIT: An entrance and exit for vehicles.
    :cvar VEHICLE_ENTRANCE: An entrance for vehicles.
    :cvar VEHICLE_EXIT: An exit for vehicles.
    :cvar PEDESTRIAN_ENTRANCE_AND_EXIT: An entrance and exit for
        pedestrian.
    :cvar PEDESTRIAN_ENTRANCE: An entrance for pedestrian.
    :cvar PEDESTRIAN_EXIT: An exit for pedestrian.
    :cvar RENTAL_CAR_RETURN: An entrance to return rental cars.
    :cvar BICYCLES: An access for bicycles.
    :cvar EMERGENCY_EXIT: An exit that can be used by pedestrians in
        case of emergency (i.e. among others easy to access and signed).
    :cvar UNSPECIFIED: The category of this access is not specified any
        further.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    VEHICLE_ENTRANCE_AND_EXIT = "vehicleEntranceAndExit"
    VEHICLE_ENTRANCE = "vehicleEntrance"
    VEHICLE_EXIT = "vehicleExit"
    PEDESTRIAN_ENTRANCE_AND_EXIT = "pedestrianEntranceAndExit"
    PEDESTRIAN_ENTRANCE = "pedestrianEntrance"
    PEDESTRIAN_EXIT = "pedestrianExit"
    RENTAL_CAR_RETURN = "rentalCarReturn"
    BICYCLES = "bicycles"
    EMERGENCY_EXIT = "emergencyExit"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"


class AccessEquipmentEnum(Enum):
    """
    Specifies additional equipment for this access.

    :cvar BARRIER: There is a barrier on this entrance or exit. Usually
        access is granted through tickets, buttons or electronic
        systems.
    :cvar TRAFFIC_SIGNAL: There is a traffic signal installation
        controlling this access.
    :cvar TICKET_BUTTON_MACHINE: A machine at this entrance provides a
        parking ticket by pressing a button.
    :cvar TICKET_CARD_MACHINE: A machine at this entrance provides a
        parking ticket by inserting some payment or identity card.
    :cvar PAY_AND_EXIT_MACHINE: A machine at this exit enables payment
        directly by inserting a payment or identity card.
    :cvar OTHER: Other.
    """
    BARRIER = "barrier"
    TRAFFIC_SIGNAL = "trafficSignal"
    TICKET_BUTTON_MACHINE = "ticketButtonMachine"
    TICKET_CARD_MACHINE = "ticketCardMachine"
    PAY_AND_EXIT_MACHINE = "payAndExitMachine"
    OTHER = "other"


class AccessibilityEnum(Enum):
    """
    Special forms of accessibility, easements and marking for handicapped
    people.

    :cvar BARRIER_FREE_ACCESSIBLE: Accessible without any steps or other
        barriers. This is not as strong as handicappedAccessible.
    :cvar HANDICAPPED_ACCESSIBLE: Accessible for handicapped people.
        Wheelchair accessible is a special form of it.
    :cvar WHEEL_CHAIR_ACCESSIBLE: Accessible by people in a wheelchair.
    :cvar HANDICAPPED_EASEMENTS: There are special easements for
        handicapped people, like handrails or handicapped-friendly
        furniture.
    :cvar ORIENTATION_SYSTEM_FOR_BLIND_PEOPLE: There is some orientation
        system, which helps blind or visually impaired people. Examples
        might be some acoustic system or tactile paving.
    :cvar HANDICAPPED_MARKED: There is a visible mark for the privilege
        of handicapped or disabled people (e.g. a wheelchair symbol).
    :cvar NONE_VALUE: No form of special accessibility, i.e. usually not
        convenient for handicapped people, e.g. because of steps or
        barriers.
    :cvar UNKNOWN: It is unknown, whether there is a special form of
        accessibility.
    :cvar OTHER: Other.
    """
    BARRIER_FREE_ACCESSIBLE = "barrierFreeAccessible"
    HANDICAPPED_ACCESSIBLE = "handicappedAccessible"
    WHEEL_CHAIR_ACCESSIBLE = "wheelChairAccessible"
    HANDICAPPED_EASEMENTS = "handicappedEasements"
    ORIENTATION_SYSTEM_FOR_BLIND_PEOPLE = "orientationSystemForBlindPeople"
    HANDICAPPED_MARKED = "handicappedMarked"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"


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


class AccidentTypeEnum(Enum):
    """
    Collection of descriptive terms for types of accidents.

    :cvar ACCIDENT: Accidents are situations in which one or more
        vehicles lose control and do not recover.  They include
        collisions between vehicle(s) or other road user(s), between
        vehicle(s) and fixed obstacle(s), or they result from a vehicle
        running off the road.
    :cvar ACCIDENT_INVOLVING_BICYCLES: Includes all accidents involving
        at least one bicycle.
    :cvar ACCIDENT_INVOLVING_BUSES: Includes all accidents involving at
        least one passenger vehicle.
    :cvar ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS: Includes all accidents
        involving at least one vehicle believed to be carrying
        materials, which could present an additional hazard to road
        users.
    :cvar ACCIDENT_INVOLVING_HEAVY_LORRIES: Includes all accidents
        involving at least one heavy goods vehicle.
    :cvar ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE: Includes all
        accidents involving at least one mass transit vehicle.
    :cvar ACCIDENT_INVOLVING_MOPEDS: Includes all accidents involving at
        least one moped.
    :cvar ACCIDENT_INVOLVING_MOTORCYCLES: Includes all accidents
        involving at least one motorcycle.
    :cvar ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL: Accident involving
        radioactive material.
    :cvar ACCIDENT_INVOLVING_TRAIN: Includes all accidents involving
        collision with a train.
    :cvar CHEMICAL_SPILLAGE_ACCIDENT: Includes all situations resulting
        in a spillage of chemicals on the carriageway.
    :cvar COLLISION: Collision of vehicle with another object of
        unspecified type.
    :cvar COLLISION_WITH_ANIMAL: Collision of vehicle with one or more
        animals.
    :cvar COLLISION_WITH_OBSTRUCTION: Collision of vehicle with an
        object of a stationary nature.
    :cvar COLLISION_WITH_PERSON: Collision of vehicle with one or more
        pedestrians.
    :cvar EARLIER_ACCIDENT: An earlier reported accident that is causing
        disruption to traffic or is resulting in further accidents.
    :cvar FUEL_SPILLAGE_ACCIDENT: Includes all situations resulting in a
        spillage of fuel on the carriageway.
    :cvar HEAD_ON_COLLISION: Collision of vehicle with another vehicle
        head on.
    :cvar HEAD_ON_OR_SIDE_COLLISION: Collision of vehicle with another
        vehicle either head on or sideways.
    :cvar JACKKNIFED_ARTICULATED_LORRY: Includes all situations
        resulting in a heavy goods vehicle folding together in an
        accidental skidding movement on the carriageway.
    :cvar JACKKNIFED_CARAVAN: Includes all situations resulting in a
        vehicle and caravan folding together in an accidental skidding
        movement on the carriageway.
    :cvar JACKKNIFED_TRAILER: Includes all situations resulting in a
        vehicle and trailer folding together in an accidental skidding
        movement on the carriageway.
    :cvar MULTIPLE_VEHICLE_COLLISION: Multiple vehicles involved in a
        collision.
    :cvar MULTIVEHICLE_ACCIDENT: Includes all accidents involving three
        or more vehicles.
    :cvar OIL_SPILLAGE_ACCIDENT: Includes all situations resulting in a
        spillage of oil on the carriageway.
    :cvar OVERTURNED_HEAVY_LORRY: Includes all situations resulting in
        the overturning of a heavy goods vehicle on the carriageway.
    :cvar OVERTURNED_TRAILER: Includes all situations resulting in the
        overturning of a trailer.
    :cvar OVERTURNED_VEHICLE: Includes all situations resulting in the
        overturning of a vehicle (of unspecified type) on the
        carriageway.
    :cvar REAR_COLLISION: Includes all accidents where one or more
        vehicles have collided with the rear of one or more other
        vehicles.
    :cvar SECONDARY_ACCIDENT: Includes all situations resulting from
        vehicles avoiding or being distracted by earlier accidents.
    :cvar SERIOUS_ACCIDENT: Includes all accidents believed to involve
        fatality or injury expected to require overnight
        hospitalisation.
    :cvar SIDE_COLLISION: Includes all accidents where one or more
        vehicles have collided with the side of one or more other
        vehicles.
    :cvar VEHICLE_OFF_ROAD: Includes all accidents where one or more
        vehicles have left the roadway.
    :cvar VEHICLE_SPUN_AROUND: Includes all accidents where a vehicle
        has skidded and has come to rest not facing its intended line of
        travel.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ACCIDENT = "accident"
    ACCIDENT_INVOLVING_BICYCLES = "accidentInvolvingBicycles"
    ACCIDENT_INVOLVING_BUSES = "accidentInvolvingBuses"
    ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS = "accidentInvolvingHazardousMaterials"
    ACCIDENT_INVOLVING_HEAVY_LORRIES = "accidentInvolvingHeavyLorries"
    ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE = "accidentInvolvingMassTransitVehicle"
    ACCIDENT_INVOLVING_MOPEDS = "accidentInvolvingMopeds"
    ACCIDENT_INVOLVING_MOTORCYCLES = "accidentInvolvingMotorcycles"
    ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL = "accidentInvolvingRadioactiveMaterial"
    ACCIDENT_INVOLVING_TRAIN = "accidentInvolvingTrain"
    CHEMICAL_SPILLAGE_ACCIDENT = "chemicalSpillageAccident"
    COLLISION = "collision"
    COLLISION_WITH_ANIMAL = "collisionWithAnimal"
    COLLISION_WITH_OBSTRUCTION = "collisionWithObstruction"
    COLLISION_WITH_PERSON = "collisionWithPerson"
    EARLIER_ACCIDENT = "earlierAccident"
    FUEL_SPILLAGE_ACCIDENT = "fuelSpillageAccident"
    HEAD_ON_COLLISION = "headOnCollision"
    HEAD_ON_OR_SIDE_COLLISION = "headOnOrSideCollision"
    JACKKNIFED_ARTICULATED_LORRY = "jackknifedArticulatedLorry"
    JACKKNIFED_CARAVAN = "jackknifedCaravan"
    JACKKNIFED_TRAILER = "jackknifedTrailer"
    MULTIPLE_VEHICLE_COLLISION = "multipleVehicleCollision"
    MULTIVEHICLE_ACCIDENT = "multivehicleAccident"
    OIL_SPILLAGE_ACCIDENT = "oilSpillageAccident"
    OVERTURNED_HEAVY_LORRY = "overturnedHeavyLorry"
    OVERTURNED_TRAILER = "overturnedTrailer"
    OVERTURNED_VEHICLE = "overturnedVehicle"
    REAR_COLLISION = "rearCollision"
    SECONDARY_ACCIDENT = "secondaryAccident"
    SERIOUS_ACCIDENT = "seriousAccident"
    SIDE_COLLISION = "sideCollision"
    VEHICLE_OFF_ROAD = "vehicleOffRoad"
    VEHICLE_SPUN_AROUND = "vehicleSpunAround"
    OTHER = "other"


class AlertCDirectionEnum(Enum):
    """The direction of traffic flow concerned by a situation or traffic data.

    In ALERT-C the positive (resp. negative) direction corresponds to
    the positive offset direction within the RDS location table.

    :cvar BOTH: Indicates that both directions of traffic flow are
        affected by the situation or relate to the traffic data.
    :cvar NEGATIVE: The direction of traffic flow concerned by a
        situation or traffic data. In ALERT-C the negative direction
        corresponds to the negative offset direction within the RDS
        location table.
    :cvar POSITIVE: The direction of traffic flow concerned by a
        situation or traffic data. In ALERT-C the positive direction
        corresponds to the positive offset direction within the RDS
        location table.
    :cvar UNKNOWN: Unknown direction.
    """
    BOTH = "both"
    NEGATIVE = "negative"
    POSITIVE = "positive"
    UNKNOWN = "unknown"


class AnimalPresenceTypeEnum(Enum):
    """
    Types of animal presence.

    :cvar ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to animals
        on the roadway.
    :cvar HERD_OF_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to a
        herd of animals on the roadway.
    :cvar LARGE_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to
        large animals on the roadway.
    """
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    HERD_OF_ANIMALS_ON_THE_ROAD = "herdOfAnimalsOnTheRoad"
    LARGE_ANIMALS_ON_THE_ROAD = "largeAnimalsOnTheRoad"


class AreaOfInterestEnum(Enum):
    """
    Types of areas of interest.

    :cvar CONTINENT_WIDE: Area of the whole European continent.
    :cvar NATIONAL: Whole area of the specific country.
    :cvar NEIGHBOURING_COUNTRIES: Area of countries which are
        neighbouring the one specified.
    :cvar NOT_SPECIFIED: Non specified area.
    :cvar REGIONAL: Area of the local region.
    """
    CONTINENT_WIDE = "continentWide"
    NATIONAL = "national"
    NEIGHBOURING_COUNTRIES = "neighbouringCountries"
    NOT_SPECIFIED = "notSpecified"
    REGIONAL = "regional"


class AuthorityOperationTypeEnum(Enum):
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
    """
    ACCIDENT_INVESTIGATION_WORK = "accidentInvestigationWork"
    BOMB_SQUAD_IN_ACTION = "bombSquadInAction"
    CIVIL_EMERGENCY = "civilEmergency"
    CUSTOMS_OPERATION = "customsOperation"
    JURIDICAL_RECONSTRUCTION = "juridicalReconstruction"
    POLICE_CHECK_POINT = "policeCheckPoint"
    POLICE_INVESTIGATION = "policeInvestigation"
    ROAD_OPERATOR_CHECK_POINT = "roadOperatorCheckPoint"
    SURVEY = "survey"
    TRANSPORT_OF_VIP = "transportOfVip"
    UNDEFINED_AUTHORITY_ACTIVITY = "undefinedAuthorityActivity"
    VEHICLE_INSPECTION_CHECK_POINT = "vehicleInspectionCheckPoint"
    VEHICLE_WEIGHING = "vehicleWeighing"
    WEIGH_IN_MOTION = "weighInMotion"
    OTHER = "other"


class AvailabilityEnum(Enum):
    """
    An enumeration which states if something is available or not.

    :cvar AVAILABLE: The element in question is available.
    :cvar NOT_AVAILABLE: The element in question is not available.
    :cvar UNKNOWN: There is no information about whether the element in
        question is available or not.
    """
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    UNKNOWN = "unknown"


class CarParkConfigurationEnum(Enum):
    """
    Types of configuration/layout of a car park.

    :cvar MULTI_STOREY: Parking is on multiple levels within a car park
        building.
    :cvar PARK_AND_RIDE: Car parking facility is associated with a park
        and ride service.
    :cvar SINGLE_LEVEL: Parking is on a single ground floor level.
    :cvar UNDERGROUND: Parking is on one or more floors below ground
        level.
    """
    MULTI_STOREY = "multiStorey"
    PARK_AND_RIDE = "parkAndRide"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"


class CarParkStatusEnum(Enum):
    """
    Collection of statuses which may be associated with car parks.

    :cvar CAR_PARK_CLOSED: The specified car park is closed.
    :cvar ALL_CAR_PARKS_FULL: All car parks are full within a specified
        area.
    :cvar CAR_PARK_FACILITY_FAULTY: The specified car parking facility
        is not operating normally.
    :cvar CAR_PARK_FULL: A specified car park is completely occupied.
    :cvar CAR_PARK_STATUS_UNKNOWN: The status of the specified car
        park(s) is unknown.
    :cvar ENOUGH_SPACES_AVAILABLE: Specified car parks have car-parking
        spaces available.
    :cvar MULTI_STORY_CAR_PARKS_FULL: Multi level car parks are fully
        occupied.
    :cvar NO_MORE_PARKING_SPACES_AVAILABLE: Specified car parks are
        fully occupied.
    :cvar NO_PARK_AND_RIDE_INFORMATION: No park and ride information
        will be available until the specified time.
    :cvar NO_PARKING_ALLOWED: No parking allowed until the specified
        time.
    :cvar NO_PARKING_INFORMATION_AVAILABLE: Car-parking information is
        not available until a specified time.
    :cvar NORMAL_PARKING_RESTRICTIONS_LIFTED: The parking restrictions
        that normally apply in the specified location have been
        temporarily lifted.
    :cvar ONLY_AFEW_SPACES_AVAILABLE: Specified car parks have 95% or
        greater occupancy.
    :cvar PARK_AND_RIDE_SERVICE_NOT_OPERATING: Park and ride services
        are not operating until the specified time.
    :cvar PARK_AND_RIDE_SERVICE_OPERATING: Park and ride services are
        operating until the specified time.
    :cvar SPECIAL_PARKING_RESTRICTIONS_IN_FORCE: Parking restrictions,
        other than those that normally apply, are in force in a
        specified area.
    """
    CAR_PARK_CLOSED = "carParkClosed"
    ALL_CAR_PARKS_FULL = "allCarParksFull"
    CAR_PARK_FACILITY_FAULTY = "carParkFacilityFaulty"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_STATUS_UNKNOWN = "carParkStatusUnknown"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    MULTI_STORY_CAR_PARKS_FULL = "multiStoryCarParksFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    NO_PARK_AND_RIDE_INFORMATION = "noParkAndRideInformation"
    NO_PARKING_ALLOWED = "noParkingAllowed"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    NORMAL_PARKING_RESTRICTIONS_LIFTED = "normalParkingRestrictionsLifted"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    PARK_AND_RIDE_SERVICE_NOT_OPERATING = "parkAndRideServiceNotOperating"
    PARK_AND_RIDE_SERVICE_OPERATING = "parkAndRideServiceOperating"
    SPECIAL_PARKING_RESTRICTIONS_IN_FORCE = "specialParkingRestrictionsInForce"


class CarriagewayEnum(Enum):
    """
    List of descriptors identifying specific carriageway details.

    :cvar CONNECTING_CARRIAGEWAY: On the connecting carriageway.
    :cvar ENTRY_SLIP_ROAD: On the entry slip road.
    :cvar EXIT_SLIP_ROAD: On the exit slip road.
    :cvar FLYOVER: On the flyover, i.e. the section of road passing over
        another.
    :cvar LEFT_HAND_FEEDER_ROAD: On the left hand feeder road.
    :cvar LEFT_HAND_PARALLEL_CARRIAGEWAY: On the left hand parallel
        carriageway.
    :cvar MAIN_CARRIAGEWAY: On the main carriageway.
    :cvar OPPOSITE_CARRIAGEWAY: On the opposite carriageway.
    :cvar PARALLEL_CARRIAGEWAY: On the adjacent parallel carriageway.
    :cvar RIGHT_HAND_FEEDER_ROAD: On the right hand feeder road.
    :cvar RIGHT_HAND_PARALLEL_CARRIAGEWAY: On the right hand parallel
        carriageway.
    :cvar ROUNDABOUT: On the roundabout.
    :cvar SERVICE_ROAD: On the adjacent service road.
    :cvar SLIP_ROADS: On the slip roads.
    :cvar UNDERPASS: On the underpass, i.e. the section of road passing
        under another.
    """
    CONNECTING_CARRIAGEWAY = "connectingCarriageway"
    ENTRY_SLIP_ROAD = "entrySlipRoad"
    EXIT_SLIP_ROAD = "exitSlipRoad"
    FLYOVER = "flyover"
    LEFT_HAND_FEEDER_ROAD = "leftHandFeederRoad"
    LEFT_HAND_PARALLEL_CARRIAGEWAY = "leftHandParallelCarriageway"
    MAIN_CARRIAGEWAY = "mainCarriageway"
    OPPOSITE_CARRIAGEWAY = "oppositeCarriageway"
    PARALLEL_CARRIAGEWAY = "parallelCarriageway"
    RIGHT_HAND_FEEDER_ROAD = "rightHandFeederRoad"
    RIGHT_HAND_PARALLEL_CARRIAGEWAY = "rightHandParallelCarriageway"
    ROUNDABOUT = "roundabout"
    SERVICE_ROAD = "serviceRoad"
    SLIP_ROADS = "slipRoads"
    UNDERPASS = "underpass"


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


class ChangedFlagEnum(Enum):
    """
    List of flags to indicate what has changed in an exchage.

    :cvar CATALOGUE: Catalogue has changed indicator.
    :cvar FILTER: Filter has changed indicator.
    """
    CATALOGUE = "catalogue"
    FILTER = "filter"


class ChargeTypeEnum(Enum):
    """
    Charge type.

    :cvar MINIMUM: Minimum price for the given interval.
    :cvar MAXIMUM: Maximum price for the given interval.
    :cvar ADDITIONAL_INTERVAL_PRICE: Price for all intervals following
        the first interval.
    :cvar SEASON_TICKET: Season ticket.
    :cvar TEMPORARY_PRICE: Temporary price.
    :cvar FIRST_INTERVAL_PRICE: Price for the first interval, e.g. the
        first hour. See also 'additional'.
    :cvar FREE_PARKING: Free Parking. Set charge to 0.
    :cvar FLAT: Flat fee.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    ADDITIONAL_INTERVAL_PRICE = "additionalIntervalPrice"
    SEASON_TICKET = "seasonTicket"
    TEMPORARY_PRICE = "temporaryPrice"
    FIRST_INTERVAL_PRICE = "firstIntervalPrice"
    FREE_PARKING = "freeParking"
    FLAT = "flat"
    UNKNOWN = "unknown"
    OTHER = "other"


class ChargingStationUsageTypeEnum(Enum):
    """
    Type of usage for electric charging station(s).

    :cvar ELECTRIC_VEHICLE: Charging of electric vehicles.
    :cvar MOTORHOME_OR_CARAVAN_SUPPLY: Supply for motorhomes or
        caravans.
    :cvar ELECTRIC_BIKE_OR_MOTORCYCLE: Charging of E-Bikes or
        E-Motorcycles.
    :cvar LORRY_POWER_CONSUMPTION: Supply for lorries with power
        consumption, e.g. for refrigerated goods transports.
    :cvar ELECTRICAL_DEVICES: Provides a plug for electrical devices
        (e.g. shaver, mobile phones, hair dryer, ...)
    :cvar OTHER: Other usage for the electric charging stations.
    """
    ELECTRIC_VEHICLE = "electricVehicle"
    MOTORHOME_OR_CARAVAN_SUPPLY = "motorhomeOrCaravanSupply"
    ELECTRIC_BIKE_OR_MOTORCYCLE = "electricBikeOrMotorcycle"
    LORRY_POWER_CONSUMPTION = "lorryPowerConsumption"
    ELECTRICAL_DEVICES = "electricalDevices"
    OTHER = "other"


class CodedReasonForSettingMessageEnum(Enum):
    """
    Coded reasons why a message has been selected for display on the sign.

    :cvar SITUATION: Message selected as the result of a situation
        occuring either on or off the road which may affect road users.
    :cvar OPERATOR_CREATED: Message selected by operator as the result
        of an unmanaged event or situation.
    :cvar TRAFFIC_MANAGEMENT: Message selected as part of the
        implementation of a traffic management action. This may or may
        not be part of a specific traffic management or diversion plan.
    :cvar TRAVEL_TIME: VMS is currently selected to display travel
        times.
    :cvar CAMPAIGN: VMS is currently selected to display a campaign
        message.
    :cvar DEFAULT: VMS is currently selected to display default
        information (e.g. time, date, temperature).
    """
    SITUATION = "situation"
    OPERATOR_CREATED = "operatorCreated"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"
    CAMPAIGN = "campaign"
    DEFAULT = "default"


class ColourEnum(Enum):
    """
    Colours.

    :cvar AMBER: The colour amber.
    :cvar BLUE: The colour blue.
    :cvar GREEN: The colour green.
    :cvar RED: The colour red.
    :cvar WHITE: The colour white.
    :cvar WHITE_YELLOW: The colour white-yellow.
    """
    AMBER = "amber"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    WHITE = "white"
    WHITE_YELLOW = "whiteYellow"


class CommentTypeEnum(Enum):
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
    :cvar LOCATION_DESCRIPTOR: A free text human oriented description of
        the location of the situation element defined by the
        SituationRecord.
    :cvar WARNING: A free text human oriented warning relating to the
        SituationRecord, such as advising the recipient that an advanced
        warning on VMS should be activated.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABNORMAL_LOAD_MOVEMENT_NOTE = "abnormalLoadMovementNote"
    DATA_PROCESSING_NOTE = "dataProcessingNote"
    DESCRIPTION = "description"
    INTERNAL_NOTE = "internalNote"
    LOCATION_DESCRIPTOR = "locationDescriptor"
    WARNING = "warning"
    OTHER = "other"


class ComparisonOperatorEnum(Enum):
    """
    Logical comparison operations.

    :cvar EQUAL_TO: Logical comparison operator of "equal to".
    :cvar GREATER_THAN: Logical comparison operator of "greater than".
    :cvar GREATER_THAN_OR_EQUAL_TO: Logical comparison operator of
        "greater than or equal to".
    :cvar LESS_THAN: Logical comparison operator of "less than".
    :cvar LESS_THAN_OR_EQUAL_TO: Logical comparison operator of "less
        than or equal to".
    """
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL_TO = "greaterThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"


class ComplianceOptionEnum(Enum):
    """
    Types of compliance.

    :cvar ADVISORY: Advisory compliance.
    :cvar MANDATORY: Mandatory compliance.
    """
    ADVISORY = "advisory"
    MANDATORY = "mandatory"


class ComputationMethodEnum(Enum):
    """
    Types of computational methods used in deriving data values for data sets.

    :cvar
        ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES:
        Arithmetic average of sample values based on a fixed number of
        samples.
    :cvar ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Arithmetic
        average of sample values in a time period.
    :cvar HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Harmonic average
        of sample values in a time period.
    :cvar MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD: Median of sample values
        taken over a time period.
    :cvar MOVING_AVERAGE_OF_SAMPLES: Moving average of sample values.
    """
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "arithmeticAverageOfSamplesInATimePeriod"
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "harmonicAverageOfSamplesInATimePeriod"
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"


class ConfidentialityValueEnum(Enum):
    """
    Values of confidentiality.

    :cvar INTERNAL_USE: For internal use only of the recipient
        organisation.
    :cvar NO_RESTRICTION: No restriction on usage.
    :cvar RESTRICTED_TO_AUTHORITIES: Restricted for use only by
        authorities.
    :cvar RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS: Restricted
        for use only by authorities and traffic operators.
    :cvar RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS:
        Restricted for use only by authorities, traffic operators and
        publishers (service providers).
    :cvar RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS:
        Restricted for use only by authorities, traffic operators,
        publishers (service providers) and variable message signs.
    """
    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = "restrictedToAuthoritiesAndTrafficOperators"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS = "restrictedToAuthoritiesTrafficOperatorsAndPublishers"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS = "restrictedToAuthoritiesTrafficOperatorsAndVms"


class ConstructionWorkTypeEnum(Enum):
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
    """
    BLASTING_WORK = "blastingWork"
    CONSTRUCTION_WORK = "constructionWork"
    DEMOLITION_WORK = "demolitionWork"
    ROAD_IMPROVEMENT_OR_UPGRADING = "roadImprovementOrUpgrading"
    ROAD_WIDENING_WORK = "roadWideningWork"


class CountryEnum(Enum):
    """
    List of countries.

    :cvar AT: Austria
    :cvar BE: Belgium
    :cvar BG: Bulgaria
    :cvar CH: Switzerland
    :cvar CS: Serbia and Montenegro
    :cvar CY: Cyprus
    :cvar CZ: Czech Republic
    :cvar DE: Germany
    :cvar DK: Denmark
    :cvar EE: Estonia
    :cvar ES: Spain
    :cvar FI: Finland
    :cvar FO: Faroe Islands
    :cvar FR: France
    :cvar GB: Great Britain
    :cvar GG: Guernsey
    :cvar GI: Gibraltar
    :cvar GR: Greece
    :cvar HR: Croatia
    :cvar HU: Hungary
    :cvar IE: Ireland
    :cvar IM: Isle Of Man
    :cvar IS_VALUE: Iceland
    :cvar IT: Italy
    :cvar JE: Jersey
    :cvar LI: Lichtenstein
    :cvar LT: Lithuania
    :cvar LU: Luxembourg
    :cvar LV: Latvia
    :cvar MA: Morocco
    :cvar MC: Monaco
    :cvar MK: Macedonia
    :cvar MT: Malta
    :cvar NL: Netherlands
    :cvar NO: Norway
    :cvar PL: Poland
    :cvar PT: Portugal
    :cvar RO: Romania
    :cvar SE: Sweden
    :cvar SI: Slovenia
    :cvar SK: Slovakia
    :cvar SM: San Marino
    :cvar TR: Turkey
    :cvar VA: Vatican City State
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AT = "at"
    BE = "be"
    BG = "bg"
    CH = "ch"
    CS = "cs"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DK = "dk"
    EE = "ee"
    ES = "es"
    FI = "fi"
    FO = "fo"
    FR = "fr"
    GB = "gb"
    GG = "gg"
    GI = "gi"
    GR = "gr"
    HR = "hr"
    HU = "hu"
    IE = "ie"
    IM = "im"
    IS_VALUE = "is"
    IT = "it"
    JE = "je"
    LI = "li"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    MA = "ma"
    MC = "mc"
    MK = "mk"
    MT = "mt"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    SE = "se"
    SI = "si"
    SK = "sk"
    SM = "sm"
    TR = "tr"
    VA = "va"
    OTHER = "other"


class CurrencyEnum(Enum):
    """Three letter code defining the currency according to ISO 4217 (e.g. EUR
    for Euro).

    This enumeration only contains European currencies including the US
    dollar.

    :cvar EUR: Euro
    :cvar ALL: Lek (Albania)
    :cvar AMD: Armeniam Dram
    :cvar AZN: Azerbaijanian Manat
    :cvar BAM: Convertible Mark (Bosnia and Herzogowina)
    :cvar BGN: Bulgarian Lev
    :cvar BYR: Belarussian Ruble
    :cvar CHF: Swiss Franc
    :cvar CZK: Czech Koruna
    :cvar DKK: Danish Krone
    :cvar GBP: Pound Sterling
    :cvar GEL: Lari (Georgia)
    :cvar HRK: Croatian Kuna
    :cvar HUF: Forint (Hungary)
    :cvar ISK: Iceland Krona
    :cvar LTL: Litas (Lithuania)
    :cvar MDL: Moldovan Leu
    :cvar MKD: Denar
    :cvar NOK: Norwegian Krone
    :cvar PLN: Zloty
    :cvar RON: New Romanian Leu
    :cvar RSD: Serbian Dinar
    :cvar RUB: Russian Ruble
    :cvar SEK: Swedish Krona
    :cvar TRY_VALUE: Turkish Lira
    :cvar UAH: Hryvnia (Ukraine)
    :cvar USD: US Dollar
    :cvar OTHER: Another currency.
    """
    EUR = "eur"
    ALL = "all"
    AMD = "amd"
    AZN = "azn"
    BAM = "bam"
    BGN = "bgn"
    BYR = "byr"
    CHF = "chf"
    CZK = "czk"
    DKK = "dkk"
    GBP = "gbp"
    GEL = "gel"
    HRK = "hrk"
    HUF = "huf"
    ISK = "isk"
    LTL = "ltl"
    MDL = "mdl"
    MKD = "mkd"
    NOK = "nok"
    PLN = "pln"
    RON = "ron"
    RSD = "rsd"
    RUB = "rub"
    SEK = "sek"
    TRY_VALUE = "try"
    UAH = "uah"
    USD = "usd"
    OTHER = "other"


class DangerousGoodsRegulationsEnum(Enum):
    """
    Types of dangerous goods regulations.

    :cvar ADR: European agreement on the international carriage of
        dangerous goods on road.
    :cvar IATA_ICAO: Regulations covering the international
        transportation of dangerous goods issued by the International
        Air Transport Association and the International Civil Aviation
        Organisation.
    :cvar IMO_IMDG: Regulations regarding the transportation of
        dangerous goods on ocean-going vessels issued by the
        International Maritime Organisation.
    :cvar RAILROAD_DANGEROUS_GOODS_BOOK: International regulations
        concerning the international carriage of dangerous goods by
        rail.
    """
    ADR = "adr"
    IATA_ICAO = "iataIcao"
    IMO_IMDG = "imoImdg"
    RAILROAD_DANGEROUS_GOODS_BOOK = "railroadDangerousGoodsBook"


class DayEnum(Enum):
    """
    Days of the week.

    :cvar MONDAY: Monday.
    :cvar TUESDAY: Tuesday.
    :cvar WEDNESDAY: Wednesday.
    :cvar THURSDAY: Thursday.
    :cvar FRIDAY: Friday.
    :cvar SATURDAY: Saturday.
    :cvar SUNDAY: Sunday.
    """
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class DelayBandEnum(Enum):
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
    """
    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = "betweenTenMinutesAndThirtyMinutes"
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"


class DelaysTypeEnum(Enum):
    """
    Course classifications of a delay.

    :cvar DELAYS: Delays on the road network as a result of any
        situation which causes hold-ups.
    :cvar DELAYS_OF_UNCERTAIN_DURATION: Delays on the road network whose
        predicted duration cannot be estimated.
    :cvar LONG_DELAYS: Delays on the road network of unusual severity.
    :cvar VERY_LONG_DELAYS: Delays on the road network of abnormally
        unusual severity.
    """
    DELAYS = "delays"
    DELAYS_OF_UNCERTAIN_DURATION = "delaysOfUncertainDuration"
    LONG_DELAYS = "longDelays"
    VERY_LONG_DELAYS = "veryLongDelays"


class DenyReasonEnum(Enum):
    """
    Reasons for denial of a request.

    :cvar UNKNOWN_REASON: Reason unknown.
    :cvar WRONG_CATALOGUE: Wrong catalogue specified.
    :cvar WRONG_FILTER: Wrong filter specified.
    :cvar WRONG_ORDER: Wrong order specified.
    :cvar WRONG_PARTNER: Wrong partner specified.
    """
    UNKNOWN_REASON = "unknownReason"
    WRONG_CATALOGUE = "wrongCatalogue"
    WRONG_FILTER = "wrongFilter"
    WRONG_ORDER = "wrongOrder"
    WRONG_PARTNER = "wrongPartner"


class DirectionCompassEnum(Enum):
    """
    Cardinal direction points of the compass.

    :cvar EAST: East.
    :cvar EAST_NORTH_EAST: East north east.
    :cvar EAST_SOUTH_EAST: East south east.
    :cvar NORTH: North.
    :cvar NORTH_EAST: North east.
    :cvar NORTH_NORTH_EAST: North north east.
    :cvar NORTH_NORTH_WEST: North north west.
    :cvar NORTH_WEST: North west.
    :cvar SOUTH: South.
    :cvar SOUTH_EAST: South east.
    :cvar SOUTH_SOUTH_EAST: South south east.
    :cvar SOUTH_SOUTH_WEST: South south west.
    :cvar SOUTH_WEST: South west.
    :cvar WEST: West.
    :cvar WEST_NORTH_WEST: West north west.
    :cvar WEST_SOUTH_WEST: West south west.
    """
    EAST = "east"
    EAST_NORTH_EAST = "eastNorthEast"
    EAST_SOUTH_EAST = "eastSouthEast"
    NORTH = "north"
    NORTH_EAST = "northEast"
    NORTH_NORTH_EAST = "northNorthEast"
    NORTH_NORTH_WEST = "northNorthWest"
    NORTH_WEST = "northWest"
    SOUTH = "south"
    SOUTH_EAST = "southEast"
    SOUTH_SOUTH_EAST = "southSouthEast"
    SOUTH_SOUTH_WEST = "southSouthWest"
    SOUTH_WEST = "southWest"
    WEST = "west"
    WEST_NORTH_WEST = "westNorthWest"
    WEST_SOUTH_WEST = "westSouthWest"


class DirectionEnum(Enum):
    """
    List of directions of travel.

    :cvar ALL_DIRECTIONS: All directions (where more than two are
        applicable) at this point on the road network.
    :cvar BOTH_WAYS: Both directions that are applicable at this point
        on the road network.
    :cvar CLOCKWISE: Clockwise.
    :cvar ANTICLOCKWISE: Anti-clockwise.
    :cvar INNER_RING: Inner ring direction.
    :cvar OUTER_RING: Outer ring direction.
    :cvar NORTH_BOUND: North bound general direction.
    :cvar NORTH_EAST_BOUND: North east bound general direction.
    :cvar EAST_BOUND: East bound general direction.
    :cvar SOUTH_EAST_BOUND: South east bound general direction.
    :cvar SOUTH_BOUND: South bound general direction.
    :cvar SOUTH_WEST_BOUND: South west bound general direction.
    :cvar WEST_BOUND: West bound general direction.
    :cvar NORTH_WEST_BOUND: North west bound general direction.
    :cvar INBOUND_TOWARDS_TOWN: Heading towards town centre direction of
        travel.
    :cvar OUTBOUND_FROM_TOWN: Heading out of or away from the town
        centre direction of travel.
    :cvar UNKNOWN: Direction is unknown.
    :cvar OPPOSITE: Opposite direction to the normal direction of flow
        at this point on the road network.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ALL_DIRECTIONS = "allDirections"
    BOTH_WAYS = "bothWays"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"
    INNER_RING = "innerRing"
    OUTER_RING = "outerRing"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    EAST_BOUND = "eastBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_BOUND = "southBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    NORTH_WEST_BOUND = "northWestBound"
    INBOUND_TOWARDS_TOWN = "inboundTowardsTown"
    OUTBOUND_FROM_TOWN = "outboundFromTown"
    UNKNOWN = "unknown"
    OPPOSITE = "opposite"
    OTHER = "other"


class DisturbanceActivityTypeEnum(Enum):
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


class DrivingConditionTypeEnum(Enum):
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
    """
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"


class ElaboratedDataFaultEnum(Enum):
    """
    Types of elaborated data faults.

    :cvar INTERMITTENT_DATA_VALUES: Data values are being produced at
        intermittent intervals which are not consitent with the expected
        reporting interval.
    :cvar NO_DATA_VALUES_AVAILABLE: No elaborated data values are
        currently available.
    :cvar SPURIOUS_UNRELIABLE_DATA_VALUES: Spurious or unreliable data
        values are being produced.
    :cvar UNSPECIFIED_OR_UNKNOWN_FAULT: An unspecified or unknown fault
        exists in the process which is generating elaborated data.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    INTERMITTENT_DATA_VALUES = "intermittentDataValues"
    NO_DATA_VALUES_AVAILABLE = "noDataValuesAvailable"
    SPURIOUS_UNRELIABLE_DATA_VALUES = "spuriousUnreliableDataValues"
    UNSPECIFIED_OR_UNKNOWN_FAULT = "unspecifiedOrUnknownFault"
    OTHER = "other"


class EnvironmentalObstructionTypeEnum(Enum):
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


class EquipmentOrSystemFaultTypeEnum(Enum):
    """
    Types of fault, malfunctioning or non operational conditions of equipment
    or systems.

    :cvar NOT_WORKING: Not working or functioning.
    :cvar OUT_OF_SERVICE: Out of service (usually for operational
        reasons).
    :cvar WORKING_INCORRECTLY: Working incorrectly.
    :cvar WORKING_INTERMITTENTLY: Working intermittently.
    """
    NOT_WORKING = "notWorking"
    OUT_OF_SERVICE = "outOfService"
    WORKING_INCORRECTLY = "workingIncorrectly"
    WORKING_INTERMITTENTLY = "workingIntermittently"


class EquipmentOrSystemTypeEnum(Enum):
    """
    Types of equipment and systems used to support the operation of the road
    network.

    :cvar ANPR_CAMERAS: Automatic number plate recognition cameras.
    :cvar AUTOMATED_TOLL_SYSTEM: Automated toll system.
    :cvar CCTV_CAMERAS: Closed-circuit television cameras.
    :cvar EMERGENCY_ROADSIDE_TELEPHONES: Emergency roadside telephones.
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
    :cvar TUNNEL_LIGHTS: Tunnel lights.
    :cvar TUNNEL_VENTILATION: Tunnel ventilation system.
    :cvar VARIABLE_MESSAGE_SIGNS: Variable message signs.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ANPR_CAMERAS = "anprCameras"
    AUTOMATED_TOLL_SYSTEM = "automatedTollSystem"
    CCTV_CAMERAS = "cctvCameras"
    EMERGENCY_ROADSIDE_TELEPHONES = "emergencyRoadsideTelephones"
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
    TUNNEL_LIGHTS = "tunnelLights"
    TUNNEL_VENTILATION = "tunnelVentilation"
    VARIABLE_MESSAGE_SIGNS = "variableMessageSigns"
    OTHER = "other"


class EquipmentTypeEnum(Enum):
    """
    Equipment available on the parking or parking space or grouped parking
    spaces.

    :cvar TOILET: Indicates, whether there are toilets available.
    :cvar SHOWER: Indicates, whether there are shower facilities
        available.
    :cvar INFORMATION_POINT: An information point with employees.
    :cvar INFORMATON_STELE: An unmanned information point.
    :cvar INTERNET_TERMINAL: Public internet terminal. Charges may be
        specified using the TariffsAndPayment section.
    :cvar INTERNET_WIRELESS: Public wireless internet. Specifying an
        amount would be the number of hotspots/access points. Charges
        may be specified using the TariffsAndPayment section.
    :cvar PAY_DESK: A possibility to pay for parking (with employees).
    :cvar PAYMENT_MACHINE: A parking ticket machine.
    :cvar CASH_MACHINE: Cash machine.
    :cvar VENDING_MACHINE: A vending machine for snacks, coffee etc.
        (without manpower).
    :cvar FAX_MACHINE_OR_SERVICE: A possibility to send and/or receive
        faxes.
    :cvar COPY_MACHINE_OR_SERVICE: A possibility to create copies of
        documents.
    :cvar SAFE_DEPOSIT: A possibility to store valuable possession in a
        safe way.
    :cvar LUGGAGE_LOCKER: Possibility to deposit luggage in a safe way.
    :cvar PUBLIC_PHONE: Indicates, whether there's a public telephone
        available.
    :cvar PUBLIC_COIN_PHONE: Indicates, whether there's a public
        telephone available that can be used with coins.
    :cvar PUBLIC_CARD_PHONE: Indicates, whether there's a public
        telephone available that can be used with a card.
    :cvar ELEVATOR: Indication of the availability of elevators.
    :cvar PICNIC_FACILITIES: Indication of whether any picnicking
        facilities, such as tables, chairs and shaded areas, are
        available.
    :cvar DUMPING_STATION: Possibility to get rid of sewerage
        (especially for motorhomes).
    :cvar FRESH_WATER: Possibility to get fresh water (e.g. for
        motorhomes) - toilets and showers etc. are not intended here.
    :cvar WASTE_DISPOSAL: Possibility to get rid of waste in a legal way
        (e.g. for truckers or motorhomes). Normal refuse bins are not
        intended here.
    :cvar REFUSE_BIN: Refuse bins for small amounts of garbage (see also
        'wasteDisposal').
    :cvar ICE_FREE_SCAFFOLD: A technical equipment to remove ice and
        snow from the roof of lorries.
    :cvar PLAYGROUND: A playground for children.
    :cvar ELECTRIC_CHARGING_STATION: For charging vehicles, motorhome
        supply etc. The 'numberOf...' attribute specifies the number of
        charging stations. You may specify the number of charging points
        and further information with component 'ElectricCharging'.
    :cvar BIKE_PARKING: Bike parking.
    :cvar TOLL_TERMINAL: A terminal, where toll charges can be paid
        manually (this does not mean a toll gate on the road)
    :cvar DEFIBRILLATOR: Medical equipment to provide first aid after
        heart attacks.
    :cvar FIRST_AID_EQUIPMENT: Equipment to support first aid on injured
        people. Note that 'defibrillator' is a separate literal.
    :cvar FIRE_HOSE: A hose for water transport in case of fire.
    :cvar FIRE_EXTINGIUSHER: Fire extinguisher
    :cvar FIRE_HYDRANT: Fire hydrant
    :cvar NONE_VALUE: None.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other equipment. Use
        'otherEquipmentOrServiceFacility' to specify it.
    """
    TOILET = "toilet"
    SHOWER = "shower"
    INFORMATION_POINT = "informationPoint"
    INFORMATON_STELE = "informatonStele"
    INTERNET_TERMINAL = "internetTerminal"
    INTERNET_WIRELESS = "internetWireless"
    PAY_DESK = "payDesk"
    PAYMENT_MACHINE = "paymentMachine"
    CASH_MACHINE = "cashMachine"
    VENDING_MACHINE = "vendingMachine"
    FAX_MACHINE_OR_SERVICE = "faxMachineOrService"
    COPY_MACHINE_OR_SERVICE = "copyMachineOrService"
    SAFE_DEPOSIT = "safeDeposit"
    LUGGAGE_LOCKER = "luggageLocker"
    PUBLIC_PHONE = "publicPhone"
    PUBLIC_COIN_PHONE = "publicCoinPhone"
    PUBLIC_CARD_PHONE = "publicCardPhone"
    ELEVATOR = "elevator"
    PICNIC_FACILITIES = "picnicFacilities"
    DUMPING_STATION = "dumpingStation"
    FRESH_WATER = "freshWater"
    WASTE_DISPOSAL = "wasteDisposal"
    REFUSE_BIN = "refuseBin"
    ICE_FREE_SCAFFOLD = "iceFreeScaffold"
    PLAYGROUND = "playground"
    ELECTRIC_CHARGING_STATION = "electricChargingStation"
    BIKE_PARKING = "bikeParking"
    TOLL_TERMINAL = "tollTerminal"
    DEFIBRILLATOR = "defibrillator"
    FIRST_AID_EQUIPMENT = "firstAidEquipment"
    FIRE_HOSE = "fireHose"
    FIRE_EXTINGIUSHER = "fireExtingiusher"
    FIRE_HYDRANT = "fireHydrant"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"


class FaultSeverityEnum(Enum):
    """
    Classification of the severity of faults.

    :cvar LOW: The fault is of low severity and has only limited impact
        on the usability of the equipment or the value of the data
        generated by the equipment.
    :cvar MEDIUM: The fault is of medium severity which will
        significantly limit the usability of the equipment or devalue
        the usefulness of the data generated by the equipment.
    :cvar HIGH: The fault is of high severity which will render the
        equipment unusable or any data generated by the equipment to be
        of no value.
    :cvar UNKNOWN: The fault is of unknown severity and hence its effect
        on the usability of the equipment or the usefulness of the data
        generated by the equipment can not be assessed.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class FuelType2Enum(Enum):
    """
    Fuel types that are currently not supported in FuelTypeEnum.

    :cvar ALL: All sort of fuel is accepted.
    :cvar PETROL95_OCTANE: Petrol with 95 octane.
    :cvar PETROL98_OCTANE: Petrol with 98 octane.
    :cvar PETROL_LEADED: Leaded petrol.
    :cvar PETROL_UNLEADED: Unleaded petrol.
    :cvar UNKNOWN: The sort of fuel is not known.
    :cvar OTHER: Other.
    """
    ALL = "all"
    PETROL95_OCTANE = "petrol95Octane"
    PETROL98_OCTANE = "petrol98Octane"
    PETROL_LEADED = "petrolLeaded"
    PETROL_UNLEADED = "petrolUnleaded"
    UNKNOWN = "unknown"
    OTHER = "other"


class FuelTypeEnum(Enum):
    """
    Type of fuel used by a vehicle.

    :cvar BATTERY: Battery.
    :cvar BIODIESEL: Biodiesel.
    :cvar DIESEL: Diesel.
    :cvar DIESEL_BATTERY_HYBRID: Diesel and battery hybrid.
    :cvar ETHANOL: Ethanol.
    :cvar HYDROGEN: Hydrogen.
    :cvar LIQUID_GAS: Liquid gas of any type including LPG.
    :cvar LPG: Liquid petroleum gas.
    :cvar METHANE: Methane gas.
    :cvar PETROL: Petrol.
    :cvar PETROL_BATTERY_HYBRID: Petrol and battery hybrid.
    """
    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    LPG = "lpg"
    METHANE = "methane"
    PETROL = "petrol"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"


class GeneralInstructionToRoadUsersTypeEnum(Enum):
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


class GroupOfParkingSitesStatusEnum(Enum):
    """
    The status of the group of parking sites (available spaces or not).

    :cvar ALL_PARKINGS_FULL: All parkings within the group are full.
    :cvar MULTI_STOREY_PARKINGS_FULL: All multi storey parkings within
        the group are full.
    :cvar NO_MORE_PARKING_SPACES_AVAILABLE: No more parking spaces
        available within the group.
    :cvar ENOUGH_SPACES_AVAILABLE: Enough spaces available within the
        group.
    :cvar UNKNOWN: The status of the group of parking sites is unknown.
    :cvar OTHER: Other.
    """
    ALL_PARKINGS_FULL = "allParkingsFull"
    MULTI_STOREY_PARKINGS_FULL = "multiStoreyParkingsFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    UNKNOWN = "unknown"
    OTHER = "other"


class GroupOfParkingSitesTypeEnum(Enum):
    """
    The type of this group of parking sites.

    :cvar PARKING_AREA: A parking area in urban environment, for example
        all parkings sites in the western centre.
    :cvar TRUCK_PARKING_PRIORITY_ZONE: This group is describing a truck
        parking priority zone according to the EU regulation.
    :cvar AGGREGATION_OF_INFORMATION: The main purpose of this group is
        to give summarized information of all encapsulated parking sites
        (e.g. number of spaces in total).
    :cvar INHABITANT_ZONE: This group is describing an inhabitant zone.
    """
    PARKING_AREA = "parkingArea"
    TRUCK_PARKING_PRIORITY_ZONE = "truckParkingPriorityZone"
    AGGREGATION_OF_INFORMATION = "aggregationOfInformation"
    INHABITANT_ZONE = "inhabitantZone"


class HeightGradeEnum(Enum):
    """
    List of height or vertical gradings of road sections.

    :cvar ABOVE_GRADE: Above or over the normal road grade elevation.
    :cvar AT_GRADE: At the normal road grade elevation.
    :cvar BELOW_GRADE: Below or under the normal road grade elevation.
    """
    ABOVE_GRADE = "aboveGrade"
    AT_GRADE = "atGrade"
    BELOW_GRADE = "belowGrade"


class InformationStatusEnum(Enum):
    """
    Status of the related information (i.e. real, test or exercise).

    :cvar REAL: The information is real. It is not a test or exercise.
    :cvar SECURITY_EXERCISE: The information is part of an exercise
        which is for testing security.
    :cvar TECHNICAL_EXERCISE: The information is part of an exercise
        which includes tests of associated technical subsystems.
    :cvar TEST: The information is part of a test for checking the
        exchange of this type of information.
    """
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"


class InfrastructureDamageTypeEnum(Enum):
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


class InjuryStatusTypeEnum(Enum):
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
    """
    DEAD = "dead"
    INJURED = "injured"
    SERIOUSLY_INJURED = "seriouslyInjured"
    SLIGHTLY_INJURED = "slightlyInjured"
    UNINJURED = "uninjured"
    UNKNOWN = "unknown"


class InterUrbanParkingSiteLocationEnum(Enum):
    """
    Location of the truck or motorway related parking.

    :cvar MOTORWAY: The parking is located directly on a motorway or a
        similar type of road.
    :cvar NEARBY_MOTORWAY: The parking is located with some distance to
        a motorway or a similar type of road but focussed on travellers
        from this motorway.
    :cvar LAY_BY: An area along a road that offers temporary parking.
    :cvar ON_STREET: Vehicles are parking on the roadside.
    :cvar OTHER: The parking is located somewhere else.
    """
    MOTORWAY = "motorway"
    NEARBY_MOTORWAY = "nearbyMotorway"
    LAY_BY = "layBy"
    ON_STREET = "onStreet"
    OTHER = "other"


class InvolvementRolesEnum(Enum):
    """
    Involvement role of a person in event.

    :cvar CYCLIST: Cyclist.
    :cvar PEDESTRIAN: Pedestrian.
    :cvar UNKNOWN: Involvement role is unknown.
    :cvar VEHICLE_DRIVER: Vehicle driver.
    :cvar VEHICLE_OCCUPANT: Vehicle occupant (driver or passenger not
        specified).
    :cvar VEHICLE_PASSENGER: Vehicle passenger.
    :cvar WITNESS: Witness.
    """
    CYCLIST = "cyclist"
    PEDESTRIAN = "pedestrian"
    UNKNOWN = "unknown"
    VEHICLE_DRIVER = "vehicleDriver"
    VEHICLE_OCCUPANT = "vehicleOccupant"
    VEHICLE_PASSENGER = "vehiclePassenger"
    WITNESS = "witness"


class JunctionClassificationEnum(Enum):
    """
    Explicit type of a junction.

    :cvar THREE_WAY_INTERCHANGE: One motorway merging into another (with
        three legs in total).
    :cvar INTERCHANGE: Usually two crossing motorways (four legs, but
        can be even more).
    :cvar MOTORWAY_CONNECTION: Beginning or end of a motorway (e.g.
        changeover to smaller road).
    :cvar JUNCTION: Entrance and exit on a motorway.
    :cvar TEMPORARY_JUNCTION: Entrance and exit on a motorway, reserved
        either for emergency and service or on a temporary basis.
    :cvar BORDER_CROSSING: Motorway crossing a border (between counties,
        countries, states, ...).
    :cvar JUNCTION_IN_ONE_DIRECTION: Entry and Exit on a motorway, where
        just one direction of the motorway is accessible.
    :cvar OPERATIONAL_SERVICE_JUNCTION: Junction accessible only for
        operational services.
    :cvar OTHER: Other.
    """
    THREE_WAY_INTERCHANGE = "threeWayInterchange"
    INTERCHANGE = "interchange"
    MOTORWAY_CONNECTION = "motorwayConnection"
    JUNCTION = "junction"
    TEMPORARY_JUNCTION = "temporaryJunction"
    BORDER_CROSSING = "borderCrossing"
    JUNCTION_IN_ONE_DIRECTION = "junctionInOneDirection"
    OPERATIONAL_SERVICE_JUNCTION = "operationalServiceJunction"
    OTHER = "other"


class LABELSecurityLevelEnum(Enum):
    """
    Security level defined by the LABEL project http://truckparkinglabel.eu.

    :cvar NONE_VALUE: None.
    :cvar SECURITY_LEVEL1: Providing the basics.
    :cvar SECURITY_LEVEL2: Technical measures to improve security.
    :cvar SECURITY_LEVEL3: Security measures are combined, Access of
        persons restricted.
    :cvar SECURITY_LEVEL4: Real time monitoring of vehicles and persons
        by professional staff.
    :cvar SECURITY_LEVEL5: Verification of vehicles and persons by
        professional staff, site manned around the clock.
    :cvar UNKNOWN: Unknown.
    """
    NONE_VALUE = "none"
    SECURITY_LEVEL1 = "securityLevel1"
    SECURITY_LEVEL2 = "securityLevel2"
    SECURITY_LEVEL3 = "securityLevel3"
    SECURITY_LEVEL4 = "securityLevel4"
    SECURITY_LEVEL5 = "securityLevel5"
    UNKNOWN = "unknown"


class LABELServiceLevelEnum(Enum):
    """
    Service level defined by the LABEL project http://truckparkinglabel.eu.

    :cvar NONE_VALUE: None.
    :cvar SERVICE_LEVEL1: Providing the basics.
    :cvar SERVICE_LEVEL2: Also providing washing facilities and a more
        convenient lay-out of the parking area.
    :cvar SERVICE_LEVEL3: Providing service for personal hygiene and
        shop/ fuel station.
    :cvar SERVICE_LEVEL4: Providing full service for driver and vehicle.
    :cvar SERVICE_LEVEL5: Providing the high end of comfort levels.
    :cvar UNKNOWN: Unknown.
    """
    NONE_VALUE = "none"
    SERVICE_LEVEL1 = "serviceLevel1"
    SERVICE_LEVEL2 = "serviceLevel2"
    SERVICE_LEVEL3 = "serviceLevel3"
    SERVICE_LEVEL4 = "serviceLevel4"
    SERVICE_LEVEL5 = "serviceLevel5"
    UNKNOWN = "unknown"


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


class LinearElementNatureEnum(Enum):
    """
    List of indicative natures of linear elements.

    :cvar ROAD: The nature of the linear element is a road.
    :cvar ROAD_SECTION: The nature of the linear element is a section of
        a road.
    :cvar SLIP_ROAD: The nature of the linear element is a slip road.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ROAD = "road"
    ROAD_SECTION = "roadSection"
    SLIP_ROAD = "slipRoad"
    OTHER = "other"


class LinearReferencingDirectionEnum(Enum):
    """
    Directions of traffic flow relative to the direction in which the linear
    element is defined.

    :cvar BOTH: Indicates that both directions of traffic flow are
        affected by the situation or relate to the traffic data.
    :cvar OPPOSITE: Indicates that the direction of traffic flow
        affected by the situation or related to the traffic data is in
        the opposite sense to the direction in which the linear element
        is defined.
    :cvar ALIGNED: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is in the same
        sense as the direction in which the linear element is defined.
    :cvar UNKNOWN: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is unknown.
    """
    BOTH = "both"
    OPPOSITE = "opposite"
    ALIGNED = "aligned"
    UNKNOWN = "unknown"


class LoadType2Enum(Enum):
    """
    Loads that are currently not supported in loadType.

    :cvar REFRIGERATED_GOODS: Refrigerated goods.
    """
    REFRIGERATED_GOODS = "refrigeratedGoods"


class LoadTypeEnum(Enum):
    """
    Types of load carried by a vehicle.

    :cvar ABNORMAL_LOAD: A load that exceeds normal vehicle dimensions
        in terms of height, length, width, gross vehicle weight or axle
        weight or any combination of these. Generally termed an
        "abnormal load".
    :cvar AMMUNITION: Ammunition.
    :cvar CHEMICALS: Chemicals of unspecified type.
    :cvar COMBUSTIBLE_MATERIALS: Combustible materials of unspecified
        type.
    :cvar CORROSIVE_MATERIALS: Corrosive materials of unspecified type.
    :cvar DEBRIS: Debris of unspecified type.
    :cvar EMPTY: No load.
    :cvar EXPLOSIVE_MATERIALS: Explosive materials of unspecified type.
    :cvar EXTRA_HIGH_LOAD: A load of exceptional height.
    :cvar EXTRA_LONG_LOAD: A load of exceptional length.
    :cvar EXTRA_WIDE_LOAD: A load of exceptional width.
    :cvar FUEL: Fuel of unspecified type.
    :cvar GLASS: Glass.
    :cvar GOODS: Any goods of a commercial nature.
    :cvar HAZARDOUS_MATERIALS: Materials classed as being of a hazardous
        nature.
    :cvar LIQUID: Liquid of an unspecified nature.
    :cvar LIVESTOCK: Livestock.
    :cvar MATERIALS: General materials of unspecified type.
    :cvar MATERIALS_DANGEROUS_FOR_PEOPLE: Materials classed as being of
        a danger to people or animals.
    :cvar MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT: Materials classed as
        being potentially dangerous to the environment.
    :cvar MATERIALS_DANGEROUS_FOR_WATER: Materials classed as being
        dangerous when exposed to water (e.g. materials which may react
        exothermically with water).
    :cvar OIL: Oil.
    :cvar ORDINARY: Materials that present limited environmental or
        health risk. Non-combustible, non-toxic, non-corrosive.
    :cvar PERISHABLE_PRODUCTS: Products or produce that will
        significantly degrade in quality or freshness over a short
        period of time.
    :cvar PETROL: Petrol or petroleum.
    :cvar PHARMACEUTICAL_MATERIALS: Pharmaceutical materials.
    :cvar RADIOACTIVE_MATERIALS: Materials that emit significant
        quantities of electro-magnetic radiation that may present a risk
        to people, animals or the environment.
    :cvar REFUSE: Refuse.
    :cvar TOXIC_MATERIALS: Materials of a toxic nature which may damage
        the environment or endanger public health.
    :cvar VEHICLES: Vehicles of any type which are being transported.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABNORMAL_LOAD = "abnormalLoad"
    AMMUNITION = "ammunition"
    CHEMICALS = "chemicals"
    COMBUSTIBLE_MATERIALS = "combustibleMaterials"
    CORROSIVE_MATERIALS = "corrosiveMaterials"
    DEBRIS = "debris"
    EMPTY = "empty"
    EXPLOSIVE_MATERIALS = "explosiveMaterials"
    EXTRA_HIGH_LOAD = "extraHighLoad"
    EXTRA_LONG_LOAD = "extraLongLoad"
    EXTRA_WIDE_LOAD = "extraWideLoad"
    FUEL = "fuel"
    GLASS = "glass"
    GOODS = "goods"
    HAZARDOUS_MATERIALS = "hazardousMaterials"
    LIQUID = "liquid"
    LIVESTOCK = "livestock"
    MATERIALS = "materials"
    MATERIALS_DANGEROUS_FOR_PEOPLE = "materialsDangerousForPeople"
    MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT = "materialsDangerousForTheEnvironment"
    MATERIALS_DANGEROUS_FOR_WATER = "materialsDangerousForWater"
    OIL = "oil"
    ORDINARY = "ordinary"
    PERISHABLE_PRODUCTS = "perishableProducts"
    PETROL = "petrol"
    PHARMACEUTICAL_MATERIALS = "pharmaceuticalMaterials"
    RADIOACTIVE_MATERIALS = "radioactiveMaterials"
    REFUSE = "refuse"
    TOXIC_MATERIALS = "toxicMaterials"
    VEHICLES = "vehicles"
    OTHER = "other"


class LocationDescriptorEnum(Enum):
    """
    List of descriptors to help to identify a specific location.

    :cvar AROUND_ABEND_IN_ROAD: Around a bend in the road.
    :cvar AT_MOTORWAY_INTERCHANGE: At a motorway interchange.
    :cvar AT_REST_AREA: At rest area off the carriageway.
    :cvar AT_SERVICE_AREA: At service area.
    :cvar AT_TOLL_PLAZA: At toll plaza.
    :cvar AT_TUNNEL_ENTRY_OR_EXIT: At entry or exit of tunnel.
    :cvar INBOUND: On the carriageway or lane which is inbound towards
        the centre of the town or city.
    :cvar IN_GALLERY: In gallery.
    :cvar IN_THE_CENTRE: In the centre of the roadway.
    :cvar IN_THE_OPPOSITE_DIRECTION: In the opposite direction.
    :cvar IN_TUNNEL: In tunnel.
    :cvar ON_BORDER: On border crossing.
    :cvar ON_BRIDGE: On bridge.
    :cvar ON_CONNECTOR: On connecting carriageway between two different
        roads or road sections.
    :cvar ON_ELEVATED_SECTION: On elevated section of road.
    :cvar ON_FLYOVER: On flyover, i.e. on section of road over another
        road.
    :cvar ON_ICE_ROAD: On ice road.
    :cvar ON_LEVEL_CROSSING: On level-crossing.
    :cvar ON_LINK_ROAD: On road section linking two different roads.
    :cvar ON_PASS: On mountain pass.
    :cvar ON_ROUNDABOUT: On roundabout.
    :cvar ON_THE_LEFT: On the left of the roadway.
    :cvar ON_THE_RIGHT: On the right of the roadway.
    :cvar ON_THE_ROADWAY: On the roadway.
    :cvar ON_UNDERGROUND_SECTION: On underground section of road.
    :cvar ON_UNDERPASS: On underpass, i.e. section of road which passes
        under another road.
    :cvar OUTBOUND: On the carriageway or lane which is outbound from
        the centre of the town or city.
    :cvar OVER_CREST_OF_HILL: Over the crest of a hill.
    :cvar WITHIN_JUNCTION: On the main carriageway within a junction
        between exit slip road and entry slip road.
    """
    AROUND_ABEND_IN_ROAD = "aroundABendInRoad"
    AT_MOTORWAY_INTERCHANGE = "atMotorwayInterchange"
    AT_REST_AREA = "atRestArea"
    AT_SERVICE_AREA = "atServiceArea"
    AT_TOLL_PLAZA = "atTollPlaza"
    AT_TUNNEL_ENTRY_OR_EXIT = "atTunnelEntryOrExit"
    INBOUND = "inbound"
    IN_GALLERY = "inGallery"
    IN_THE_CENTRE = "inTheCentre"
    IN_THE_OPPOSITE_DIRECTION = "inTheOppositeDirection"
    IN_TUNNEL = "inTunnel"
    ON_BORDER = "onBorder"
    ON_BRIDGE = "onBridge"
    ON_CONNECTOR = "onConnector"
    ON_ELEVATED_SECTION = "onElevatedSection"
    ON_FLYOVER = "onFlyover"
    ON_ICE_ROAD = "onIceRoad"
    ON_LEVEL_CROSSING = "onLevelCrossing"
    ON_LINK_ROAD = "onLinkRoad"
    ON_PASS = "onPass"
    ON_ROUNDABOUT = "onRoundabout"
    ON_THE_LEFT = "onTheLeft"
    ON_THE_RIGHT = "onTheRight"
    ON_THE_ROADWAY = "onTheRoadway"
    ON_UNDERGROUND_SECTION = "onUndergroundSection"
    ON_UNDERPASS = "onUnderpass"
    OUTBOUND = "outbound"
    OVER_CREST_OF_HILL = "overCrestOfHill"
    WITHIN_JUNCTION = "withinJunction"


class MaintenanceVehicleActionsEnum(Enum):
    """
    Types of maintenance vehicle actions associated with roadworks.

    :cvar MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW: Maintenance
        vehicles are merging into the traffic flow creating a potential
        hazard for road users.
    :cvar SALT_AND_GRIT_SPREADING: Maintenance vehicle(s) are spreading
        salt and/or grit.
    :cvar SLOW_MOVING: Maintenance vehicles are slow moving.
    :cvar SNOW_CLEARING: Maintenance vehicle(s) are involved in the
        clearance of snow.
    :cvar STOPPING_TO_SERVICE_EQUIPMENTS: Maintenance vehicles are
        stopping to service equipments on or next to the roadway.
    """
    MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW = "maintenanceVehiclesMergingIntoTrafficFlow"
    SALT_AND_GRIT_SPREADING = "saltAndGritSpreading"
    SLOW_MOVING = "slowMoving"
    SNOW_CLEARING = "snowClearing"
    STOPPING_TO_SERVICE_EQUIPMENTS = "stoppingToServiceEquipments"


class MeansOfPaymentEnum(Enum):
    """
    Means of payment.

    :cvar PAYMENT_CARD: Payment by electronic card(s). Use
        'AcceptedPaymentCards' resp. 'UsedPaymentCard' to specify them
        more exactly.
    :cvar CASH: Cash payment.
    :cvar CASH_COINS_ONLY: Cash payment with coins only.
    :cvar DIRECT_CASH_TRANSFER: Direct cash transfer.
    :cvar ELECTRONIC_SETTLEMENT: Electronic settlement; includes on
        board units.
    :cvar RFID: RFID.
    :cvar MOBILE_APP: Payment method using an app on a smartphone.
    :cvar PAY_BY_SMS: Payment by SMS. The telephone number can be
        specified by 'paymentAdditionalDescription'.
    :cvar MOBILE_PHONE: A payment method using a mobile phone but
        without an app or SMS, for instance by calling a number.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    PAYMENT_CARD = "paymentCard"
    CASH = "cash"
    CASH_COINS_ONLY = "cashCoinsOnly"
    DIRECT_CASH_TRANSFER = "directCashTransfer"
    ELECTRONIC_SETTLEMENT = "electronicSettlement"
    RFID = "rfid"
    MOBILE_APP = "mobileApp"
    PAY_BY_SMS = "payBySMS"
    MOBILE_PHONE = "mobilePhone"
    UNKNOWN = "unknown"
    OTHER = "other"


class MeasuredOrDerivedDataTypeEnum(Enum):
    """
    Types of measured or derived data.

    :cvar HUMIDITY_INFORMATION: Measured or derived humidity
        information.
    :cvar INDIVIDUAL_VEHICLE_MEASUREMENTS: Measured or derived
        individual vehicle measurements.
    :cvar POLLUTION_INFORMATION: Measured or derived pollution
        information.
    :cvar PRECIPITATION_INFORMATION: Measured or derived precipitation
        information.
    :cvar PRESSURE_INFORMATION: Measured or derived pressure
        information.
    :cvar RADIATION_INFORMATION: Measured or derived radiation
        information.
    :cvar ROAD_SURFACE_CONDITION_INFORMATION: Measured or derived road
        surface conditions information.
    :cvar TEMPERATURE_INFORMATION: Measured or derived temperature
        information.
    :cvar TRAFFIC_CONCENTRATION: Measured or derived traffic
        concentration information.
    :cvar TRAFFIC_FLOW: Measured or derived traffic flow information.
    :cvar TRAFFIC_HEADWAY: Measured or derived traffic headway
        information.
    :cvar TRAFFIC_SPEED: Measured or derived traffic speed information.
    :cvar TRAFFIC_STATUS_INFORMATION: Measured or derived traffic status
        information.
    :cvar TRAVEL_TIME_INFORMATION: Measured or derived travel time
        information.
    :cvar VISIBILITY_INFORMATION: Measured or derived visibility
        information.
    :cvar WIND_INFORMATION: Measured or derived wind information.
    """
    HUMIDITY_INFORMATION = "humidityInformation"
    INDIVIDUAL_VEHICLE_MEASUREMENTS = "individualVehicleMeasurements"
    POLLUTION_INFORMATION = "pollutionInformation"
    PRECIPITATION_INFORMATION = "precipitationInformation"
    PRESSURE_INFORMATION = "pressureInformation"
    RADIATION_INFORMATION = "radiationInformation"
    ROAD_SURFACE_CONDITION_INFORMATION = "roadSurfaceConditionInformation"
    TEMPERATURE_INFORMATION = "temperatureInformation"
    TRAFFIC_CONCENTRATION = "trafficConcentration"
    TRAFFIC_FLOW = "trafficFlow"
    TRAFFIC_HEADWAY = "trafficHeadway"
    TRAFFIC_SPEED = "trafficSpeed"
    TRAFFIC_STATUS_INFORMATION = "trafficStatusInformation"
    TRAVEL_TIME_INFORMATION = "travelTimeInformation"
    VISIBILITY_INFORMATION = "visibilityInformation"
    WIND_INFORMATION = "windInformation"


class MeasurementEquipmentFaultEnum(Enum):
    """
    Types of measurement equipment faults.

    :cvar INTERMITTENT_DATA_VALUES: Data values are being produced at
        intermittent intervals which are not consitent with the expected
        reporting interval.
    :cvar NO_DATA_VALUES_AVAILABLE: No measured data values are
        currently available.
    :cvar SPURIOUS_UNRELIABLE_DATA_VALUES: Spurious or unreliable data
        values are being produced.
    :cvar UNSPECIFIED_OR_UNKNOWN_FAULT: An unspecified or unknown fault
        exists in the measurement equipment.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    INTERMITTENT_DATA_VALUES = "intermittentDataValues"
    NO_DATA_VALUES_AVAILABLE = "noDataValuesAvailable"
    SPURIOUS_UNRELIABLE_DATA_VALUES = "spuriousUnreliableDataValues"
    UNSPECIFIED_OR_UNKNOWN_FAULT = "unspecifiedOrUnknownFault"
    OTHER = "other"


class MobilityEnum(Enum):
    """
    Types of mobility relating to a situation element defined by a
    SituationReord.

    :cvar MOBILE: The described element of a situation is moving.
    :cvar STATIONARY: The described element of a situation is
        stationary.
    :cvar UNKNOWN: The mobility of the described element of a situation
        is unknown.
    """
    MOBILE = "mobile"
    STATIONARY = "stationary"
    UNKNOWN = "unknown"


class MonthOfYearEnum(Enum):
    """
    A list of the months of the year.

    :cvar JANUARY: The month of January.
    :cvar FEBRUARY: The month of February.
    :cvar MARCH: The month of March.
    :cvar APRIL: The month of April.
    :cvar MAY: The month of May.
    :cvar JUNE: The month of June.
    :cvar JULY: The month of July.
    :cvar AUGUST: The month of August.
    :cvar SEPTEMBER: The month of September.
    :cvar OCTOBER: The month of October.
    :cvar NOVEMBER: The month of November.
    :cvar DECEMBER: The month of December.
    """
    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"


@dataclass
class MultilingualStringValue:
    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 1024,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class NonWeatherRelatedRoadConditionTypeEnum(Enum):
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
    :cvar ROAD_SURFACE_IN_POOR_CONDITION: The road surface is damaged,
        severely rutted or potholed (i.e. it is in a poor state of
        repair).
    :cvar SLIPPERY_ROAD: The road surface is slippery due to an
        unspecified non-weather related cause.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    DIESEL_ON_ROAD = "dieselOnRoad"
    LEAVES_ON_ROAD = "leavesOnRoad"
    LOOSE_CHIPPINGS = "looseChippings"
    LOOSE_SAND_ON_ROAD = "looseSandOnRoad"
    MUD_ON_ROAD = "mudOnRoad"
    OIL_ON_ROAD = "oilOnRoad"
    PETROL_ON_ROAD = "petrolOnRoad"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"


class ObstructionTypeEnum(Enum):
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
    :cvar HIGH_SPEED_CHASE: Authorised and unauthorised vehicles are
        travelling at high speeds along the roadway.  This may present a
        hazard to other vehicles.
    :cvar HOUSE_FIRE: House fire(s) near the road way resulting in smoke
        and driver distraction which may cause traffic disruption.
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
    :cvar RECKLESS_DRIVER: A vehicle being driven without due care and
        attention is causing a hazard to other vehicles.
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
    HIGH_SPEED_CHASE = "highSpeedChase"
    HOUSE_FIRE = "houseFire"
    INCIDENT = "incident"
    INDUSTRIAL_ACCIDENT = "industrialAccident"
    OBJECT_ON_THE_ROAD = "objectOnTheRoad"
    OBJECTS_FALLING_FROM_MOVING_VEHICLE = "objectsFallingFromMovingVehicle"
    OBSTRUCTION_ON_THE_ROAD = "obstructionOnTheRoad"
    PEOPLE_ON_ROADWAY = "peopleOnRoadway"
    RAIL_CRASH = "railCrash"
    RECKLESS_DRIVER = "recklessDriver"
    RESCUE_AND_RECOVERY_WORK = "rescueAndRecoveryWork"
    SEVERE_FROST_DAMAGED_ROADWAY = "severeFrostDamagedRoadway"
    SHED_LOAD = "shedLoad"
    SNOW_AND_ICE_DEBRIS = "snowAndIceDebris"
    SPILLAGE_OCCURRING_FROM_MOVING_VEHICLE = "spillageOccurringFromMovingVehicle"
    SPILLAGE_ON_THE_ROAD = "spillageOnTheRoad"
    UNPROTECTED_ACCIDENT_AREA = "unprotectedAccidentArea"
    OTHER = "other"


class OccupancyDetectionTypeEnum(Enum):
    """Type of parking occupancy detection (balancing, single slot, ...

    ).

    :cvar NONE_VALUE: No occupancy detection available.
    :cvar BALANCING: Counting and balancing incoming and outcoming
        traffic amount ('indirect' method).
    :cvar SINGLE_SPACE_DETECTION: There is a detector for every
        individual parking space ('direct' method).
    :cvar MODEL_BASED: Occupancy detection is based on some model, i.e.
        hydrograph, forecasting or estimation.
    :cvar MANUAL: Manual collection of occupancy information, i.e.
        operators count the vehicles.
    :cvar UNSPECIFIED: Unspecified.
    :cvar OTHER: Other.
    :cvar UNKNOWN: Unknown.
    """
    NONE_VALUE = "none"
    BALANCING = "balancing"
    SINGLE_SPACE_DETECTION = "singleSpaceDetection"
    MODEL_BASED = "modelBased"
    MANUAL = "manual"
    UNSPECIFIED = "unspecified"
    OTHER = "other"
    UNKNOWN = "unknown"


class OpeningStatusEnum(Enum):
    """
    The opening status of some entity (e.g. parking site, service facility,
    access,...)

    :cvar OPEN: Open resp. available.
    :cvar CLOSED: Closed, usually because of the regular opening times.
    :cvar CLOSED_ABNORMAL: Closed because of some scheduled or
        unscheduled event, like holiday, maintenance, construction works
        or any kind of problems. It is possible that the closure will
        last for some time.
    :cvar OPENING_TIMES_IN_FORCE: The normal opening times are in force,
        i.e. it is not explicit said if it's open right now.
    :cvar STATUS_UNKNOWN: The opening status is unknown.
    :cvar OTHER: Other.
    """
    OPEN = "open"
    CLOSED = "closed"
    CLOSED_ABNORMAL = "closedAbnormal"
    OPENING_TIMES_IN_FORCE = "openingTimesInForce"
    STATUS_UNKNOWN = "statusUnknown"
    OTHER = "other"


class OpenlrFormOfWayEnum(Enum):
    """
    Enumeration of for of way.

    :cvar UNDEFINED: undefined
    :cvar MOTORWAY: motorway
    :cvar MULTIPLE_CARRIAGEWAY: multipleCarrigeway
    :cvar SINGLE_CARRIAGEWAY: single carrigeway
    :cvar ROUNDABOUT: roadabout
    :cvar SLIP_ROAD: sliproad
    :cvar TRAFFIC_SQUARE: traffic square
    :cvar OTHER: other
    """
    UNDEFINED = "undefined"
    MOTORWAY = "motorway"
    MULTIPLE_CARRIAGEWAY = "multipleCarriageway"
    SINGLE_CARRIAGEWAY = "singleCarriageway"
    ROUNDABOUT = "roundabout"
    SLIP_ROAD = "slipRoad"
    TRAFFIC_SQUARE = "trafficSquare"
    OTHER = "other"


class OpenlrFunctionalRoadClassEnum(Enum):
    """
    Enemuration of functional road class.

    :cvar FRC0: Main road, highest importance
    :cvar FRC1: First class road
    :cvar FRC2: Second class road
    :cvar FRC3: Third class road
    :cvar FRC4: Fourth class road
    :cvar FRC5: Fifth class road
    :cvar FRC6: Sixth class road
    :cvar FRC7: Other class road, lowest importance
    """
    FRC0 = "FRC0"
    FRC1 = "FRC1"
    FRC2 = "FRC2"
    FRC3 = "FRC3"
    FRC4 = "FRC4"
    FRC5 = "FRC5"
    FRC6 = "FRC6"
    FRC7 = "FRC7"


class OpenlrOrientationEnum(Enum):
    """
    Enumeration of side of road.

    :cvar NO_ORIENTATION_OR_UNKNOWN: No orientation or unknown
    :cvar WITH_LINE_DIRECTION: With line direction
    :cvar AGAINST_LINE_DIRECTION: Against line direction
    :cvar BOTH: Both directions
    """
    NO_ORIENTATION_OR_UNKNOWN = "noOrientationOrUnknown"
    WITH_LINE_DIRECTION = "withLineDirection"
    AGAINST_LINE_DIRECTION = "againstLineDirection"
    BOTH = "both"


class OpenlrSideOfRoadEnum(Enum):
    """
    Enumeration of side of road.

    :cvar ON_ROAD_OR_UNKNOWN: On road or unknown
    :cvar RIGHT: right
    :cvar LEFT: left
    :cvar BOTH: both
    """
    ON_ROAD_OR_UNKNOWN = "onRoadOrUnknown"
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


class OperatingModeEnum(Enum):
    """
    Modes of operation of the exchange.

    :cvar OPERATING_MODE0: "Subscription Management Mechanism" - a
        specialized operating mode to handle subscriptions.
    :cvar OPERATING_MODE1: "Publisher Push on Occurrence" operating
        mode.
    :cvar OPERATING_MODE2: "Publisher Push Periodic" operating mode.
    :cvar OPERATING_MODE3: "Client Pull" operating mode.
    """
    OPERATING_MODE0 = "operatingMode0"
    OPERATING_MODE1 = "operatingMode1"
    OPERATING_MODE2 = "operatingMode2"
    OPERATING_MODE3 = "operatingMode3"


class OperationStatusEnum(Enum):
    """
    Specifies, whether some scenario or equipment is in operation or not.

    :cvar IN_OPERATION: The specified element is in operation right now.
    :cvar LIMITED_OPERATION: The specified element is in operation on a
        limited basis.
    :cvar NOT_IN_OPERATION: The specified element is not operating right
        now.
    :cvar NOT_IN_OPERATION_ABNORMAL: The specified element is not
        operating due to abnormal conditions (holidays, restoration-
        works, long-term closure, ....).
    :cvar TECHNICAL_DEFECT: The specified element is not in operation
        due to a technical defect.
    :cvar UNKNOWN: There is no information about the operation status.
    """
    IN_OPERATION = "inOperation"
    LIMITED_OPERATION = "limitedOperation"
    NOT_IN_OPERATION = "notInOperation"
    NOT_IN_OPERATION_ABNORMAL = "notInOperationAbnormal"
    TECHNICAL_DEFECT = "technicalDefect"
    UNKNOWN = "unknown"


class OperatorActionOriginEnum(Enum):
    """
    Origins of operator actions.

    :cvar EXTERNAL: Operator action originated externally to the
        authority which is taking the action.
    :cvar INTERNAL: Operator action originated within the authority
        which is taking the action.
    """
    EXTERNAL = "external"
    INTERNAL = "internal"


class OperatorActionStatusEnum(Enum):
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
    """
    REQUESTED = "requested"
    APPROVED = "approved"
    BEING_IMPLEMENTED = "beingImplemented"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"
    TERMINATION_REQUESTED = "terminationRequested"
    BEING_TERMINATED = "beingTerminated"


class OwnershipTypeEnum(Enum):
    """
    Ownership type enum.

    :cvar PUBLIC: Public ownership.
    :cvar PRIVATE: Private ownership.
    :cvar PUBLIC_PRIVATE: A public private partnership model.
    :cvar RESIDENT: A private individual ownership.
    :cvar UNKNOWN: An unknown kind of ownership.
    :cvar OTHER: Other kind of ownership.
    """
    PUBLIC = "public"
    PRIVATE = "private"
    PUBLIC_PRIVATE = "publicPrivate"
    RESIDENT = "resident"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingConditionsEnum(Enum):
    """
    Defines if normal parking conditions are suspended or special parking
    conditions are in force.

    :cvar NORMAL_PARKING_CONDITIONS_SUSPENDED: The parking conditions
        (possibly including tariffs) that normally apply are temporarily
        suspended.
    :cvar SPECIAL_PARKING_CONDITIONS_IN_FORCE: Parking conditions, other
        than those that normally apply, are currently in force for the
        parking site.
    :cvar OTHER: Other.
    """
    NORMAL_PARKING_CONDITIONS_SUSPENDED = "normalParkingConditionsSuspended"
    SPECIAL_PARKING_CONDITIONS_IN_FORCE = "specialParkingConditionsInForce"
    OTHER = "other"


class ParkingDurationEnum(Enum):
    """
    Parking durations.

    :cvar PICK_UP_DROP_OFF: Very short duration parking normally of up
        to 20 minutes assigned for pick-ups and drop-offs.
    :cvar SHORT_TERM: Short term parking without indication of max-
        duration.
    :cvar SHORT_TERM24HOURS: Short term parking up to 24 hours.
    :cvar SHORT_TERM48HOURS: Short term parking up to 48 hours.
    :cvar SHORT_TERM72HOURS: Short term parking up to 72 hours.
    :cvar SHORT_TERM96HOURS: Short term parking up to 96 hours.
    :cvar LONG_TERM: Long term parking in excess of any specified short
        term parking.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    PICK_UP_DROP_OFF = "pickUpDropOff"
    SHORT_TERM = "shortTerm"
    SHORT_TERM24HOURS = "shortTerm24hours"
    SHORT_TERM48HOURS = "shortTerm48hours"
    SHORT_TERM72HOURS = "shortTerm72hours"
    SHORT_TERM96HOURS = "shortTerm96hours"
    LONG_TERM = "longTerm"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingFaultEnum(Enum):
    """
    Types of parking site or access faults.

    :cvar COMMUNICATIONS_FAILURE: Communications failure affecting
        parking site.
    :cvar BARRIER_MALFUNCTION: The entrance or exit barrier(s) are
        malfunctioning causing access problems to vehicles.
    :cvar ENTRANCE_EXIT_OBSTRUCTED: One or more entrances or exits are
        obstructed to some degree causing access problems to vehicles.
    :cvar ERRONEOUS_OCCUPANCY_INFORMATION: Occupancy information is
        subject to errors due to malfunctioning equipment.
    :cvar ERRONEOUS_OCCUPANCY_DISPLAYED: Occupancy information displayed
        on signs associated with parking site (e.g. at entrance) are
        erroneous.
    :cvar PAYMENT_MACHINES_INOPERATIVE: Payment machines are not
        functioning normally.
    :cvar RESERVATION_SERVICE_OUT_OF_ORDER: Reservation service out of
        order.
    :cvar NO_PARKING_INFORMATION_AVAILABLE: No parking information
        available.
    :cvar UNSPECIFIED: General fault of unspecified type.
    :cvar UNKNOWN: Unknown parking facility fault.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    BARRIER_MALFUNCTION = "barrierMalfunction"
    ENTRANCE_EXIT_OBSTRUCTED = "entranceExitObstructed"
    ERRONEOUS_OCCUPANCY_INFORMATION = "erroneousOccupancyInformation"
    ERRONEOUS_OCCUPANCY_DISPLAYED = "erroneousOccupancyDisplayed"
    PAYMENT_MACHINES_INOPERATIVE = "paymentMachinesInoperative"
    RESERVATION_SERVICE_OUT_OF_ORDER = "reservationServiceOutOfOrder"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingLayoutEnum(Enum):
    """
    Types of layout of the parking site.

    :cvar MULTI_STOREY: Parking is on multiple levels within a parking
        building.
    :cvar SINGLE_LEVEL: Parking is inside a building on a single ground
        floor level.
    :cvar UNDERGROUND: Parking is on one or more floors below ground
        level.
    :cvar UNDERGROUND_AND_MULTISTOREY: Parking is on multiple floors
        levels including both below and above ground level.
    :cvar AUTOMATED_PARKING_GARAGE: Parking is completely automated from
        the point of leaving the vehicle in an arrival bay to its
        delivery back to the driver in a pickup bay.
    :cvar OPEN_SPACE: A normal ground level parking place.
    :cvar COVERED: Some covered parking space.
    :cvar NESTED: A parking space within a complex structure of
        buildings or surrounded by buildings.
    :cvar FIELD_VALUE: A non-bituminized parking space (e.g. for events
        or as extension).
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    MULTI_STOREY = "multiStorey"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"
    UNDERGROUND_AND_MULTISTOREY = "undergroundAndMultistorey"
    AUTOMATED_PARKING_GARAGE = "automatedParkingGarage"
    OPEN_SPACE = "openSpace"
    COVERED = "covered"
    NESTED = "nested"
    FIELD_VALUE = "field"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingModeEnum(Enum):
    """
    The arrangement of the parking space or the group of parking spaces in
    relation to the road.

    :cvar PERPENDICULAR_PARKING: Parking spaces are located in an angle
        of nearly 90 degree to the road.
    :cvar PARALLEL_PARKING: Parking spaces are located parallel to the
        road.
    :cvar ECHELON_PARKING: Parking spaces are located in a diagonal
        relation to the road.
    :cvar PARKING_ON_OPPOSITE_SIDE_OF_ROAD: Parking is possible on the
        other side of the road.
    :cvar OTHER: Other.
    """
    PERPENDICULAR_PARKING = "perpendicularParking"
    PARALLEL_PARKING = "parallelParking"
    ECHELON_PARKING = "echelonParking"
    PARKING_ON_OPPOSITE_SIDE_OF_ROAD = "parkingOnOppositeSideOfRoad"
    OTHER = "other"


class ParkingOccupancyEnum(Enum):
    """
    Parking Occupancy enum.

    :cvar EXPECT_CAR_PARK_TO_BE_FULL: Expect car park to be full.
    :cvar PERCENTAGE10: 10% full.
    :cvar PERCENTAGE20: 20% full.
    :cvar PERCENTAGE30: 30% full.
    :cvar PERCENTAGE40: 40% full.
    :cvar PERCENTAGE50: 50% full.
    :cvar PERCENTAGE60: 60% full.
    :cvar PERCENTAGE70: 70% full.
    :cvar PERCENTAGE80: 80% full.
    :cvar PERCENTAGE90: 90% full.
    :cvar FULL: Full.
    :cvar UNKNOWN: Unknown.
    """
    EXPECT_CAR_PARK_TO_BE_FULL = "expectCarParkToBeFull"
    PERCENTAGE10 = "percentage10"
    PERCENTAGE20 = "percentage20"
    PERCENTAGE30 = "percentage30"
    PERCENTAGE40 = "percentage40"
    PERCENTAGE50 = "percentage50"
    PERCENTAGE60 = "percentage60"
    PERCENTAGE70 = "percentage70"
    PERCENTAGE80 = "percentage80"
    PERCENTAGE90 = "percentage90"
    FULL = "full"
    UNKNOWN = "unknown"


class ParkingOccupancyTrendEnum(Enum):
    """
    List of terms used to describe the trend in parking space occupancy.

    :cvar DECREASING: Parking space occupancy is decreasing.
    :cvar INCREASING: Parking space occupancy is increasing.
    :cvar STABLE: Parking space occupancy is stable.
    :cvar INCREASING_QUICKLY: Parking space occupancy is increasing
        quickly.
    :cvar INCREASING_SLOWLY: Parking space occupancy is increasing
        slowly.
    :cvar DECREASING_QUICKLY: Parking space occupancy is decreasing
        quickly.
    :cvar DECREASING_SLOWLY: Parking space occupancy is decreasing
        slowly.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"
    INCREASING_QUICKLY = "increasingQuickly"
    INCREASING_SLOWLY = "increasingSlowly"
    DECREASING_QUICKLY = "decreasingQuickly"
    DECREASING_SLOWLY = "decreasingSlowly"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingPaymentModeEnum(Enum):
    """
    Mode of payment for parking.

    :cvar PAY_AND_DISPLAY: Pay at machine and display ticket inside
        vehicle.
    :cvar PAY_MANUAL_AT_EXIT_BOOTH: Pay at the manned exit booth of the
        parking site.
    :cvar PAY_PRIOR_TO_EXIT: Pay at machine on foot prior to returning
        to vehicle and use payment ticket to exit.
    :cvar PAY_BY_PREPAID_TOKEN: Pay by prepaid token that is used at
        exit.
    :cvar PAY_AND_EXIT: Pay directly at the exit with a payment card
        (usually, this payment card must have been used when entering as
        well). In 'AccessEquipmentEnum', there are three more literals
        to indicate, whether an entrance or exit has got this feature.
    :cvar OTHER: Other.
    """
    PAY_AND_DISPLAY = "payAndDisplay"
    PAY_MANUAL_AT_EXIT_BOOTH = "payManualAtExitBooth"
    PAY_PRIOR_TO_EXIT = "payPriorToExit"
    PAY_BY_PREPAID_TOKEN = "payByPrepaidToken"
    PAY_AND_EXIT = "payAndExit"
    OTHER = "other"


class ParkingRouteDirectionEnum(Enum):
    """
    The direction of the parking route.

    :cvar TOWARDS_PARKING_SITE: Towards parking site.
    :cvar AWAY_FROM_PARKING_SITE: Away from parking site.
    """
    TOWARDS_PARKING_SITE = "towardsParkingSite"
    AWAY_FROM_PARKING_SITE = "awayFromParkingSite"


class ParkingRouteTypeEnum(Enum):
    """
    The type of the parking route.

    :cvar PEDESTRIAN: A parking route for pedestrian.
    :cvar BICYCLE: A parking route for bicycles.
    :cvar LORRY: A parking route for lorries.
    :cvar OTHER: Another type of parking route.
    """
    PEDESTRIAN = "pedestrian"
    BICYCLE = "bicycle"
    LORRY = "lorry"
    OTHER = "other"


class ParkingSecurityEnum(Enum):
    """
    Specifies security measures related to the parking site or particular
    spaces.

    :cvar SOCIAL_CONTROL: Social control e.g. parking situated in a
        neighbourhood.
    :cvar SECURITY_STAFF: Security staff.
    :cvar EXTERNAL_SECURITY: External security, e.g. police or staff not
        directly belonging to the parking.
    :cvar CCTV: CCTV (camera observation).
    :cvar DOG: Dog.
    :cvar GUARD24HOURS: 24/24 guard.
    :cvar LIGHTING: Site is illuminated in a normal way (but not as
        strong as 'floodLight').
    :cvar FLOOD_LIGHT: Flood light (stronger than lighting).
    :cvar FENCES: Fences.
    :cvar AREA_SEPERATED_FROM_SURROUNDINGS: Site is separated from its
        surroundings. Can also be used to express a space for noise-
        producing vehicles, e.g. lorries with cooling generators.
    :cvar NONE_VALUE: There are no security measures.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: None of the values in this enumeration applies. Use
        'parkingAdditionalSecurity' instead.
    """
    SOCIAL_CONTROL = "socialControl"
    SECURITY_STAFF = "securityStaff"
    EXTERNAL_SECURITY = "externalSecurity"
    CCTV = "cctv"
    DOG = "dog"
    GUARD24HOURS = "guard24hours"
    LIGHTING = "lighting"
    FLOOD_LIGHT = "floodLight"
    FENCES = "fences"
    AREA_SEPERATED_FROM_SURROUNDINGS = "areaSeperatedFromSurroundings"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingSiteOvercrowdingStatusEnum(Enum):
    """The overcrowding status of the parking site.

    Choose between two levels or simply (no) overcrowding.

    :cvar OVERCROWDING: The parking site is overcrowded (as specified in
        ParkingThresholds).
    :cvar NO_OVERCROWDING: The parking site is not overcrowded.
    :cvar OVERCROWDING_LEVEL1: The parking site is overcrowded at level
        1 (as specified in ParkingThresholds).
    :cvar OVERCROWDING_LEVEL2: The parking site is overcrowded at level
        2 (as specified in ParkingThresholds).
    :cvar UNKNOWN: The overcrowding level is unknown.
    :cvar OTHER: Other.
    """
    OVERCROWDING = "overcrowding"
    NO_OVERCROWDING = "noOvercrowding"
    OVERCROWDING_LEVEL1 = "overcrowdingLevel1"
    OVERCROWDING_LEVEL2 = "overcrowdingLevel2"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingSiteStatusEnum(Enum):
    """
    The status of the parking site (spaces available or not).

    :cvar SPACES_AVAILABLE: Parking spaces are currently available.
    :cvar ALMOST_FULL: The parking site is almost full (as defined by
        its configuration parameters).
    :cvar FULL_AT_ENTRANCE: The parking site is considered full at its
        entrance (e.g. full sign is displayed at entrance or on managing
        VMS).
    :cvar FULL: The parking site is full (as defined by its
        configuration parameters).
    :cvar UNKNOWN: The status of the parking site is unknown.
    :cvar OTHER: Other.
    """
    SPACES_AVAILABLE = "spacesAvailable"
    ALMOST_FULL = "almostFull"
    FULL_AT_ENTRANCE = "fullAtEntrance"
    FULL = "full"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingSpaceAccessibilityEnum(Enum):
    """
    Easements for handicapped people expecially related to a parking space or a
    group of parking spaces.

    :cvar EXTRA_SPACE_LEFT_SIDE: There is some extra space on the left
        side of the parking space (in parking direction point of view),
        for example to improve the situation for wheelchair users.
    :cvar EXTRA_SPACE_RIGHT_SIDE: There is some extra space on the right
        side of the parking space (in parking direction point of view),
        for example to improve the situation for wheelchair users.
    :cvar NEARBY_PEDESTRIAN_EXIT: The parking space is quite near to a
        pedestrian exit. Note: Can be more exactly defined by using
        'dedicatedAccess'.
    :cvar BORDERS_MARKED: The border of the parking space is marked
        (painted on the ground).
    :cvar OTHER: Other.
    """
    EXTRA_SPACE_LEFT_SIDE = "extraSpaceLeftSide"
    EXTRA_SPACE_RIGHT_SIDE = "extraSpaceRightSide"
    NEARBY_PEDESTRIAN_EXIT = "nearbyPedestrianExit"
    BORDERS_MARKED = "bordersMarked"
    OTHER = "other"


class ParkingSpacePhysicsEnum(Enum):
    """
    Specifies drive through and open air properties for the parking space or
    the group of parking spaces.

    :cvar DRIVE_THROUGH: Entering as well as leaving the parking space
        can be done straight in the direction of parking.
    :cvar OPEN_AIR: There is no roof and not another storey on top of
        the parking space, which could prevent from rain, for example.
    """
    DRIVE_THROUGH = "driveThrough"
    OPEN_AIR = "openAir"


class ParkingSpecialLocationEnum(Enum):
    """
    Locations, often associated with a building, for a
    SpecialLocationParkingSite.

    :cvar AIRPORT_TERMINAL: The parking site is associated with an
        airport terminal.
    :cvar EXHIBITON_CENTRE: The parking site is associated with an
        exhibition centre.
    :cvar SHOPPING_CENTRE: The parking site is associated with a
        shopping centre.
    :cvar SPECIFIC_FACILITY: The parking site is associated with a
        specific facility (e.g. a hospital, a tourist site, a garden
        centre, a park etc.).. Attribute "parkingOtherSpecialLocation"
        may be used to specify details.
    :cvar TRAIN_STATION: The parking site is associated with a train
        station.
    :cvar CAMPGROUND: The parking site is associated with a campground.
    :cvar THEME_PARK: The parking site is associated with a theme park.
    :cvar FERRY_TERMINAL: The parking site is associated with a ferry
        terminal.
    :cvar VEHICLE_ON_RAIL_TERMINAL: The parking site is associated with
        a vehicle-to-rail terminal.
    :cvar COACH_STATION: The parking site is associated with a coach
        station.
    :cvar CABLE_CAR_STATION: The parking site is associated with a cable
        car station.
    :cvar PUBLIC_TRANSPORT_STATION: The parking site is associated with
        a public transport station.
    :cvar MARKET: The parking site is associated with a market.
    :cvar RELIGIOUS_CENTRE: The parking site is associated with a
        religious centre.
    :cvar CONVENTION_CENTRE: The parking site is associated with a
        convention centre.
    :cvar CINEMA: The parking site is associated with a cinema.
    :cvar SKILIFT: The parking site is associated with a ski lift.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: The parking site is associated with some other
        location. Use "parkingOtherSpecialLocation" to specify details.
    """
    AIRPORT_TERMINAL = "airportTerminal"
    EXHIBITON_CENTRE = "exhibitonCentre"
    SHOPPING_CENTRE = "shoppingCentre"
    SPECIFIC_FACILITY = "specificFacility"
    TRAIN_STATION = "trainStation"
    CAMPGROUND = "campground"
    THEME_PARK = "themePark"
    FERRY_TERMINAL = "ferryTerminal"
    VEHICLE_ON_RAIL_TERMINAL = "vehicleOnRailTerminal"
    COACH_STATION = "coachStation"
    CABLE_CAR_STATION = "cableCarStation"
    PUBLIC_TRANSPORT_STATION = "publicTransportStation"
    MARKET = "market"
    RELIGIOUS_CENTRE = "religiousCentre"
    CONVENTION_CENTRE = "conventionCentre"
    CINEMA = "cinema"
    SKILIFT = "skilift"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingSupervisionEnum(Enum):
    """
    Defines the kind of supervision of the parking site.

    :cvar REMOTE: Remote.
    :cvar ON_SITE: On site.
    :cvar CONTROL_CENTRE_ON_SITE: Control centre on site.
    :cvar CONTROL_CENTRE_OFF_SITE: Control centre off site.
    :cvar PATROL: Patrol.
    :cvar NONE_VALUE: None.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    REMOTE = "remote"
    ON_SITE = "onSite"
    CONTROL_CENTRE_ON_SITE = "controlCentreOnSite"
    CONTROL_CENTRE_OFF_SITE = "controlCentreOffSite"
    PATROL = "patrol"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingTypeOfGroup(Enum):
    """
    The type of group specification (group of parking spaces).

    :cvar ADJACENT_SPACES: A description of adjacent spaces.
    :cvar NON_ADJACENT_SPACES: A description of non-adjacent spaces.
    :cvar COMPLETE_FLOOR: A description for a complete floor in a car
        park.
    :cvar MIXED_USAGE: A definition for mixed usage for this group (e.g.
        by time). This means there are more definitions for this group
        or for sub- or supersets of it.
    :cvar STATISTICS_ONLY: This group provides statistical figures only,
        for example 60 spaces for lorries in total. Usually, this kind
        of group does not use georeference information.  It is not a
        complete description of parking spaces.
    :cvar SINGLE_PARAMETERS: This group provides some single features
        for a selected number of spaces. For example, you can define all
        spaces, where electric charging stations are provided. It is not
        a complete description of the parking spaces.
    :cvar OTHER: Some other kind of group.
    """
    ADJACENT_SPACES = "adjacentSpaces"
    NON_ADJACENT_SPACES = "nonAdjacentSpaces"
    COMPLETE_FLOOR = "completeFloor"
    MIXED_USAGE = "mixedUsage"
    STATISTICS_ONLY = "statisticsOnly"
    SINGLE_PARAMETERS = "singleParameters"
    OTHER = "other"


class ParkingUsageScenarioEnum(Enum):
    """
    Types of parking usage (park &amp; ride, kiss &amp; ride, ...)

    :cvar TRUCK_PARKING: The parking site is designed for lorries (other
        vehicles are allowed as well).
    :cvar PARK_AND_RIDE: Parking for public transport users.
    :cvar PARK_AND_CYCLE: A parking site for people who continue their
        journey by bike.
    :cvar PARK_AND_WALK: A parking site for people who continue to walk.
    :cvar KISS_AND_RIDE: Parking site with possibility for very short
        parking to drop off (or drop on) passengers for public
        transport.
    :cvar LIFTSHARE: A parking site for people who are sharing their
        cars.
    :cvar CAR_SHARING: A parking site for people who are sharing cars
        organised by a car sharing company..
    :cvar REST_AREA: The parking site is associated with a rest area,
        i.e. people can relax some time outside their car there. Note
        that the presence of some bench, picnic place or toilet is
        already sufficient; there is no need for a restaurant or a
        building.
    :cvar SERVICE_AREA: The parking site is associated with a service
        area.
    :cvar DROP_OFF_WITH_VALET: A valet drop off service.
    :cvar DROP_OFF_MECHANICAL: A mechanical drop off service.
    :cvar EVENT_PARKING: Parking is associated with an event. Use
        'eventParkingType' or 'eventParkingType2' to specify the event.
    :cvar AUTOMATIC_PARKING_GUIDANCE: Specifies, if there is a (visual)
        guidance system within the parking site, which helps the drivers
        to find free spaces. Note: This is not a parking VMS or a
        parking route, which are usually located outside the parking
        site.
    :cvar STAFF_GUIDES_TO_SPACE: Staff guides to space.
    :cvar VEHICLE_LIFT: Vehicle lift
    :cvar LOADING_BAY: The parking site or space(s) are designed as a
        loading bay.
    :cvar DROP_OFF: The parking site or space(s) are designed for drop
        off only.
    :cvar OVERNIGHT_PARKING: The parking site or space(s) are designed
        for overnight parking. Note that the absence of this scenario
        does not automatically mean a prohibition of overnight parking.
        See also PermitsAndProhibitions.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other usage scenario.
    """
    TRUCK_PARKING = "truckParking"
    PARK_AND_RIDE = "parkAndRide"
    PARK_AND_CYCLE = "parkAndCycle"
    PARK_AND_WALK = "parkAndWalk"
    KISS_AND_RIDE = "kissAndRide"
    LIFTSHARE = "liftshare"
    CAR_SHARING = "carSharing"
    REST_AREA = "restArea"
    SERVICE_AREA = "serviceArea"
    DROP_OFF_WITH_VALET = "dropOffWithValet"
    DROP_OFF_MECHANICAL = "dropOffMechanical"
    EVENT_PARKING = "eventParking"
    AUTOMATIC_PARKING_GUIDANCE = "automaticParkingGuidance"
    STAFF_GUIDES_TO_SPACE = "staffGuidesToSpace"
    VEHICLE_LIFT = "vehicleLift"
    LOADING_BAY = "loadingBay"
    DROP_OFF = "dropOff"
    OVERNIGHT_PARKING = "overnightParking"
    UNKNOWN = "unknown"
    OTHER = "other"


class ParkingVacantSpacesEnum(Enum):
    """
    Parking vacant spaces enum.

    :cvar NO_PARKING_SPACES_AVAILABLE: No parking spaces available.
    :cvar EXPECT_NO_SPACES_AVAILABLE: Expect no parking spaces
        available.
    :cvar ONLY_AFEW_SPACES_AVAILABLE: Only a few parking spaces
        available.
    :cvar LESS_THAN10_SPACES_AVAILABLE: Less than 10 parking spaces
        available.
    :cvar LESS_THAN20_SPACES_AVAILABLE: Less than 20 parking spaces
        available.
    :cvar LESS_THAN30_SPACES_AVAILABLE: Less than 30 parking spaces
        available.
    :cvar LESS_THAN40_SPACES_AVAILABLE: Less than 40 parking spaces
        available.
    :cvar LESS_THAN50_SPACES_AVAILABLE: Less than 50 parking spaces
        available.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    NO_PARKING_SPACES_AVAILABLE = "noParkingSpacesAvailable"
    EXPECT_NO_SPACES_AVAILABLE = "expectNoSpacesAvailable"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    LESS_THAN10_SPACES_AVAILABLE = "lessThan10SpacesAvailable"
    LESS_THAN20_SPACES_AVAILABLE = "lessThan20SpacesAvailable"
    LESS_THAN30_SPACES_AVAILABLE = "lessThan30SpacesAvailable"
    LESS_THAN40_SPACES_AVAILABLE = "lessThan40SpacesAvailable"
    LESS_THAN50_SPACES_AVAILABLE = "lessThan50SpacesAvailable"
    UNKNOWN = "unknown"
    OTHER = "other"


class PaymentCardBrandsEnum(Enum):
    """
    Brands of payment cards.

    :cvar AMERICAN_EXPRESS: American Express
    :cvar CIRRUS: Cirrus
    :cvar DINERS_CLUB: Diners Club
    :cvar DISCOVER_CARD: Discover Card
    :cvar GIRO_CARD: Girocard
    :cvar MAESTRO: Maestro
    :cvar MASTER_CARD: MasterCard
    :cvar VISA: Visa
    :cvar V_PAY: V PAY
    :cvar OTHER: Other
    """
    AMERICAN_EXPRESS = "americanExpress"
    CIRRUS = "cirrus"
    DINERS_CLUB = "dinersClub"
    DISCOVER_CARD = "discoverCard"
    GIRO_CARD = "giroCard"
    MAESTRO = "maestro"
    MASTER_CARD = "masterCard"
    VISA = "visa"
    V_PAY = "vPay"
    OTHER = "other"


class PaymentCardTypesEnum(Enum):
    """
    Types of payment cards.

    :cvar CREDIT_CARD: Credit card
    :cvar DEBIT_CARD: Debit card
    :cvar CHARGE_CARD: Charge card
    :cvar FLEET_CARD: Fleet or petrol station card.
    :cvar STORED_VALUE_CARD: Stored value card / prepaid card.
    :cvar OTHER: Some other type of card.
    """
    CREDIT_CARD = "creditCard"
    DEBIT_CARD = "debitCard"
    CHARGE_CARD = "chargeCard"
    FLEET_CARD = "fleetCard"
    STORED_VALUE_CARD = "storedValueCard"
    OTHER = "other"


class PermitTypeEnum(Enum):
    """
    Type of permission for parking.

    :cvar BLUE_ZONE_PERMIT: Blue zone permit.
    :cvar CARE_TAKING_PERMIT: Permit for care taking.
    :cvar CARPOOLING_PERMIT: A permit for vehicles used for carpooling.
    :cvar CAR_SHARING_PERMIT: A permit for car sharing vehicles.
    :cvar DISABLED_PERMIT: Permit for disabled.
    :cvar EMERGENCY_VEHICLE_PERMIT: Permit for emergency vehicle.
    :cvar EMPLOYEE_PERMIT: Permit for employees.
    :cvar FAIR_PERMIT: Permit of a fair.
    :cvar GOVERNMENT_PERMIT: Vehicles that have an official parking
        permission from the appropriate (local) government.
    :cvar MAINTENANCE_VEHICLE_PERMIT: Permit for a maintenance vehicle.
    :cvar RESIDENT_PERMIT: Permit for a resident.
    :cvar ROAD_WORKS_PERMIT: Permit for road works.
    :cvar SPECIFIC_IDENTIFIED_VEHICLE_PERMIT: A specific identified
        vehicle.
    :cvar TAXI_PERMIT: Permit for a taxi.
    :cvar OTHER: Some other permit.
    """
    BLUE_ZONE_PERMIT = "blueZonePermit"
    CARE_TAKING_PERMIT = "careTakingPermit"
    CARPOOLING_PERMIT = "carpoolingPermit"
    CAR_SHARING_PERMIT = "carSharingPermit"
    DISABLED_PERMIT = "disabledPermit"
    EMERGENCY_VEHICLE_PERMIT = "emergencyVehiclePermit"
    EMPLOYEE_PERMIT = "employeePermit"
    FAIR_PERMIT = "fairPermit"
    GOVERNMENT_PERMIT = "governmentPermit"
    MAINTENANCE_VEHICLE_PERMIT = "maintenanceVehiclePermit"
    RESIDENT_PERMIT = "residentPermit"
    ROAD_WORKS_PERMIT = "roadWorksPermit"
    SPECIFIC_IDENTIFIED_VEHICLE_PERMIT = "specificIdentifiedVehiclePermit"
    TAXI_PERMIT = "taxiPermit"
    OTHER = "other"


class PersonCategoryEnum(Enum):
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


class PhysicalMountingEnum(Enum):
    """
    The ways in which equipments such as VMS are mounted or deployed on the
    road.

    :cvar CENTRAL_RESERVATION_MOUNTED: Equipment mounted in the central
        reservation.
    :cvar GANTRY_MOUNTED: Equipment mounted on an overhead gantry across
        the roadway.
    :cvar OVERHEAD_BRIDGE_MOUNTED: Equipment mounted overhead on a
        bridge structure.
    :cvar ROADSIDE_CANTILEVER_MOUNTED: Equipment mounted on a cantilever
        from the roadside.
    :cvar ROADSIDE_MOUNTED: Equipment mounted at the roadside.
    :cvar TRAILER_MOUNTED: Equipment mounted on a movable trailer.
    :cvar TUNNEL_ENTRANCE_MOUNTED: Equipment mounted on the entrance to
        a tunnel.
    :cvar VEHICLE_MOUNTED: Equipment mounted on a vehicle.
    """
    CENTRAL_RESERVATION_MOUNTED = "centralReservationMounted"
    GANTRY_MOUNTED = "gantryMounted"
    OVERHEAD_BRIDGE_MOUNTED = "overheadBridgeMounted"
    ROADSIDE_CANTILEVER_MOUNTED = "roadsideCantileverMounted"
    ROADSIDE_MOUNTED = "roadsideMounted"
    TRAILER_MOUNTED = "trailerMounted"
    TUNNEL_ENTRANCE_MOUNTED = "tunnelEntranceMounted"
    VEHICLE_MOUNTED = "vehicleMounted"


class PlacesEnum(Enum):
    """
    List of types of places.

    :cvar AROUND_BENDS_IN_THE_ROAD: Around bends in the road.
    :cvar AT_CUSTOMS_POSTS: At customs posts.
    :cvar AT_HIGH_ALTITUDES: At high altitudes.
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
    :cvar IN_THE_CITY_CENTRE: In the city centre.
    :cvar IN_THE_INNER_CITY_AREAS: In the inner city areas.
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
    """
    AROUND_BENDS_IN_THE_ROAD = "aroundBendsInTheRoad"
    AT_CUSTOMS_POSTS = "atCustomsPosts"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    AT_TOLL_PLAZAS = "atTollPlazas"
    IN_BUILT_UP_AREAS = "inBuiltUpAreas"
    IN_CONTRAFLOW_SECTIONS = "inContraflowSections"
    IN_FORESTED_AREAS = "inForestedAreas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_ROADWORKS_AREAS = "inRoadworksAreas"
    IN_RURAL_AREAS = "inRuralAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_CITY_CENTRE = "inTheCityCentre"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
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


class PollutantTypeEnum(Enum):
    """
    Types of pollutant that can be measured in the atmosphere.

    :cvar BENZENE_TOLUENE_XYLENE: Benzene, toluene or xylene.
    :cvar CARBON_MONOXIDE: Carbon monoxide.
    :cvar LEAD: Lead.
    :cvar METHANE: Methane.
    :cvar NITRIC_OXIDE: Nitric oxide.
    :cvar NITROGEN_DIOXIDE: Nitrogen dioxide.
    :cvar NITROGEN_MONOXIDE: Nitrogen monoxide.
    :cvar NITROGEN_OXIDES: Nitrogen oxides.
    :cvar NON_METHANE_HYDROCARBONS: Non-methane hydrocarbons.
    :cvar OZONE: Ozone.
    :cvar PARTICULATES10: Particulate matter which passes through a
        size-selective inlet with a 50% cut-off efficiency at an
        aerodynamic diameter of 10 µm (micrometres).
    :cvar POLYCYCLIC_AROMATIC_HYDROCARBONS: Polycyclic aromatic
        hydrocarbons.
    :cvar PRIMARY_PARTICULATE: Primary particulate particles.
    :cvar SULPHUR_DIOXIDE: Sulphur dioxide.
    :cvar TOTAL_HYDROCARBONS: Total hydrocarbons, i.e. including methane
        and non-methane.
    """
    BENZENE_TOLUENE_XYLENE = "benzeneTolueneXylene"
    CARBON_MONOXIDE = "carbonMonoxide"
    LEAD = "lead"
    METHANE = "methane"
    NITRIC_OXIDE = "nitricOxide"
    NITROGEN_DIOXIDE = "nitrogenDioxide"
    NITROGEN_MONOXIDE = "nitrogenMonoxide"
    NITROGEN_OXIDES = "nitrogenOxides"
    NON_METHANE_HYDROCARBONS = "nonMethaneHydrocarbons"
    OZONE = "ozone"
    PARTICULATES10 = "particulates10"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "polycyclicAromaticHydrocarbons"
    PRIMARY_PARTICULATE = "primaryParticulate"
    SULPHUR_DIOXIDE = "sulphurDioxide"
    TOTAL_HYDROCARBONS = "totalHydrocarbons"


class PoorEnvironmentTypeEnum(Enum):
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


class PositionAbsoluteEnum(Enum):
    """
    Absolute positions of an item within an alloted space.

    :cvar ON_LEFT: On the left of the allotted space.
    :cvar ON_RIGHT: On the right of the allotted space.
    :cvar AT_TOP: At the top of the allotted space.
    :cvar AT_BOTTOM: At the bottom of the allotted space.
    """
    ON_LEFT = "onLeft"
    ON_RIGHT = "onRight"
    AT_TOP = "atTop"
    AT_BOTTOM = "atBottom"


class PositionRelativeEnum(Enum):
    """
    Relative positions of one item to another.

    :cvar ABOVE: Positioned above relative item.
    :cvar BELOW: Positioned below relative item.
    :cvar TO_THE_LEFT: Positioned to the left of relative item.
    :cvar TO_THE_RIGHT: Positioned to the right of relative item.
    """
    ABOVE = "above"
    BELOW = "below"
    TO_THE_LEFT = "toTheLeft"
    TO_THE_RIGHT = "toTheRight"


class PrecipitationTypeEnum(Enum):
    """
    Types of precipitation.

    :cvar DRIZZLE: Light, fine rain.
    :cvar FREEZING_RAIN: Freezing rain.
    :cvar HAIL: Small balls of ice and compacted snow.
    :cvar RAIN: Rain.
    :cvar SLEET: Wet snow mixed with rain.
    :cvar SNOW: Snow.
    """
    DRIZZLE = "drizzle"
    FREEZING_RAIN = "freezingRain"
    HAIL = "hail"
    RAIN = "rain"
    SLEET = "sleet"
    SNOW = "snow"


class ProbabilityOfOccurrenceEnum(Enum):
    """
    Levels of confidence that the sender has in the information, ordered
    {certain, probable, risk of}.

    :cvar CERTAIN: The source is completely certain of the occurrence of
        the situation record version content.
    :cvar PROBABLE: The source has a reasonably high level of confidence
        of the occurrence of the situation record version content.
    :cvar RISK_OF: The source has a moderate level of confidence of the
        occurrence of the situation record version content.
    """
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"


class PublicEventType2Enum(Enum):
    """
    Additional types for a public event.

    :cvar OPEN_AIR_CONCERT: Open air concert
    :cvar SOUND_AND_LIGHT_SHOW: Sound and light show.
    :cvar ART_EVENT: Art event
    :cvar FLOWER_EVENT: Flower event
    :cvar BEER_FESTIVAL: Beer festival
    :cvar FOOD_FESTIVAL: Food festival
    :cvar WINE_FESTIVAL: Wine festival
    :cvar THEATRICAL_EVENT: Theatrical event
    :cvar FIREWORK_DISPLAY: Firework display
    :cvar STREET_FESTIVAL: Street festival
    :cvar FILM_FESTIVAL: Film festival
    :cvar UNKNOWN: Service provider does not know at time of message
        generation.
    :cvar OTHER: Some other kind of public event.
    """
    OPEN_AIR_CONCERT = "openAirConcert"
    SOUND_AND_LIGHT_SHOW = "soundAndLightShow"
    ART_EVENT = "artEvent"
    FLOWER_EVENT = "flowerEvent"
    BEER_FESTIVAL = "beerFestival"
    FOOD_FESTIVAL = "foodFestival"
    WINE_FESTIVAL = "wineFestival"
    THEATRICAL_EVENT = "theatricalEvent"
    FIREWORK_DISPLAY = "fireworkDisplay"
    STREET_FESTIVAL = "streetFestival"
    FILM_FESTIVAL = "filmFestival"
    UNKNOWN = "unknown"
    OTHER = "other"


class PublicEventTypeEnum(Enum):
    """
    Types of public events.

    :cvar AGRICULTURAL_SHOW: Agricultural show or event which could
        disrupt traffic.
    :cvar AIR_SHOW: Air show or other aeronautical event which could
        disrupt traffic.
    :cvar ATHLETICS_MEETING: Athletics event that could disrupt traffic.
    :cvar COMMERCIAL_EVENT: Commercial event which could disrupt
        traffic.
    :cvar CULTURAL_EVENT: Cultural event which could disrupt traffic.
    :cvar BALL_GAME: Ball game event that could disrupt traffic.
    :cvar BASEBALL_GAME: Baseball game event that could disrupt traffic.
    :cvar BASKETBALL_GAME: Basketball game event that could disrupt
        traffic.
    :cvar BICYCLE_RACE: Bicycle race that could disrupt traffic.
    :cvar BOAT_RACE: Regatta (boat race event of sailing, powerboat or
        rowing) that could disrupt traffic.
    :cvar BOAT_SHOW: Boat show which could disrupt traffic.
    :cvar BOXING_TOURNAMENT: Boxing event that could disrupt traffic.
    :cvar BULL_FIGHT: Bull fighting event that could disrupt traffic.
    :cvar CEREMONIAL_EVENT: Formal or religious act, rite or ceremony
        that could disrupt traffic.
    :cvar CONCERT: Concert event that could disrupt traffic.
    :cvar CRICKET_MATCH: Cricket match that could disrupt traffic.
    :cvar EXHIBITION: Major display or trade show which could disrupt
        traffic.
    :cvar FAIR: Periodic (e.g. annual), often traditional, gathering for
        entertainment or trade promotion, which could disrupt traffic.
    :cvar FESTIVAL: Celebratory event or series of events which could
        disrupt traffic.
    :cvar FILM_TVMAKING: Film or TV making event which could disrupt
        traffic.
    :cvar FOOTBALL_MATCH: Football match that could disrupt traffic.
    :cvar FUNFAIR: Periodic (e.g. annual), often traditional, gathering
        for entertainment, which could disrupt traffic.
    :cvar GARDENING_OR_FLOWER_SHOW: Gardening and/or flower show or
        event which could disrupt traffic.
    :cvar GOLF_TOURNAMENT: Golf tournament event that could disrupt
        traffic.
    :cvar HOCKEY_GAME: Hockey game event that could disrupt traffic.
    :cvar HORSE_RACE_MEETING: Horse race meeting that could disrupt
        traffic.
    :cvar INTERNATIONAL_SPORTS_MEETING: Large sporting event of an
        international nature that could disrupt traffic.
    :cvar MAJOR_EVENT: Significant organised event either on or near the
        roadway which could disrupt traffic.
    :cvar MARATHON: Marathon, cross-country or road running event that
        could disrupt traffic.
    :cvar MARKET: Periodic (e.g. weekly) gathering for buying and
        selling, which could disrupt traffic.
    :cvar MATCH: Sports match of unspecified type that could disrupt
        traffic.
    :cvar MOTOR_SHOW: Motor show which could disrupt traffic.
    :cvar MOTOR_SPORT_RACE_MEETING: Motor sport race meeting that could
        disrupt traffic.
    :cvar PARADE: Formal display or organised procession which could
        disrupt traffic.
    :cvar PROCESSION: An organised procession which could disrupt
        traffic.
    :cvar RACE_MEETING: Race meeting (other than horse or motor sport)
        that could disrupt traffic.
    :cvar RUGBY_MATCH: Rugby match that could disrupt traffic.
    :cvar SEVERAL_MAJOR_EVENTS: A series of significant organised events
        either on or near the roadway which could disrupt traffic.
    :cvar SHOW: Entertainment event that could disrupt traffic.
    :cvar SHOW_JUMPING: Horse showing jumping and tournament event that
        could disrupt traffic.
    :cvar SPORTS_MEETING: Sports event of unspecified type that could
        disrupt traffic.
    :cvar STATE_OCCASION: Public ceremony or visit of national or
        international significance which could disrupt traffic.
    :cvar TENNIS_TOURNAMENT: Tennis tournament that could disrupt
        traffic.
    :cvar TOURNAMENT: Sporting event or series of events of unspecified
        type lasting more than one day which could disrupt traffic.
    :cvar TRADE_FAIR: A periodic (e.g. annual), often traditional,
        gathering for trade promotion, which could disrupt traffic.
    :cvar WATER_SPORTS_MEETING: Water sports meeting that could disrupt
        traffic.
    :cvar WINTER_SPORTS_MEETING: Winter sports meeting or event (e.g.
        skiing, ski jumping, skating) that could disrupt traffic.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AGRICULTURAL_SHOW = "agriculturalShow"
    AIR_SHOW = "airShow"
    ATHLETICS_MEETING = "athleticsMeeting"
    COMMERCIAL_EVENT = "commercialEvent"
    CULTURAL_EVENT = "culturalEvent"
    BALL_GAME = "ballGame"
    BASEBALL_GAME = "baseballGame"
    BASKETBALL_GAME = "basketballGame"
    BICYCLE_RACE = "bicycleRace"
    BOAT_RACE = "boatRace"
    BOAT_SHOW = "boatShow"
    BOXING_TOURNAMENT = "boxingTournament"
    BULL_FIGHT = "bullFight"
    CEREMONIAL_EVENT = "ceremonialEvent"
    CONCERT = "concert"
    CRICKET_MATCH = "cricketMatch"
    EXHIBITION = "exhibition"
    FAIR = "fair"
    FESTIVAL = "festival"
    FILM_TVMAKING = "filmTVMaking"
    FOOTBALL_MATCH = "footballMatch"
    FUNFAIR = "funfair"
    GARDENING_OR_FLOWER_SHOW = "gardeningOrFlowerShow"
    GOLF_TOURNAMENT = "golfTournament"
    HOCKEY_GAME = "hockeyGame"
    HORSE_RACE_MEETING = "horseRaceMeeting"
    INTERNATIONAL_SPORTS_MEETING = "internationalSportsMeeting"
    MAJOR_EVENT = "majorEvent"
    MARATHON = "marathon"
    MARKET = "market"
    MATCH = "match"
    MOTOR_SHOW = "motorShow"
    MOTOR_SPORT_RACE_MEETING = "motorSportRaceMeeting"
    PARADE = "parade"
    PROCESSION = "procession"
    RACE_MEETING = "raceMeeting"
    RUGBY_MATCH = "rugbyMatch"
    SEVERAL_MAJOR_EVENTS = "severalMajorEvents"
    SHOW = "show"
    SHOW_JUMPING = "showJumping"
    SPORTS_MEETING = "sportsMeeting"
    STATE_OCCASION = "stateOccasion"
    TENNIS_TOURNAMENT = "tennisTournament"
    TOURNAMENT = "tournament"
    TRADE_FAIR = "tradeFair"
    WATER_SPORTS_MEETING = "waterSportsMeeting"
    WINTER_SPORTS_MEETING = "winterSportsMeeting"
    OTHER = "other"


class PublicHolidayTypeEnum(Enum):
    """
    Types of public holiday.

    :cvar BETWEEN_CHRISTMAS_AND_NEW_YEAR: The days between the Christmas
        and New Year public holidays which are not official public
        holidays.
    :cvar BOXING_DAY: The day following Christmas day.
    :cvar BRIDGE_HOLIDAY: A day between a public holiday and the
        weekend.
    :cvar CHRISTMAS_EVE: The day before Christmas day.
    :cvar CHRISTMAS_DAY_AND_BOXING_DAY: Christmas day and Boxing day
        (day following Christmas day).
    :cvar CHRISTMAS_HOLIDAY_PERIOD: The period between the Christmas and
        New Year public holidays (inclusive).
    :cvar DAY_FOLLOWING_PUBLIC_HOLIDAY: A day following a public
        holiday.
    :cvar EASTER_FRIDAY_HOLIDAY: Good Friday (the Friday prior to the
        Easter weekend).
    :cvar EASTER_HOLIDAY_PERIOD: The period between Easter Friday and
        Easter Monday (inclusive).
    :cvar EASTER_MONDAY_HOLIDAY: The Monday following the Easter
        weekend.
    :cvar EASTER_SATURDAY: The Saturday of the Easter weekend.
    :cvar EASTER_SUNDAY: Easter Sunday.
    :cvar EVE_OF_PUBLIC_HOLIDAY: The day preceding a public holiday.
    :cvar HOLIDAY_PERIOD: A holiday period.
    :cvar IN_LIEU_OF_PUBLIC_HOLIDAY: A holiday in lieu of a public
        holiday that falls on a weekend.
    :cvar JANUARY2ND_HOLIDAY: The 2nd of January holiday.
    :cvar NEW_YEARS_DAY: New Year's day.
    :cvar NEW_YEARS_EVE: The day before New Year's day.
    :cvar NOT_PUBLIC_HOLIDAY: A day that is not a public holiday.
    :cvar PUBLIC_HOLIDAY: A public holiday in the respective
        country/region.
    :cvar OTHER: None of the elements in the list. Public holiday is
        specified by 'publicHolidayName' instead.
    """
    BETWEEN_CHRISTMAS_AND_NEW_YEAR = "betweenChristmasAndNewYear"
    BOXING_DAY = "boxingDay"
    BRIDGE_HOLIDAY = "bridgeHoliday"
    CHRISTMAS_EVE = "christmasEve"
    CHRISTMAS_DAY_AND_BOXING_DAY = "christmasDayAndBoxingDay"
    CHRISTMAS_HOLIDAY_PERIOD = "christmasHolidayPeriod"
    DAY_FOLLOWING_PUBLIC_HOLIDAY = "dayFollowingPublicHoliday"
    EASTER_FRIDAY_HOLIDAY = "easterFridayHoliday"
    EASTER_HOLIDAY_PERIOD = "easterHolidayPeriod"
    EASTER_MONDAY_HOLIDAY = "easterMondayHoliday"
    EASTER_SATURDAY = "easterSaturday"
    EASTER_SUNDAY = "easterSunday"
    EVE_OF_PUBLIC_HOLIDAY = "eveOfPublicHoliday"
    HOLIDAY_PERIOD = "holidayPeriod"
    IN_LIEU_OF_PUBLIC_HOLIDAY = "inLieuOfPublicHoliday"
    JANUARY2ND_HOLIDAY = "january2ndHoliday"
    NEW_YEARS_DAY = "newYearsDay"
    NEW_YEARS_EVE = "newYearsEve"
    NOT_PUBLIC_HOLIDAY = "notPublicHoliday"
    PUBLIC_HOLIDAY = "publicHoliday"
    OTHER = "other"


@dataclass
class Reference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ReferentTypeEnum(Enum):
    """
    A set of types of known points along a linear object such as a road.

    :cvar BOUNDARY: A boundary between two jurisdictional or
        administrative areas. These may be legal boundaries such as
        between counties or countries, maintenance responsibility
        boundaries or control boundaries.
    :cvar INTERSECTION: A crossing of two or more roads where the
        precise point of intersection is defined according to specific
        business rules.
    :cvar REFERENCE_MARKER: A marker which is usually but not
        necessarily physical that is one of a sequence which are spaced
        out along the linear object (road)  to provide a location
        reference. The spacing of markers is not necessarily even.
    :cvar LANDMARK: A visible identifiable physical landmark either
        alongside or close to the linear object.
    :cvar ROAD_NODE: A topological node defined on a road network. Such
        nodes may delineate the segmentation of the road network
        according to defined business rules or may constitute a purely
        topological representation of a road network.
    """
    BOUNDARY = "boundary"
    INTERSECTION = "intersection"
    REFERENCE_MARKER = "referenceMarker"
    LANDMARK = "landmark"
    ROAD_NODE = "roadNode"


class RegulationEnum(Enum):
    """
    Regulation parameters for actions.

    :cvar PERMITTED: Permitted.
    :cvar PROHIBITED: Prohibited.
    :cvar PUNISHABLE: The action is prohibited and can be punished.
    :cvar SEASONAL_HETEROGENEOUS: It depends on the season, whether the
        action is allowed or not.
    :cvar PERMITTED_ONLY_AT_PARTICULAR_TIMES: Permitted only at
        particular times.
    :cvar PERMITTED_ONLY_ON_PARTICULAR_AREAS: Permitted only on
        particular areas (but inside the parking site ground).
    :cvar PROHIBITED_AT_PARTICULAR_TIMES: Prohibited at particular
        times.
    :cvar PROHIBITED_ON_PARTICULAR_AREAS: Prohibited on particular
        areas.
    :cvar ONLY_ON_REQUEST: Only on request (i.e. permission needed).
    :cvar HETEROGENEOUS: The regulation rule is quite complex and cannot
        be noted here.
    :cvar ONLY_OUTSIDE_BUILDINGS: Only outside buildings.
    :cvar ONLY_INSIDE_BUILDINGS: Only inside buildings.
    :cvar UNSPECIFIED: There is no regulation for this action.
    :cvar UNKNOWN: The regulation is unknown.
    :cvar OTHER: Other.
    """
    PERMITTED = "permitted"
    PROHIBITED = "prohibited"
    PUNISHABLE = "punishable"
    SEASONAL_HETEROGENEOUS = "seasonalHeterogeneous"
    PERMITTED_ONLY_AT_PARTICULAR_TIMES = "permittedOnlyAtParticularTimes"
    PERMITTED_ONLY_ON_PARTICULAR_AREAS = "permittedOnlyOnParticularAreas"
    PROHIBITED_AT_PARTICULAR_TIMES = "prohibitedAtParticularTimes"
    PROHIBITED_ON_PARTICULAR_AREAS = "prohibitedOnParticularAreas"
    ONLY_ON_REQUEST = "onlyOnRequest"
    HETEROGENEOUS = "heterogeneous"
    ONLY_OUTSIDE_BUILDINGS = "onlyOutsideBuildings"
    ONLY_INSIDE_BUILDINGS = "onlyInsideBuildings"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"


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


class RequestTypeEnum(Enum):
    """
    Types of requests that may be made by a client on a supplier.

    :cvar CATALOGUE: A request for the supplier's catalogue.
    :cvar FILTER: A request for the client's filter as currently stored
        by the supplier.
    :cvar REQUEST_DATA: A request for current data.
    :cvar REQUEST_HISTORICAL_DATA: A request for historical data, i.e.
        data which was valid within an historical time window.
    :cvar SUBSCRIPTION: A request for a client's subscription as
        currently held by a supplier.
    """
    CATALOGUE = "catalogue"
    FILTER = "filter"
    REQUEST_DATA = "requestData"
    REQUEST_HISTORICAL_DATA = "requestHistoricalData"
    SUBSCRIPTION = "subscription"


class ReroutingManagementTypeEnum(Enum):
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


class ReservationTypeEnum(Enum):
    """
    Reservation type enum.

    :cvar OPTIONAL_VALUE: Places can be reserved, but must not.
    :cvar MANDATORY: Places need to be reserved.
    :cvar NOT_AVAILABLE: Places cannot be reserved.
    :cvar PARTLY: Some places can or must be reserved, others not (do
        not use when specifying a single parking space).
    :cvar UNKNOWN: Possibility of reservation is unknown,
    :cvar UNSPECIFIED: Possibility of reservation is not specified.
    """
    OPTIONAL_VALUE = "optional"
    MANDATORY = "mandatory"
    NOT_AVAILABLE = "notAvailable"
    PARTLY = "partly"
    UNKNOWN = "unknown"
    UNSPECIFIED = "unspecified"


class ResponseEnum(Enum):
    """
    Types of response that a supplier can return to a requesting client.

    :cvar ACKNOWLEDGE: An acknowledgement that the supplier has received
        and complied with the client's request.
    :cvar CATALOGUE_REQUEST_DENIED: A notification that the supplier has
        denied the client's request for a catalogue.
    :cvar FILTER_REQUEST_DENIED: A notification that the supplier has
        denied the client's request for a filter.
    :cvar REQUEST_DENIED: A notification that the supplier has denied
        the client's request for a data.
    :cvar SUBSCRIPTION_REQUEST_DENIED: A notification that the supplier
        has denied the client's request for a subscription.
    """
    ACKNOWLEDGE = "acknowledge"
    CATALOGUE_REQUEST_DENIED = "catalogueRequestDenied"
    FILTER_REQUEST_DENIED = "filterRequestDenied"
    REQUEST_DENIED = "requestDenied"
    SUBSCRIPTION_REQUEST_DENIED = "subscriptionRequestDenied"


class RestAreaActivityEnum(Enum):
    """
    Rest area activity enum.

    :cvar OPEN_FIRE: Open fire.
    :cvar OVERNIGHT_PARKING: Overnight parking.
    :cvar PICNIC: Picnic.
    :cvar SMOKING: Smoking.
    :cvar CAMPING: Camping.
    :cvar HANDLING_HAZARDOUS_MATERIAL: Handling with hazardous material.
    :cvar BARBECUE: Barbeque.
    :cvar OTHER: Other.
    """
    OPEN_FIRE = "openFire"
    OVERNIGHT_PARKING = "overnightParking"
    PICNIC = "picnic"
    SMOKING = "smoking"
    CAMPING = "camping"
    HANDLING_HAZARDOUS_MATERIAL = "handlingHazardousMaterial"
    BARBECUE = "barbecue"
    OTHER = "other"


class RoadMaintenanceTypeEnum(Enum):
    """
    Types of road maintenance.

    :cvar CLEARANCE_WORK: Clearance work of an unspecified nature.
    :cvar CONTROLLED_AVALANCHE: Controlled avalanche work.
    :cvar INSTALLATION_WORK: Installation of new equipments or systems
        on or along-side the roadway.
    :cvar GRASS_CUTTING_WORK: Grass cutting work.
    :cvar LITTER_CLEARANCE: Work to collect litter from the roadway
        and/or adjacent verges.
    :cvar MAINTENANCE_WORK: Maintenance of road, associated
        infrastructure or equipments.
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
    """
    CLEARANCE_WORK = "clearanceWork"
    CONTROLLED_AVALANCHE = "controlledAvalanche"
    INSTALLATION_WORK = "installationWork"
    GRASS_CUTTING_WORK = "grassCuttingWork"
    LITTER_CLEARANCE = "litterClearance"
    MAINTENANCE_WORK = "maintenanceWork"
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


class RoadOperatorServiceDisruptionTypeEnum(Enum):
    """
    Types of disruption to road operator services relevant to road users.

    :cvar EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE: Emergency telephone
        number for use by public to report incidents is out of service.
    :cvar INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE: Road
        information service telephone number is out of service.
    :cvar NO_TRAFFIC_OFFICER_PATROL_SERVICE: No traffic officer patrol
        service is operating.
    """
    EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE = "emergencyTelephoneNumberOutOfService"
    INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE = "informationServiceTelephoneNumberOutOfService"
    NO_TRAFFIC_OFFICER_PATROL_SERVICE = "noTrafficOfficerPatrolService"


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
    CLEAR_ALANE_FOR_SNOWPLOUGHS_AND_GRITTING_VEHICLES = "clearALaneForSnowploughsAndGrittingVehicles"
    CLOSED_PERMANENTLY_FOR_THE_WINTER = "closedPermanentlyForTheWinter"
    CONTRAFLOW = "contraflow"
    DO_NOT_USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "doNotUseSpecifiedLanesOrCarriageways"
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
    USE_OF_SPECIFIED_LANES_OR_CARRIAGEWAYS_ALLOWED = "useOfSpecifiedLanesOrCarriagewaysAllowed"
    USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "useSpecifiedLanesOrCarriageways"
    VEHICLE_STORAGE_IN_OPERATION = "vehicleStorageInOperation"
    WEIGHT_RESTRICTION_IN_OPERATION = "weightRestrictionInOperation"
    OTHER = "other"


class RoadTypeEnum(Enum):
    """
    Categorisation of the  road type (motorway, main road, ...).

    :cvar MOTORWAY: Motorway.
    :cvar TRUNK_ROAD: Trunk road.
    :cvar MAIN_ROAD: Main road.
    :cvar OTHER: Other.
    """
    MOTORWAY = "motorway"
    TRUNK_ROAD = "trunkRoad"
    MAIN_ROAD = "mainRoad"
    OTHER = "other"


class RoadsideAssistanceTypeEnum(Enum):
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


class RoadsideServiceDisruptionTypeEnum(Enum):
    """
    Types of disruption to roadside services relevant to road users.

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
    """
    BAR_CLOSED = "barClosed"
    DIESEL_SHORTAGE = "dieselShortage"
    FUEL_SHORTAGE = "fuelShortage"
    LPG_SHORTAGE = "lpgShortage"
    METHANE_SHORTAGE = "methaneShortage"
    NO_DIESEL_FOR_HEAVY_VEHICLES = "noDieselForHeavyVehicles"
    NO_DIESEL_FOR_LIGHT_VEHICLES = "noDieselForLightVehicles"
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


class RoadworksDurationEnum(Enum):
    """
    Expected durations of roadworks in general terms.

    :cvar LONG_TERM: The roadworks are expected to last for a long term
        ( duration &gt; 6 months)
    :cvar MEDIUM_TERM: The roadworks are expected to last for a medium
        term (1 month &lt; duration &lt; = 6 months).
    :cvar SHORT_TERM: The roadworks are expected to last for a short
        term ( duration &lt; = 1 month)
    """
    LONG_TERM = "longTerm"
    MEDIUM_TERM = "mediumTerm"
    SHORT_TERM = "shortTerm"


class RoadworksScaleEnum(Enum):
    """
    Coarse classifications of the scale of roadworks in terms of the traffic
    disruption they are likely to cause.

    :cvar MAJOR: The roadworks are likely to cause major traffic
        disruption.
    :cvar MEDIUM: The roadworks are likely to cause a medium level of
        traffic disruption.
    :cvar MINOR: The roadworks are likely to cause minor traffic
        disruption.
    """
    MAJOR = "major"
    MEDIUM = "medium"
    MINOR = "minor"


class ServiceFacilityTypeEnum(Enum):
    """Service facilities available on the parking site, parking space or group
    of parking spaces.

    In distinction to equipment, a service is mostly manned.

    :cvar HOTEL: A hotel.
    :cvar MOTEL: Hotel on the motorway or other accommodation service.
    :cvar OVERNIGHT_ACCOMMODATION: OvernightAccomodation.
    :cvar SHOP: A shop of unspecified kind.
    :cvar KIOSK: Kiosk.
    :cvar FOOD_SHOPPING: Food shopping.
    :cvar CAFE: Cafe.
    :cvar RESTAURANT: Restaurant.
    :cvar RESTAURANT_SELF_SERVICE: A restaurant where people arange and
        fetch their meal themselve, this might enclose a buffet.
    :cvar MOTORWAY_RESTAURANT: Restaurant located on a motorway rest
        area.
    :cvar MOTORWAY_RESTAURANT_SMALL: Smaller type of restaurant located
        on a motorway rest area. Might be with limited offers.
    :cvar SPARE_PARTS_SHOPPING: Spare parts shopping.
    :cvar PETROL_STATION: Indicates whether it is possible to get
        petrol.
    :cvar VEHICLE_MAINTENANCE: Garage repair service.
    :cvar TYRE_REPAIR: A tyre repair service.
    :cvar TRUCK_REPAIR: Truck repair.
    :cvar TRUCK_WASH: Truck wash.
    :cvar CAR_WASH: Car wash.
    :cvar PHARMACY: Pharmacy.
    :cvar MEDICAL_FACILITY: Medical facility.
    :cvar POLICE: Indicates whether a police station is on site or very
        close.
    :cvar TOURIST_INFORMATION: Tourist information with employees.
    :cvar BIKE_SHARING: Bike Sharing.
    :cvar DOCSTOP: The site is part of the Docstop project,
        http://www.docstoponline.eu, which means medical assistance for
        professional drivers.
    :cvar LAUNDRY: A possibility for washing clothes (might also be a
        laundromat with coins).
    :cvar LEISURE_ACTIVITIES: There are leisure activities offered on
        the site or in the very near surrounding. Use the additional
        description attribute to give details.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other service facility. Use
        'otherEquipmentOrServiceFacility' to specify it.
    """
    HOTEL = "hotel"
    MOTEL = "motel"
    OVERNIGHT_ACCOMMODATION = "overnightAccommodation"
    SHOP = "shop"
    KIOSK = "kiosk"
    FOOD_SHOPPING = "foodShopping"
    CAFE = "cafe"
    RESTAURANT = "restaurant"
    RESTAURANT_SELF_SERVICE = "restaurantSelfService"
    MOTORWAY_RESTAURANT = "motorwayRestaurant"
    MOTORWAY_RESTAURANT_SMALL = "motorwayRestaurantSmall"
    SPARE_PARTS_SHOPPING = "sparePartsShopping"
    PETROL_STATION = "petrolStation"
    VEHICLE_MAINTENANCE = "vehicleMaintenance"
    TYRE_REPAIR = "tyreRepair"
    TRUCK_REPAIR = "truckRepair"
    TRUCK_WASH = "truckWash"
    CAR_WASH = "carWash"
    PHARMACY = "pharmacy"
    MEDICAL_FACILITY = "medicalFacility"
    POLICE = "police"
    TOURIST_INFORMATION = "touristInformation"
    BIKE_SHARING = "bikeSharing"
    DOCSTOP = "docstop"
    LAUNDRY = "laundry"
    LEISURE_ACTIVITIES = "leisureActivities"
    UNKNOWN = "unknown"
    OTHER = "other"


class SeverityEnum(Enum):
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
    """
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE_VALUE = "none"
    UNKNOWN = "unknown"


@dataclass
class SituationRecordExtendedApproved:
    """
    Extension class for SituationRecord.

    :ivar safety_related_message: Indicates, whether this
        SituationRecord specifies a safety related message according to
        Commission Delegated Regulation (EU) No 886/2013.
    """
    safety_related_message: Optional[bool] = field(
        default=None,
        metadata={
            "name": "safetyRelatedMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


class SourceTypeEnum(Enum):
    """
    Type of sources from which situation information may be derived.

    :cvar AUTOMOBILE_CLUB_PATROL: A patrol of an automobile club.
    :cvar CAMERA_OBSERVATION: A camera observation (either still or
        video camera).
    :cvar FREIGHT_VEHICLE_OPERATOR: An operator of freight vehicles.
    :cvar INDUCTION_LOOP_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing inductive loop
        information.
    :cvar INFRARED_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing infrared image
        information.
    :cvar MICROWAVE_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing microwave
        information.
    :cvar MOBILE_TELEPHONE_CALLER: A caller using a mobile telephone
        (who may or may not be on the road network).
    :cvar NON_POLICE_EMERGENCY_SERVICE_PATROL: Emergency service patrols
        other than police.
    :cvar OTHER_INFORMATION: Other sources of information.
    :cvar OTHER_OFFICIAL_VEHICLE: Personnel from a vehicle belonging to
        the road operator or authority or any emergency service,
        including authorised breakdown service organisations.
    :cvar POLICE_PATROL: A police patrol.
    :cvar PRIVATE_BREAKDOWN_SERVICE: A private breakdown service.
    :cvar PUBLIC_AND_PRIVATE_UTILITIES: A utility organisation, either
        public or private.
    :cvar REGISTERED_MOTORIST_OBSERVER: A motorist who is an officially
        registered observer.
    :cvar ROAD_AUTHORITIES: A road authority.
    :cvar ROAD_OPERATOR_PATROL: A patrol of the road operator or
        authority.
    :cvar ROADSIDE_TELEPHONE_CALLER: A caller who is using an emergency
        roadside telephone.
    :cvar SPOTTER_AIRCRAFT: A spotter aircraft of an organisation
        specifically assigned to the monitoring of the traffic network.
    :cvar TRAFFIC_MONITORING_STATION: A station, usually automatic,
        dedicated to the monitoring of the road network.
    :cvar TRANSIT_OPERATOR: An operator of a transit service, e.g. bus
        link operator.
    :cvar VEHICLE_PROBE_MEASUREMENT: A specially equipped vehicle used
        to provide measurements.
    :cvar VIDEO_PROCESSING_MONITORING_STATION: A station dedicated to
        the monitoring of the road network by processing video image
        information.
    """
    AUTOMOBILE_CLUB_PATROL = "automobileClubPatrol"
    CAMERA_OBSERVATION = "cameraObservation"
    FREIGHT_VEHICLE_OPERATOR = "freightVehicleOperator"
    INDUCTION_LOOP_MONITORING_STATION = "inductionLoopMonitoringStation"
    INFRARED_MONITORING_STATION = "infraredMonitoringStation"
    MICROWAVE_MONITORING_STATION = "microwaveMonitoringStation"
    MOBILE_TELEPHONE_CALLER = "mobileTelephoneCaller"
    NON_POLICE_EMERGENCY_SERVICE_PATROL = "nonPoliceEmergencyServicePatrol"
    OTHER_INFORMATION = "otherInformation"
    OTHER_OFFICIAL_VEHICLE = "otherOfficialVehicle"
    POLICE_PATROL = "policePatrol"
    PRIVATE_BREAKDOWN_SERVICE = "privateBreakdownService"
    PUBLIC_AND_PRIVATE_UTILITIES = "publicAndPrivateUtilities"
    REGISTERED_MOTORIST_OBSERVER = "registeredMotoristObserver"
    ROAD_AUTHORITIES = "roadAuthorities"
    ROAD_OPERATOR_PATROL = "roadOperatorPatrol"
    ROADSIDE_TELEPHONE_CALLER = "roadsideTelephoneCaller"
    SPOTTER_AIRCRAFT = "spotterAircraft"
    TRAFFIC_MONITORING_STATION = "trafficMonitoringStation"
    TRANSIT_OPERATOR = "transitOperator"
    VEHICLE_PROBE_MEASUREMENT = "vehicleProbeMeasurement"
    VIDEO_PROCESSING_MONITORING_STATION = "videoProcessingMonitoringStation"


class SpecialDayTypeEnum(Enum):
    """
    Collection of general types of days.

    :cvar BICYCLE_RACE_DAY: Day of local bicycle race.
    :cvar BULL_FIGHT_DAY: Day of local bullfight.
    :cvar CARNIVAL_DAY: Day of a local carnival involving a procession
        along roads.
    :cvar EXHIBITION_DAY: Day of a local exhibition.
    :cvar FESTIVAL_DAY: Day of a local festival.
    :cvar GAMES_DAY: Day of local games (e.g. highland games in
        Scotland).
    :cvar HORSE_RACE_MEETING_DAY: Day of a local horse race meeting.
    :cvar HUNT_MEETING_DAY: Day of a local hunt meeting.
    :cvar MARATHON_RACE_DAY: Day of local marathon race.
    :cvar MARKET_DAY: Day of a local market.
    :cvar MOTOR_SPORT_RACE_MEETING_DAY: Day of a local motor sport race
        meeting.
    :cvar NON_WORKING_DAY: A non-working day in the specific
        country/region.
    :cvar RACE_MEETING_DAY: Day of a local race meeting (other than
        horse or motor sport).
    :cvar REGATTA_DAY: Day of a local regatta.
    :cvar SHOW_DAY: Day of a local show.
    :cvar SPORTS_MEETING_DAY: Day of a local sports meeting.
    :cvar WORKING_DAY: A working day in the specific country/region.
    :cvar SCHOOL_DAY: School day.
    :cvar ELECTION_DAY: Election day.
    :cvar PUBLIC_HOLIDAY: Public holiday.
    :cvar HOLIDAYS: A day within the school holidays. You can use the
        PublicHoliday class to specify more details.
    :cvar UNDEFINED_DAY_TYPE: UndefinedDayType
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    BICYCLE_RACE_DAY = "bicycleRaceDay"
    BULL_FIGHT_DAY = "bullFightDay"
    CARNIVAL_DAY = "carnivalDay"
    EXHIBITION_DAY = "exhibitionDay"
    FESTIVAL_DAY = "festivalDay"
    GAMES_DAY = "gamesDay"
    HORSE_RACE_MEETING_DAY = "horseRaceMeetingDay"
    HUNT_MEETING_DAY = "huntMeetingDay"
    MARATHON_RACE_DAY = "marathonRaceDay"
    MARKET_DAY = "marketDay"
    MOTOR_SPORT_RACE_MEETING_DAY = "motorSportRaceMeetingDay"
    NON_WORKING_DAY = "nonWorkingDay"
    RACE_MEETING_DAY = "raceMeetingDay"
    REGATTA_DAY = "regattaDay"
    SHOW_DAY = "showDay"
    SPORTS_MEETING_DAY = "sportsMeetingDay"
    WORKING_DAY = "workingDay"
    SCHOOL_DAY = "schoolDay"
    ELECTION_DAY = "electionDay"
    PUBLIC_HOLIDAY = "publicHoliday"
    HOLIDAYS = "holidays"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
    UNKNOWN = "unknown"
    OTHER = "other"


class SpeedManagementTypeEnum(Enum):
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
    """
    ACTIVE_SPEED_CONTROL_IN_OPERATION = "activeSpeedControlInOperation"
    DO_NOT_SLOWDOWN_UNNECESSARILY = "doNotSlowdownUnnecessarily"
    OBSERVE_SPEED_LIMIT = "observeSpeedLimit"
    POLICE_SPEED_CHECKS_IN_OPERATION = "policeSpeedChecksInOperation"
    REDUCE_YOUR_SPEED = "reduceYourSpeed"
    SPEED_RESTRICTION_IN_OPERATION = "speedRestrictionInOperation"
    OTHER = "other"


class SubjectTypeOfWorksEnum(Enum):
    """
    Subject types of construction or maintenance work.

    :cvar BRIDGE: Bridge on, over or under the highway.
    :cvar BURIED_CABLES: Buried cables under or along the highway.
    :cvar BURIED_SERVICES: Unspecified buried services on, under or
        along the highway.
    :cvar CRASH_BARRIER: Crash barrier.
    :cvar GALLERY: Gallery.
    :cvar GANTRY: Gantry over or above the roadway.
    :cvar GAS_MAIN_WORK: Gas mains.
    :cvar INTERCHANGE: Motorway or major road interchange.
    :cvar JUNCTION: Motorway or major road junction.
    :cvar LEVEL_CROSSING: Level-crossing or associated equipment.
    :cvar LIGHTING_SYSTEM: Road lighting system.
    :cvar MEASUREMENT_EQUIPMENT: Equipment used for determining traffic
        measurements.
    :cvar NOISE_PROTECTION: Installations along the roadway designed to
        reduce road noise in the surrounding environment.
    :cvar ROAD: Road.
    :cvar ROADSIDE_DRAINS: Roadside drains.
    :cvar ROADSIDE_EMBANKMENT: Roadside embankment.
    :cvar ROADSIDE_EQUIPMENT: Roadside equipment.
    :cvar ROAD_SIGNS: Road signs.
    :cvar ROUNDABOUT: Roundabout.
    :cvar TOLL_GATE: Toll gate.
    :cvar TUNNEL: Road tunnel.
    :cvar WATER_MAIN: Water main under or along the highway.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    BRIDGE = "bridge"
    BURIED_CABLES = "buriedCables"
    BURIED_SERVICES = "buriedServices"
    CRASH_BARRIER = "crashBarrier"
    GALLERY = "gallery"
    GANTRY = "gantry"
    GAS_MAIN_WORK = "gasMainWork"
    INTERCHANGE = "interchange"
    JUNCTION = "junction"
    LEVEL_CROSSING = "levelCrossing"
    LIGHTING_SYSTEM = "lightingSystem"
    MEASUREMENT_EQUIPMENT = "measurementEquipment"
    NOISE_PROTECTION = "noiseProtection"
    ROAD = "road"
    ROADSIDE_DRAINS = "roadsideDrains"
    ROADSIDE_EMBANKMENT = "roadsideEmbankment"
    ROADSIDE_EQUIPMENT = "roadsideEquipment"
    ROAD_SIGNS = "roadSigns"
    ROUNDABOUT = "roundabout"
    TOLL_GATE = "tollGate"
    TUNNEL = "tunnel"
    WATER_MAIN = "waterMain"
    OTHER = "other"


class SubscriptionStateEnum(Enum):
    """
    The state of a client's current subscription.

    :cvar ACTIVE: The client's subscription as registered with a
        supplier is currently active.
    :cvar SUSPENDED: The client's subscription as registered with a
        supplier is currently suspended.
    """
    ACTIVE = "active"
    SUSPENDED = "suspended"


class TimePrecisionEnum(Enum):
    """
    List of precisions to which times can be given.

    :cvar TENTHS_OF_SECOND: Time given to the nearest tenth of a second.
    :cvar SECOND: Time given to the nearest second.
    :cvar MINUTE: Time given to the nearest minute.
    :cvar QUARTER_HOUR: Time given to the nearest quarter hour.
    :cvar HALF_HOUR: Time given to the nearest half hour.
    :cvar HOUR: Time given to the nearest hour.
    """
    TENTHS_OF_SECOND = "tenthsOfSecond"
    SECOND = "second"
    MINUTE = "minute"
    QUARTER_HOUR = "quarterHour"
    HALF_HOUR = "halfHour"
    HOUR = "hour"


class TpegLoc01AreaLocationSubtypeEnum(Enum):
    """
    Types of area.

    :cvar LARGE_AREA: A geographic or geometric large area.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    LARGE_AREA = "largeArea"
    OTHER = "other"


class TpegLoc01FramedPointLocationSubtypeEnum(Enum):
    """
    Types of points on the road network framed by two other points on the same
    road.

    :cvar FRAMED_POINT: A point on the road network framed by two other
        points on the same road.
    """
    FRAMED_POINT = "framedPoint"


class TpegLoc01LinearLocationSubtypeEnum(Enum):
    """
    Types of linear location.

    :cvar SEGMENT: A segment (or link) of the road network corresponding
        to the way in which the road operator has segmented the network.
    """
    SEGMENT = "segment"


class TpegLoc01SimplePointLocationSubtypeEnum(Enum):
    """
    Types of simple point.

    :cvar INTERSECTION: An point on the road network at which one or
        more roads intersect.
    :cvar NON_LINKED_POINT: A point on the road network which is not at
        a junction or intersection.
    """
    INTERSECTION = "intersection"
    NON_LINKED_POINT = "nonLinkedPoint"


class TpegLoc03AreaDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing area locations.

    :cvar ADMINISTRATIVE_AREA_NAME: Name of an administrative area.
    :cvar ADMINISTRATIVE_REFERENCE_NAME: Reference name by which
        administrative area is known.
    :cvar AREA_NAME: Name of an area.
    :cvar COUNTY_NAME: Name of a county (administrative sub-division).
    :cvar LAKE_NAME: Name of a lake.
    :cvar NATION_NAME: Name of a nation (e.g. Wales) which is a sub-
        division of a ISO recognised country.
    :cvar POLICE_FORCE_CONTROL_AREA_NAME: Name of a police force control
        area.
    :cvar REGION_NAME: Name of a geographic region.
    :cvar SEA_NAME: Name of a sea.
    :cvar TOWN_NAME: Name of a town.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AREA_NAME = "areaName"
    COUNTY_NAME = "countyName"
    LAKE_NAME = "lakeName"
    NATION_NAME = "nationName"
    POLICE_FORCE_CONTROL_AREA_NAME = "policeForceControlAreaName"
    REGION_NAME = "regionName"
    SEA_NAME = "seaName"
    TOWN_NAME = "townName"
    OTHER = "other"


class TpegLoc03IlcPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing a junction by identifying the intersecting roads
    at a road junction.

    :cvar TPEG_ILC_NAME1: The name of the road on which the junction
        point is located.
    :cvar TPEG_ILC_NAME2: The name of the first intersecting road at the
        junction.
    :cvar TPEG_ILC_NAME3: The name of the second intersecting road (if
        one exists) at the junction.
    """
    TPEG_ILC_NAME1 = "tpegIlcName1"
    TPEG_ILC_NAME2 = "tpegIlcName2"
    TPEG_ILC_NAME3 = "tpegIlcName3"


class TpegLoc03JunctionPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing a point at a road junction.

    :cvar JUNCTION_NAME: Name of a road network junction where two or
        more roads join.
    """
    JUNCTION_NAME = "junctionName"


class TpegLoc03OtherPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors other than junction names and road descriptors which can help
    to identify the location of points on the road network.

    :cvar ADMINISTRATIVE_AREA_NAME: Name of an administrative area.
    :cvar ADMINISTRATIVE_REFERENCE_NAME: Reference name by which an
        administrative area is known.
    :cvar AIRPORT_NAME: Name of an airport.
    :cvar AREA_NAME: Name of an area.
    :cvar BUILDING_NAME: Name of a building.
    :cvar BUS_STOP_IDENTIFIER: Identifier of a bus stop on the road
        network.
    :cvar BUS_STOP_NAME: Name of a bus stop on the road network.
    :cvar CANAL_NAME: Name of a canal.
    :cvar COUNTY_NAME: Name of a county (administrative sub-division).
    :cvar FERRY_PORT_NAME: Name of a ferry port.
    :cvar INTERSECTION_NAME: Name of a road network intersection.
    :cvar LAKE_NAME: Name of a lake.
    :cvar LINK_NAME: Name of a road link.
    :cvar LOCAL_LINK_NAME: Local name of a road link.
    :cvar METRO_STATION_NAME: Name of a metro/underground station.
    :cvar NATION_NAME: Name of a nation (e.g. Wales) which is a sub-
        division of a ISO recognised country.
    :cvar NON_LINKED_POINT_NAME: Name of a point on the road network
        which is not at a junction or intersection.
    :cvar PARKING_FACILITY_NAME: Name of a parking facility.
    :cvar POINT_NAME: Name of a specific point.
    :cvar POINT_OF_INTEREST_NAME: Name of a general point of interest.
    :cvar RAILWAY_STATION: Name of a railway station.
    :cvar REGION_NAME: Name of a geographic region.
    :cvar RIVER_NAME: Name of a river.
    :cvar SEA_NAME: Name of a sea.
    :cvar SERVICE_AREA_NAME: Name of a service area on a road network.
    :cvar TIDAL_RIVER_NAME: Name of a river which is of a tidal nature.
    :cvar TOWN_NAME: Name of a town.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AIRPORT_NAME = "airportName"
    AREA_NAME = "areaName"
    BUILDING_NAME = "buildingName"
    BUS_STOP_IDENTIFIER = "busStopIdentifier"
    BUS_STOP_NAME = "busStopName"
    CANAL_NAME = "canalName"
    COUNTY_NAME = "countyName"
    FERRY_PORT_NAME = "ferryPortName"
    INTERSECTION_NAME = "intersectionName"
    LAKE_NAME = "lakeName"
    LINK_NAME = "linkName"
    LOCAL_LINK_NAME = "localLinkName"
    METRO_STATION_NAME = "metroStationName"
    NATION_NAME = "nationName"
    NON_LINKED_POINT_NAME = "nonLinkedPointName"
    PARKING_FACILITY_NAME = "parkingFacilityName"
    POINT_NAME = "pointName"
    POINT_OF_INTEREST_NAME = "pointOfInterestName"
    RAILWAY_STATION = "railwayStation"
    REGION_NAME = "regionName"
    RIVER_NAME = "riverName"
    SEA_NAME = "seaName"
    SERVICE_AREA_NAME = "serviceAreaName"
    TIDAL_RIVER_NAME = "tidalRiverName"
    TOWN_NAME = "townName"
    OTHER = "other"


class TpegLoc04HeightTypeEnum(Enum):
    """
    Types of height.

    :cvar ABOVE: Height above specified location.
    :cvar ABOVE_SEA_LEVEL: Height above mean sea high water level.
    :cvar ABOVE_STREET_LEVEL: Height above street level.
    :cvar AT: At height of specified location.
    :cvar AT_SEA_LEVEL: At mean sea high water level.
    :cvar AT_STREET_LEVEL: At street level.
    :cvar BELOW: Height below specified location.
    :cvar BELOW_SEA_LEVEL: Height below mean sea high water level.
    :cvar BELOW_STREET_LEVEL: Height below street level.
    :cvar UNDEFINED: Undefined height reference.
    :cvar UNKNOWN: Unknown height reference.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABOVE = "above"
    ABOVE_SEA_LEVEL = "aboveSeaLevel"
    ABOVE_STREET_LEVEL = "aboveStreetLevel"
    AT = "at"
    AT_SEA_LEVEL = "atSeaLevel"
    AT_STREET_LEVEL = "atStreetLevel"
    BELOW = "below"
    BELOW_SEA_LEVEL = "belowSeaLevel"
    BELOW_STREET_LEVEL = "belowStreetLevel"
    UNDEFINED = "undefined"
    UNKNOWN = "unknown"
    OTHER = "other"


class TrafficConstrictionTypeEnum(Enum):
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
    """
    CARRIAGEWAY_BLOCKED = "carriagewayBlocked"
    CARRIAGEWAY_PARTIALLY_OBSTRUCTED = "carriagewayPartiallyObstructed"
    LANES_BLOCKED = "lanesBlocked"
    LANES_PARTIALLY_OBSTRUCTED = "lanesPartiallyObstructed"
    ROAD_BLOCKED = "roadBlocked"
    ROAD_PARTIALLY_OBSTRUCTED = "roadPartiallyObstructed"


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


class TrafficStatusEnum(Enum):
    """
    List of terms used to describe traffic conditions.

    :cvar IMPOSSIBLE: Traffic in the specified direction is completely
        congested, effectively at a standstill, making driving
        impossible.
    :cvar CONGESTED: Traffic in the specified direction is congested
        making driving very slow and difficult.
    :cvar HEAVY: Traffic in the specified direction is heavier than
        usual making driving conditions more difficult than normal.
    :cvar FREE_FLOW: Traffic in the specified direction is free flowing.
    :cvar UNKNOWN: Traffic conditions are unknown.
    """
    IMPOSSIBLE = "impossible"
    CONGESTED = "congested"
    HEAVY = "heavy"
    FREE_FLOW = "freeFlow"
    UNKNOWN = "unknown"


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


class TrafficTypeEnum(Enum):
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


class TransitServiceInformationEnum(Enum):
    """
    Types of public transport information.

    :cvar CANCELLATIONS: Public transport, park-and-ride, rail or bus
        services will be cancelled until the specified time.
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
        at no charge between specified locations until the specified
        time.
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
    :cvar SERVICE_NOT_OPERATING: The specified service is not operating
        until the specified time.
    :cvar SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE: The
        specified service is not operating but an alternative service is
        available.
    :cvar SERVICE_SUSPENDED: The specified service has been suspended
        until the specified time.
    :cvar SERVICE_WITHDRAWN: The specified service has been cancelled.
    :cvar SHUTTLE_SERVICE_OPERATING: A shuttle service is operating
        between the specified locations until the specified time.
    :cvar TEMPORARY_CHANGES_TO_TIMETABLES: The timetable for the
        specified service is subject to temporary changes.
    :cvar OTHER: Other than as defined in this enumeration.
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


class TransitServiceTypeEnum(Enum):
    """
    Types of transport services available to the general public.

    :cvar AIR: Air service.
    :cvar BUS: Bus service.
    :cvar FERRY: Ferry service.
    :cvar HYDROFOIL: Hydrofoil service.
    :cvar RAIL: Rail service.
    :cvar TRAM: Tram service.
    :cvar UNDERGROUND_METRO: Underground or metro service.
    """
    AIR = "air"
    BUS = "bus"
    FERRY = "ferry"
    HYDROFOIL = "hydrofoil"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND_METRO = "undergroundMetro"


class TravelTimeTrendTypeEnum(Enum):
    """
    List of terms used to describe the trend in travel times.

    :cvar DECREASING: Travel times are decreasing.
    :cvar INCREASING: Travel times are increasing.
    :cvar STABLE: Travel times are stable.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"


class TravelTimeTypeEnum(Enum):
    """
    List of ways in which travel times are derived.

    :cvar BEST: Travel time is derived from the best out of a monitored
        sample.
    :cvar ESTIMATED: Travel time is an automated estimate.
    :cvar INSTANTANEOUS: Travel time is derived from instantaneous
        measurements.
    :cvar RECONSTITUTED: Travel time is reconstituted from other
        measurements.
    """
    BEST = "best"
    ESTIMATED = "estimated"
    INSTANTANEOUS = "instantaneous"
    RECONSTITUTED = "reconstituted"


class TruckParkingDynamicManagementEnum(Enum):
    """
    Dynamic parking mode enum.

    :cvar COMPACT_PARKING: Lorries are parking one after the other in
        different lanes; each lane has a dedicated time of departure
        (which might be displayed on a sign gantry).
    :cvar QUEUE_PARKING: Lorries are parking in queues, one after the
        other. Each lorry must have an earlier time of departure than
        all the lorries behind it.
    :cvar NO_DYNAMIC_PARKING_MANAGEMENT: No dynamic parking management.
    :cvar OTHER: Some other type of dynamic parking management.
    """
    COMPACT_PARKING = "compactParking"
    QUEUE_PARKING = "queueParking"
    NO_DYNAMIC_PARKING_MANAGEMENT = "noDynamicParkingManagement"
    OTHER = "other"


class UpdateMethodEnum(Enum):
    """
    The types of updates of situations that may be requested by a client.

    :cvar ALL_ELEMENT_UPDATE: The client has currently requested that
        all situation elements are sent when one or more component
        elements are updated.
    :cvar SINGLE_ELEMENT_UPDATE: The client has currently requested that
        only the individual elements of a situation that have changed
        are sent when updated.
    :cvar SNAPSHOT: The client has requested that all situations and
        their elements which are valid at the time of request be sent
        together, i.e. a snapshot in time of all valid situations.
    """
    ALL_ELEMENT_UPDATE = "allElementUpdate"
    SINGLE_ELEMENT_UPDATE = "singleElementUpdate"
    SNAPSHOT = "snapshot"


class UrbanParkingSiteTypeEnum(Enum):
    """
    The type of an urban parking site.

    :cvar ON_STREET_PARKING: Vehicles are parking on the roadside.
    :cvar OFF_STREET_PARKING: Vehicles are parking off the road, e.g. on
        a parking space, a car park or some other area designed for
        parking.
    :cvar OTHER: The parking is associated with some other location.
    """
    ON_STREET_PARKING = "onStreetParking"
    OFF_STREET_PARKING = "offStreetParking"
    OTHER = "other"


class UrgencyEnum(Enum):
    """
    Degrees of urgency that a receiving client should associate with the
    disseminate of the information contained in the publication.

    :cvar EXTREMELY_URGENT: Dissemination of the information is
        extremely urgent.
    :cvar URGENT: Dissemination of the information is urgent.
    :cvar NORMAL_URGENCY: Dissemination of the information is of normal
        urgency.
    """
    EXTREMELY_URGENT = "extremelyUrgent"
    URGENT = "urgent"
    NORMAL_URGENCY = "normalUrgency"


class UrlLinkTypeEnum(Enum):
    """
    Types of URL links.

    :cvar DOCUMENT_PDF: URL link to a pdf document.
    :cvar HTML: URL link to an html page.
    :cvar IMAGE: URL link to an image.
    :cvar RSS: URL link to an RSS feed.
    :cvar VIDEO_STREAM: URL link to a video stream.
    :cvar VOICE_STREAM: URL link to a voice stream.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    DOCUMENT_PDF = "documentPdf"
    HTML = "html"
    IMAGE = "image"
    RSS = "rss"
    VIDEO_STREAM = "videoStream"
    VOICE_STREAM = "voiceStream"
    OTHER = "other"


class UserTypeEnum(Enum):
    """
    Types of users; used for parking but also for usage of equipment and
    services.

    :cvar ALL_USERS: All users.
    :cvar SHOPPERS: Shoppers.
    :cvar HOTEL_GUESTS: Hotel guests.
    :cvar SUBSCRIBERS: Subscribers.
    :cvar RESERVATION_HOLDERS: Those who have a valid reservation for
        the duration of parking.
    :cvar SEASON_TICKET_HOLDERS: Season ticket holders.
    :cvar REGISTERED_DISABLED_USERS: Registered disabled persons.
    :cvar DISABLED: Physically impaired people.
    :cvar HANDICAPPED: Persons with deficiencies in their daily life.
    :cvar HEARING_IMPAIRED: People with difficulties to hear.
    :cvar VISUALLY_IMPAIRED: People with difficulties to see.
    :cvar WHEELCHAIR_USERS: Wheelchair users.
    :cvar ELDERLY_USERS: Elderly users.
    :cvar FAMILIES: Families.
    :cvar MEN: Men.
    :cvar WOMEN: Women.
    :cvar PREGNANT_WOMEN: Pregnant women.
    :cvar PENSIONERS: Pensioners.
    :cvar STUDENTS: Students.
    :cvar STAFF: Staff.
    :cvar EMPLOYEES: Employees.
    :cvar CUSTOMERS: Customers.
    :cvar VISITORS: Visitors.
    :cvar MEMBERS: Members.
    :cvar SHORT_TERM_PARKER: Short-term parker.
    :cvar LONG_TERM_PARKER: Long-term parker.
    :cvar OVERNIGHT_PARKER: Overnight parker.
    :cvar SPORT_EVENT_AWAY_SUPPORTERS: Sport event away supporters.
    :cvar SPORT_EVENT_HOME_SUPPORTERS: Sport event home supporters.
    :cvar RESIDENTS: Local residents.
    :cvar COMMUTERS: Commuters.
    :cvar PARK_AND_RIDE_USERS: Users that are changing into public
        transport at this parking.
    :cvar PARK_AND_WALK_USER: Park and walk user.
    :cvar PARK_AND_CYCLE_USER: Park and cycle user.
    :cvar OTHER: Other.
    :cvar UNKNOWN: Unknown.
    """
    ALL_USERS = "allUsers"
    SHOPPERS = "shoppers"
    HOTEL_GUESTS = "hotelGuests"
    SUBSCRIBERS = "subscribers"
    RESERVATION_HOLDERS = "reservationHolders"
    SEASON_TICKET_HOLDERS = "seasonTicketHolders"
    REGISTERED_DISABLED_USERS = "registeredDisabledUsers"
    DISABLED = "disabled"
    HANDICAPPED = "handicapped"
    HEARING_IMPAIRED = "hearingImpaired"
    VISUALLY_IMPAIRED = "visuallyImpaired"
    WHEELCHAIR_USERS = "wheelchairUsers"
    ELDERLY_USERS = "elderlyUsers"
    FAMILIES = "families"
    MEN = "men"
    WOMEN = "women"
    PREGNANT_WOMEN = "pregnantWomen"
    PENSIONERS = "pensioners"
    STUDENTS = "students"
    STAFF = "staff"
    EMPLOYEES = "employees"
    CUSTOMERS = "customers"
    VISITORS = "visitors"
    MEMBERS = "members"
    SHORT_TERM_PARKER = "shortTermParker"
    LONG_TERM_PARKER = "longTermParker"
    OVERNIGHT_PARKER = "overnightParker"
    SPORT_EVENT_AWAY_SUPPORTERS = "sportEventAwaySupporters"
    SPORT_EVENT_HOME_SUPPORTERS = "sportEventHomeSupporters"
    RESIDENTS = "residents"
    COMMUTERS = "commuters"
    PARK_AND_RIDE_USERS = "parkAndRideUsers"
    PARK_AND_WALK_USER = "parkAndWalkUser"
    PARK_AND_CYCLE_USER = "parkAndCycleUser"
    OTHER = "other"
    UNKNOWN = "unknown"


class ValidityStatusEnum(Enum):
    """
    Values of validity status that can be assigned to a described event, action
    or item.

    :cvar ACTIVE: The described event, action or item is currently
        active regardless of the definition of the validity time
        specification.
    :cvar SUSPENDED: The described event, action or item is currently
        suspended, that is inactive, regardless of the definition of the
        validity time specification.
    :cvar DEFINED_BY_VALIDITY_TIME_SPEC: The validity status of the
        described event, action or item is in accordance with the
        definition of the validity time specification.
    """
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"


class VehicleEquipmentEnum(Enum):
    """
    Types of vehicle equipment in use or on board.

    :cvar NOT_USING_SNOW_CHAINS: Vehicle not using snow chains.
    :cvar NOT_USING_SNOW_CHAINS_OR_TYRES: Vehicle not using either snow
        tyres or snow chains.
    :cvar SNOW_CHAINS_IN_USE: Vehicle using snow chains.
    :cvar SNOW_TYRES_IN_USE: Vehicle using snow tyres.
    :cvar SNOW_CHAINS_OR_TYRES_IN_USE: Vehicle using snow tyres or snow
        chains.
    :cvar WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD: Vehicle which is not
        carrying on board snow tyres or chains.
    """
    NOT_USING_SNOW_CHAINS = "notUsingSnowChains"
    NOT_USING_SNOW_CHAINS_OR_TYRES = "notUsingSnowChainsOrTyres"
    SNOW_CHAINS_IN_USE = "snowChainsInUse"
    SNOW_TYRES_IN_USE = "snowTyresInUse"
    SNOW_CHAINS_OR_TYRES_IN_USE = "snowChainsOrTyresInUse"
    WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD = "withoutSnowTyresOrChainsOnBoard"


class VehicleObstructionTypeEnum(Enum):
    """
    Types of obstructions involving vehicles.

    :cvar ABANDONED_VEHICLE: Abandoned vehicle(s) on the roadway which
        may cause traffic disruption.
    :cvar ABNORMAL_LOAD: Vehicle(s) carrying exceptional load(s) which
        may cause traffic disruption.
    :cvar BROKEN_DOWN_BUS: Broken down passenger vehicle(s) on the
        carriageway which may cause traffic disruption.
    :cvar BROKEN_DOWN_HEAVY_LORRY: Broken down heavy lorry/lorries on
        the carriageway which may cause traffic disruption.
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
    :cvar MILITARY_CONVOY: A group of military vehicles moving together
        in formation which may cause traffic disruption.
    :cvar OVERHEIGHT_VEHICLE: Vehicles of height greater than normally
        allowed which may cause traffic disruption.
    :cvar PROHIBITED_VEHICLE_ON_THE_ROADWAY: Vehicles not normally
        permitted on the highway are present which may cause traffic
        disruption.
    :cvar SALTING_OR_GRITTING_VEHICLE_IN_USE: Salting and gritting
        vehicles are in use which may cause traffic disruption.
    :cvar SLOW_MOVING_MAINTENANCE_VEHICLE: Slow moving vehicles
        undertaking maintenance work may pose a hazard to other vehicles
        on the carriageway.
    :cvar SLOW_VEHICLE: A vehicle travelling at well below normal
        highway speeds which may cause traffic disruption.
    :cvar SNOWPLOUGH: Snowploughs are in use which may cause traffic
        disruption.
    :cvar TRACK_LAYING_VEHICLE: Tracked vehicles are in use which may
        cause traffic disruption.
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
    :cvar VEHICLE_STUCK_UNDER_BRIDGE: A vehicle is stuck under a bridge.
    :cvar VEHICLE_WITH_OVERHEIGHT_LOAD: An over-height vehicle which may
        present a hazard to road users.
    :cvar VEHICLE_WITH_OVERWIDE_LOAD: A vehicle of width greater than
        that normally allowed which may cause traffic disruption.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABANDONED_VEHICLE = "abandonedVehicle"
    ABNORMAL_LOAD = "abnormalLoad"
    BROKEN_DOWN_BUS = "brokenDownBus"
    BROKEN_DOWN_HEAVY_LORRY = "brokenDownHeavyLorry"
    BROKEN_DOWN_VEHICLE = "brokenDownVehicle"
    CONVOY = "convoy"
    DAMAGED_VEHICLE = "damagedVehicle"
    DANGEROUS_SLOW_MOVING_VEHICLE = "dangerousSlowMovingVehicle"
    EMERGENCY_VEHICLE = "emergencyVehicle"
    HIGH_SPEED_EMERGENCY_VEHICLE = "highSpeedEmergencyVehicle"
    LONG_LOAD = "longLoad"
    MILITARY_CONVOY = "militaryConvoy"
    OVERHEIGHT_VEHICLE = "overheightVehicle"
    PROHIBITED_VEHICLE_ON_THE_ROADWAY = "prohibitedVehicleOnTheRoadway"
    SALTING_OR_GRITTING_VEHICLE_IN_USE = "saltingOrGrittingVehicleInUse"
    SLOW_MOVING_MAINTENANCE_VEHICLE = "slowMovingMaintenanceVehicle"
    SLOW_VEHICLE = "slowVehicle"
    SNOWPLOUGH = "snowplough"
    TRACK_LAYING_VEHICLE = "trackLayingVehicle"
    UNLIT_VEHICLE_ON_THE_ROAD = "unlitVehicleOnTheRoad"
    VEHICLE_ON_FIRE = "vehicleOnFire"
    VEHICLE_CARRYING_HAZARDOUS_MATERIALS = "vehicleCarryingHazardousMaterials"
    VEHICLE_IN_DIFFICULTY = "vehicleInDifficulty"
    VEHICLE_ON_WRONG_CARRIAGEWAY = "vehicleOnWrongCarriageway"
    VEHICLE_STUCK = "vehicleStuck"
    VEHICLE_STUCK_UNDER_BRIDGE = "vehicleStuckUnderBridge"
    VEHICLE_WITH_OVERHEIGHT_LOAD = "vehicleWithOverheightLoad"
    VEHICLE_WITH_OVERWIDE_LOAD = "vehicleWithOverwideLoad"
    OTHER = "other"


class VehicleStatusEnum(Enum):
    """
    The status of a vehicle.

    :cvar ABANDONED: Abandoned vehicle.
    :cvar BROKEN_DOWN: Broken down vehicle (i.e. it is immobile due to
        mechanical breakdown).
    :cvar BURNT_OUT: Burnt out vehicle, but fire is extinguished.
    :cvar DAMAGED: Vehicle is damaged following an incident or
        collision. It may or may not be able to move by itself.
    :cvar DAMAGED_AND_IMMOBILIZED: Vehicle is damaged following an
        incident or collision. It is immobilized and therefore needs
        assistance to be moved.
    :cvar ON_FIRE: Vehicle is on fire.
    """
    ABANDONED = "abandoned"
    BROKEN_DOWN = "brokenDown"
    BURNT_OUT = "burntOut"
    DAMAGED = "damaged"
    DAMAGED_AND_IMMOBILIZED = "damagedAndImmobilized"
    ON_FIRE = "onFire"


class VehicleType2Enum(Enum):
    """
    Vehicle types which are currently not supported in vehicleType.

    :cvar MOTORHOME: Motorhome
    :cvar LIGHT_GOODS_VEHICLE: Light goods vehicle
    :cvar HEAVY_GOODS_VEHICLE: Heavy goods vehicle
    :cvar MINIBUS: Minibus
    :cvar SMALL_CAR: Small car
    :cvar LARGE_CAR: Large car
    :cvar LIGHT_GOODS_VEHICLE_WITH_TRAILER: Light goods vehicle with
        trailer
    :cvar HEAVY_GOODS_VEHICLE_WITH_TRAILER: Heavy goods vehicle with
        trailer
    :cvar HEAVY_HAULAGE_VEHICLE: Heavy-haulage vehicle
    :cvar PASSENGER_CAR: Passenger car
    :cvar UNKNOWN: Unknown.
    """
    MOTORHOME = "motorhome"
    LIGHT_GOODS_VEHICLE = "lightGoodsVehicle"
    HEAVY_GOODS_VEHICLE = "heavyGoodsVehicle"
    MINIBUS = "minibus"
    SMALL_CAR = "smallCar"
    LARGE_CAR = "largeCar"
    LIGHT_GOODS_VEHICLE_WITH_TRAILER = "lightGoodsVehicleWithTrailer"
    HEAVY_GOODS_VEHICLE_WITH_TRAILER = "heavyGoodsVehicleWithTrailer"
    HEAVY_HAULAGE_VEHICLE = "heavyHaulageVehicle"
    PASSENGER_CAR = "passengerCar"
    UNKNOWN = "unknown"


class VehicleTypeEnum(Enum):
    """
    Types of vehicle.

    :cvar AGRICULTURAL_VEHICLE: Vehicle normally used for agricultural
        purposes, e.g. tractor, combined harvester etc.
    :cvar ANY_VEHICLE: Vehicle of any type.
    :cvar ARTICULATED_VEHICLE: Articulated vehicle.
    :cvar BICYCLE: Bicycle.
    :cvar BUS: Bus.
    :cvar CAR: Car.
    :cvar CARAVAN: Caravan.
    :cvar CAR_OR_LIGHT_VEHICLE: Car or light vehicle.
    :cvar CAR_WITH_CARAVAN: Car towing a caravan.
    :cvar CAR_WITH_TRAILER: Car towing a trailer.
    :cvar CONSTRUCTION_OR_MAINTENANCE_VEHICLE: Vehicle normally used for
        construction or maintenance purposes, e.g. digger, excavator,
        bulldozer, lorry mounted crane etc.
    :cvar FOUR_WHEEL_DRIVE: Four wheel drive vehicle.
    :cvar HIGH_SIDED_VEHICLE: High sided vehicle.
    :cvar LORRY: Lorry of any type.
    :cvar MOPED: Moped (a two wheeled motor vehicle characterized by a
        small engine typically less than 50cc and by normally having
        pedals).
    :cvar MOTORCYCLE: Motorcycle.
    :cvar MOTORCYCLE_WITH_SIDE_CAR: Three wheeled vehicle comprising a
        motorcycle with an attached side car.
    :cvar MOTORSCOOTER: Motorscooter (a two wheeled motor vehicle
        characterized by a step-through frame and small diameter
        wheels).
    :cvar TANKER: Vehicle with large tank for carrying bulk liquids.
    :cvar THREE_WHEELED_VEHICLE: Three wheeled vehicle of unspecified
        type.
    :cvar TRAILER: Trailer.
    :cvar TRAM: Tram.
    :cvar TWO_WHEELED_VEHICLE: Two wheeled vehicle of unspecified type.
    :cvar VAN: Van.
    :cvar VEHICLE_WITH_CATALYTIC_CONVERTER: Vehicle with catalytic
        converter.
    :cvar VEHICLE_WITHOUT_CATALYTIC_CONVERTER: Vehicle without catalytic
        converter.
    :cvar VEHICLE_WITH_CARAVAN: Vehicle (of unspecified type) towing a
        caravan.
    :cvar VEHICLE_WITH_TRAILER: Vehicle (of unspecified type) towing a
        trailer.
    :cvar WITH_EVEN_NUMBERED_REGISTRATION_PLATES: Vehicle with even
        numbered registration plate.
    :cvar WITH_ODD_NUMBERED_REGISTRATION_PLATES: Vehicle with odd
        numbered registration plate.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AGRICULTURAL_VEHICLE = "agriculturalVehicle"
    ANY_VEHICLE = "anyVehicle"
    ARTICULATED_VEHICLE = "articulatedVehicle"
    BICYCLE = "bicycle"
    BUS = "bus"
    CAR = "car"
    CARAVAN = "caravan"
    CAR_OR_LIGHT_VEHICLE = "carOrLightVehicle"
    CAR_WITH_CARAVAN = "carWithCaravan"
    CAR_WITH_TRAILER = "carWithTrailer"
    CONSTRUCTION_OR_MAINTENANCE_VEHICLE = "constructionOrMaintenanceVehicle"
    FOUR_WHEEL_DRIVE = "fourWheelDrive"
    HIGH_SIDED_VEHICLE = "highSidedVehicle"
    LORRY = "lorry"
    MOPED = "moped"
    MOTORCYCLE = "motorcycle"
    MOTORCYCLE_WITH_SIDE_CAR = "motorcycleWithSideCar"
    MOTORSCOOTER = "motorscooter"
    TANKER = "tanker"
    THREE_WHEELED_VEHICLE = "threeWheeledVehicle"
    TRAILER = "trailer"
    TRAM = "tram"
    TWO_WHEELED_VEHICLE = "twoWheeledVehicle"
    VAN = "van"
    VEHICLE_WITH_CATALYTIC_CONVERTER = "vehicleWithCatalyticConverter"
    VEHICLE_WITHOUT_CATALYTIC_CONVERTER = "vehicleWithoutCatalyticConverter"
    VEHICLE_WITH_CARAVAN = "vehicleWithCaravan"
    VEHICLE_WITH_TRAILER = "vehicleWithTrailer"
    WITH_EVEN_NUMBERED_REGISTRATION_PLATES = "withEvenNumberedRegistrationPlates"
    WITH_ODD_NUMBERED_REGISTRATION_PLATES = "withOddNumberedRegistrationPlates"
    OTHER = "other"


class VehicleUsage2Enum(Enum):
    """
    Vehicle usage types which are currently not supported in vehicleUsageType.

    :cvar CITY_LOGISTICS: Vehicles that are used to deliver goods in a
        city area.
    :cvar CAR_SHARING: Vehicles operated by a car-sharing company.
    """
    CITY_LOGISTICS = "cityLogistics"
    CAR_SHARING = "carSharing"


class VehicleUsageEnum(Enum):
    """
    Types of usage of a vehicle.

    :cvar AGRICULTURAL: Vehicle used for agricultural purposes.
    :cvar COMMERCIAL: Vehicle which is limited to non-private usage or
        public transport usage.
    :cvar EMERGENCY_SERVICES: Vehicle used by the emergency services.
    :cvar MILITARY: Vehicle used by the military.
    :cvar NON_COMMERCIAL: Vehicle used for non-commercial or private
        purposes.
    :cvar PATROL: Vehicle used as part of a patrol service, e.g. road
        operator or automobile association patrol vehicle.
    :cvar RECOVERY_SERVICES: Vehicle used to provide a recovery service.
    :cvar ROAD_MAINTENANCE_OR_CONSTRUCTION: Vehicle used for road
        maintenance or construction work purposes.
    :cvar ROAD_OPERATOR: Vehicle used by the road operator.
    :cvar TAXI: Vehicle used to provide an authorised taxi service.
    """
    AGRICULTURAL = "agricultural"
    COMMERCIAL = "commercial"
    EMERGENCY_SERVICES = "emergencyServices"
    MILITARY = "military"
    NON_COMMERCIAL = "nonCommercial"
    PATROL = "patrol"
    RECOVERY_SERVICES = "recoveryServices"
    ROAD_MAINTENANCE_OR_CONSTRUCTION = "roadMaintenanceOrConstruction"
    ROAD_OPERATOR = "roadOperator"
    TAXI = "taxi"


@dataclass
class VersionedReference:
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


class VmsDatexPictogramEnum(Enum):
    """
    Types of main pictograms.

    :cvar ACCIDENT: Accident.
    :cvar ADVISORY_SPEED: Advisory speed limit.
    :cvar ANIMALS_ON_ROAD: Animal(s) on the road.
    :cvar BLANK_VOID: Blank or void.
    :cvar BRIDGE_CLOSED: Bridge closed.
    :cvar BRIDGE_SWING_IN_OPERATION: Bridge swing in operation.
    :cvar CAR_PARK_FULL: Car park full.
    :cvar CAR_PARK_SPACES_AVAILABLE: Spaces available in car park.
    :cvar CARRIAGEWAY_NARROWS: The carriageway narrows ahead.
    :cvar CARRIAGEWAY_NARROWS_ON_THE_LEFT: The carriageway narrows ahead
        from the left.
    :cvar CARRIAGEWAY_NARROWS_ON_THE_RIGHT: The carriageway narrows
        ahead from the right.
    :cvar CARRIAGEWAY_REDUCED_TO_ONE_LANE: Carriageway reduced to one
        lane.
    :cvar CARRIAGEWAY_REDUCED_TO_TWO_LANES: Carriageway reduced to two
        lanes.
    :cvar CARRIAGEWAY_REDUCED_TO_THREE_LANES: Carriageway reduced to
        three lanes.
    :cvar CHAINS_OR_SNOW_TYRES_RECOMMENDED: Chains or snow tyres are
        recommended.
    :cvar COMPULSORY_MINIMUM_SPEED: Mandatory minimum speed limit.
    :cvar CROSS_WIND: Cross wind.
    :cvar DANGER_OF_FIRE: Danger of fire.
    :cvar DRIVING_OF_VEHICLES_LESS_THAN_XMETRES_APART_PROHIBITED: The
        driving of vehicles less than X metres apart is prohibited.
    :cvar END_OF_ADVISORY_SPEED: End of advisory speed.
    :cvar END_OF_COMPULSORY_MINIMUM_SPEED: End of compulsory minimum
        speed limit.
    :cvar END_OF_PROHIBITION_OF_OVERTAKING: End of prohibition of
        overtaking.
    :cvar END_OF_PROHIBITION_OF_OVERTAKING_FOR_GOODS_VEHICLES: End of
        prohibition of overtaking for goods vehicles.
    :cvar END_OF_SPEED_LIMIT: End of mandatory speed limit.
    :cvar EXIT_CLOSED: Exit closed.
    :cvar FALLING_ROCKS: Danger of rock fall or landslide.
    :cvar FASTEN_CHILDRENS_SEAT_BELTS: Fasten the seat belts of
        children.
    :cvar FASTEN_YOUR_SEAT_BELT: Fasten your seat belt.
    :cvar FIRE: Fire.
    :cvar FLOODING_OR_FLASH_FLOODS: Flooding or flash floods.
    :cvar FOG: Fog.
    :cvar FOOTBALL_MATCH: Football match (current or anticipated
        disruption due to football match).
    :cvar HARD_SHOULDER_NOT_RUNNING: Hard shoulder running is in
        operation.
    :cvar HARD_SHOULDER_RUNNING: Hard shoulder running is not in
        operation.
    :cvar KEEP_ASAFE_DISTANCE: Keep a safe distance.
    :cvar KEEP_LEFT: Keep left.
    :cvar KEEP_RIGHT: Keep right.
    :cvar LANE1_CLOSED_OF2: Lane 1 closed on a 2 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE2_CLOSED_OF2: Lane 2 closed on a 2 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE1_CLOSED_OF3: Lane 1 closed on a 3 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE3_CLOSED_OF3: Lane 3 closed on a 3 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANES1_AND2_CLOSED_OF3: Lanes 1 and 2 closed on a 3 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES2_AND3_CLOSED_OF3: Lanes 2 and 3 closed on a 3 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANE1_CLOSED_OF4: Lane 1 closed on a 4 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANE4_CLOSED_OF4: Lane 4 closed on a 4 lane carriageway. Lanes
        numbered from nearside (next to hard shoulder on motorway) to
        central median.
    :cvar LANES1_AND2_CLOSED_OF4: Lanes 1 and 2 closed on a 4 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES3_AND4_CLOSED_OF4: Lanes 3 and 4 closed on a 4 lane
        carriageway. Lanes numbered from nearside (next to hard shoulder
        on motorway) to central median.
    :cvar LANES1_AND2_AND3_CLOSED_OF4: Lanes 1, 2 and 3 closed on a 4
        lane carriageway. Lanes numbered from nearside (next to hard
        shoulder on motorway) to central median.
    :cvar LANES2_AND3_AND4_CLOSED_OF4: Lanes 2, 3 and 4 closed on a 4
        lane carriageway. Lanes numbered from nearside (next to hard
        shoulder on motorway) to central median.
    :cvar LANE_CLOSED: Lane closed.
    :cvar LANE_DEVIATION_TO_LEFT: Lane deviates to the left.
    :cvar LANE_DEVIATION_TO_RIGHT: Lane deviates to the right.
    :cvar LANE_OPEN: Lane open.
    :cvar LEFT_HAND_LANE_CLOSED: Left hand lane closed ahead.
    :cvar LIGHT_SIGNALS: Traffic light signals ahead.
    :cvar LOOSE_GRAVEL: Loose gravel.
    :cvar MAINTENANCE_VEHICLE_IN_ACTION: Maintenance vehicles in action.
    :cvar MAXIMUM_SPEED_LIMITED_TO_THE_FIGURE_INDICATED: Mandatory
        maximum speed limit, displayed as speed limit indside a red
        circle.
    :cvar NARROW_LANES_AEAD: Narrow lanes ahead.
    :cvar NO_ENTRY: No entry.
    :cvar NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER: No
        entry for any power driven vehicle drawing a trailer
    :cvar
        NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER_OTHER_THAN_ASEMI_TRAILER_OR_ASINGLE_AXLE_TRAILER:
        No entry to any power driven vehicle drawing a trailer other
        than a semi-trailer or a single axle trailer. A semi-trailer is
        one designed to be coupled to a motor vehicle so that part of
        its weight and that of its load is borne by the motor vehicle.
    :cvar NO_ENTRY_FOR_GOODS_VEHICLES: No entry for goods vehicles.
    :cvar NO_ENTRY_FOR_VEHICLES_EXCEEDING_XTONNES_LADEN_MASS: No entry
        for vehicles exceeding X tonnes laden mass.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AMASS_EXCEEDING_XTONNES_ON_ONE_AXLE:
        No entry for vehicles having a mass exceeding X tonnes on a
        single axle.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_HEIGHT_EXCEEDING_XMETRES:
        No entry for vehicles having an overall height exceeding X
        metres.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_LENGTH_EXCEEDING_XMETRES:
        No entry for vehicles having an overall length exceeding X
        metres.
    :cvar
        NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_WIDTH_EXCEEDING_XMETRES:
        No entry for vehicles having an overall width exceeding X
        metres.
    :cvar NO_ENTRY_FOR_VEHICLES_CARRYING_DANGEROUS_GOODS: No entry for
        vehicles carrying dangerous goods.
    :cvar OTHER_DANGERS: Danger ahead of an unspecified nature.
    :cvar OVERTAKING_BY_GOODS_VEHICLES_PROHIBITED: Overtaking prohibited
        for goods vehicles.
    :cvar OVERTAKING_PROHIBITED: Overtaking prohibited.
    :cvar POLLUTION_OR_SMOG_ALERT: Pollution or smog alert.
    :cvar QUEUE: Queue ahead.
    :cvar RAIN: Rain.
    :cvar RIGHT_HAND_LANE_CLOSED: Right hand lane closed ahead.
    :cvar ROAD_CLOSED_AHEAD: Road closed ahead.
    :cvar ROADWORKS: Roadworks.
    :cvar SLIPPERY_ROAD: Slippery road.
    :cvar SMOKE: Smoke.
    :cvar SNOW: Snow.
    :cvar SNOW_CHAINS_COMPULSORY: The use of snow chains is compulsory.
    :cvar SNOW_TYRES_COMPULSORY: The use of snow tyres is compulsory.
    :cvar SNOW_PLOUGH_IN_ACTION: Snow plough(s) in action.
    :cvar SPEED_CAMERAS_IN_ACTION: Speed cameras in action.
    :cvar TRAFFIC_CONGESTION: Traffic congestion and possible queues.
    :cvar TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD: All traffic is
        diverted to the opposite carriageway ahead in a contraflow
        layout.
    :cvar TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD:
        Traffic is partially diverted to the opposite carriageway ahead
        in a contraflow layout.
    :cvar TUNNEL_CLOSED: Tunnel closed.
    :cvar TURN_LEFT: Mandatory turn left.
    :cvar TURN_RIGHT: Mandatory turn right.
    :cvar TWO_WAY_TRAFFIC: Two way traffic (on a single carriageway).
    :cvar UNEVEN_ROAD: Uneven road surface.
    :cvar VEHICLE_FIRE: Vehicle fire.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ACCIDENT = "accident"
    ADVISORY_SPEED = "advisorySpeed"
    ANIMALS_ON_ROAD = "animalsOnRoad"
    BLANK_VOID = "blankVoid"
    BRIDGE_CLOSED = "bridgeClosed"
    BRIDGE_SWING_IN_OPERATION = "bridgeSwingInOperation"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_SPACES_AVAILABLE = "carParkSpacesAvailable"
    CARRIAGEWAY_NARROWS = "carriagewayNarrows"
    CARRIAGEWAY_NARROWS_ON_THE_LEFT = "carriagewayNarrowsOnTheLeft"
    CARRIAGEWAY_NARROWS_ON_THE_RIGHT = "carriagewayNarrowsOnTheRight"
    CARRIAGEWAY_REDUCED_TO_ONE_LANE = "carriagewayReducedToOneLane"
    CARRIAGEWAY_REDUCED_TO_TWO_LANES = "carriagewayReducedToTwoLanes"
    CARRIAGEWAY_REDUCED_TO_THREE_LANES = "carriagewayReducedToThreeLanes"
    CHAINS_OR_SNOW_TYRES_RECOMMENDED = "chainsOrSnowTyresRecommended"
    COMPULSORY_MINIMUM_SPEED = "compulsoryMinimumSpeed"
    CROSS_WIND = "crossWind"
    DANGER_OF_FIRE = "dangerOfFire"
    DRIVING_OF_VEHICLES_LESS_THAN_XMETRES_APART_PROHIBITED = "drivingOfVehiclesLessThanXMetresApartProhibited"
    END_OF_ADVISORY_SPEED = "endOfAdvisorySpeed"
    END_OF_COMPULSORY_MINIMUM_SPEED = "endOfCompulsoryMinimumSpeed"
    END_OF_PROHIBITION_OF_OVERTAKING = "endOfProhibitionOfOvertaking"
    END_OF_PROHIBITION_OF_OVERTAKING_FOR_GOODS_VEHICLES = "endOfProhibitionOfOvertakingForGoodsVehicles"
    END_OF_SPEED_LIMIT = "endOfSpeedLimit"
    EXIT_CLOSED = "exitClosed"
    FALLING_ROCKS = "fallingRocks"
    FASTEN_CHILDRENS_SEAT_BELTS = "fastenChildrensSeatBelts"
    FASTEN_YOUR_SEAT_BELT = "fastenYourSeatBelt"
    FIRE = "fire"
    FLOODING_OR_FLASH_FLOODS = "floodingOrFlashFloods"
    FOG = "fog"
    FOOTBALL_MATCH = "footballMatch"
    HARD_SHOULDER_NOT_RUNNING = "hardShoulderNotRunning"
    HARD_SHOULDER_RUNNING = "hardShoulderRunning"
    KEEP_ASAFE_DISTANCE = "keepASafeDistance"
    KEEP_LEFT = "keepLeft"
    KEEP_RIGHT = "keepRight"
    LANE1_CLOSED_OF2 = "lane1ClosedOf2"
    LANE2_CLOSED_OF2 = "lane2ClosedOf2"
    LANE1_CLOSED_OF3 = "lane1ClosedOf3"
    LANE3_CLOSED_OF3 = "lane3ClosedOf3"
    LANES1_AND2_CLOSED_OF3 = "lanes1And2ClosedOf3"
    LANES2_AND3_CLOSED_OF3 = "lanes2And3ClosedOf3"
    LANE1_CLOSED_OF4 = "lane1ClosedOf4"
    LANE4_CLOSED_OF4 = "lane4ClosedOf4"
    LANES1_AND2_CLOSED_OF4 = "lanes1And2ClosedOf4"
    LANES3_AND4_CLOSED_OF4 = "lanes3And4ClosedOf4"
    LANES1_AND2_AND3_CLOSED_OF4 = "lanes1And2And3ClosedOf4"
    LANES2_AND3_AND4_CLOSED_OF4 = "lanes2And3And4ClosedOf4"
    LANE_CLOSED = "laneClosed"
    LANE_DEVIATION_TO_LEFT = "laneDeviationToLeft"
    LANE_DEVIATION_TO_RIGHT = "laneDeviationToRight"
    LANE_OPEN = "laneOpen"
    LEFT_HAND_LANE_CLOSED = "leftHandLaneClosed"
    LIGHT_SIGNALS = "lightSignals"
    LOOSE_GRAVEL = "looseGravel"
    MAINTENANCE_VEHICLE_IN_ACTION = "maintenanceVehicleInAction"
    MAXIMUM_SPEED_LIMITED_TO_THE_FIGURE_INDICATED = "maximumSpeedLimitedToTheFigureIndicated"
    NARROW_LANES_AEAD = "narrowLanesAead"
    NO_ENTRY = "noEntry"
    NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER = "noEntryForAnyPowerDrivenVehicleDrawingATrailer"
    NO_ENTRY_FOR_ANY_POWER_DRIVEN_VEHICLE_DRAWING_ATRAILER_OTHER_THAN_ASEMI_TRAILER_OR_ASINGLE_AXLE_TRAILER = "noEntryForAnyPowerDrivenVehicleDrawingATrailerOtherThanASemiTrailerOrASingleAxleTrailer"
    NO_ENTRY_FOR_GOODS_VEHICLES = "noEntryForGoodsVehicles"
    NO_ENTRY_FOR_VEHICLES_EXCEEDING_XTONNES_LADEN_MASS = "noEntryForVehiclesExceedingXTonnesLadenMass"
    NO_ENTRY_FOR_VEHICLES_HAVING_AMASS_EXCEEDING_XTONNES_ON_ONE_AXLE = "noEntryForVehiclesHavingAMassExceedingXTonnesOnOneAxle"
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_HEIGHT_EXCEEDING_XMETRES = "noEntryForVehiclesHavingAnOverallHeightExceedingXMetres"
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_LENGTH_EXCEEDING_XMETRES = "noEntryForVehiclesHavingAnOverallLengthExceedingXMetres"
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_WIDTH_EXCEEDING_XMETRES = "noEntryForVehiclesHavingAnOverallWidthExceedingXMetres"
    NO_ENTRY_FOR_VEHICLES_CARRYING_DANGEROUS_GOODS = "noEntryForVehiclesCarryingDangerousGoods"
    OTHER_DANGERS = "otherDangers"
    OVERTAKING_BY_GOODS_VEHICLES_PROHIBITED = "overtakingByGoodsVehiclesProhibited"
    OVERTAKING_PROHIBITED = "overtakingProhibited"
    POLLUTION_OR_SMOG_ALERT = "pollutionOrSmogAlert"
    QUEUE = "queue"
    RAIN = "rain"
    RIGHT_HAND_LANE_CLOSED = "rightHandLaneClosed"
    ROAD_CLOSED_AHEAD = "roadClosedAhead"
    ROADWORKS = "roadworks"
    SLIPPERY_ROAD = "slipperyRoad"
    SMOKE = "smoke"
    SNOW = "snow"
    SNOW_CHAINS_COMPULSORY = "snowChainsCompulsory"
    SNOW_TYRES_COMPULSORY = "snowTyresCompulsory"
    SNOW_PLOUGH_IN_ACTION = "snowPloughInAction"
    SPEED_CAMERAS_IN_ACTION = "speedCamerasInAction"
    TRAFFIC_CONGESTION = "trafficCongestion"
    TRAFFIC_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = "trafficDeviatedToOppositeCarriagewayAhead"
    TRAFFIC_PARTIALLY_DEVIATED_TO_OPPOSITE_CARRIAGEWAY_AHEAD = "trafficPartiallyDeviatedToOppositeCarriagewayAhead"
    TUNNEL_CLOSED = "tunnelClosed"
    TURN_LEFT = "turnLeft"
    TURN_RIGHT = "turnRight"
    TWO_WAY_TRAFFIC = "twoWayTraffic"
    UNEVEN_ROAD = "unevenRoad"
    VEHICLE_FIRE = "vehicleFire"
    OTHER = "other"


class VmsDatexSupplementalPictogramEnum(Enum):
    """
    Types of pictograms displayable in supplementary panels (normally below the
    main pictogram display which it qualifies).

    :cvar DISTANCE_TO_THE_BEGINNINGOF_THE_APPLICATION_ZONE: Distance to
        the beginning of the application zone.
    :cvar EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER: Except any
        power driven vehicle drawing a trailer.
    :cvar EXCEPT_BUS: Except for buses.
    :cvar EXCEPT_GOODS_VEHICLES: Except for goods vehicles.
    :cvar EXCEPT_SEMI_TRAILER: Except for semi trailers (i.e. any
        trailer designed to be coupled to a motor vehicle in such a way
        that part of its weight and that of its load is borne by the
        motor vehicle).
    :cvar EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS: Except for vehicles
        carrying dangerous goods (i.e. for which special sign plating is
        prescribed).
    :cvar IN_CASE_OF_ICE_OR_SNOW: In case of ice or snow.
    :cvar LENGTH_OF_THE_APPLICATION_ZONE: Length of the applicable zone.
    :cvar RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER:
        Restricted to any power driven vehicle drawing a trailer.
    :cvar RESTRICETD_TO_BUS: Restricted to buses.
    :cvar RESTRICTED_TO_GOODS_VEHICLES: Restricted to goods vehicles.
    :cvar RESTRICTED_TO_SEMI_TRAILER: Restricted to semi trailers (i.e.
        any trailer designed to be coupled to a motor vehicle in such a
        way that part of its wieght and that of its load is borne by the
        motor vehicle).
    :cvar RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS: Restricted to
        vehicles carrying dangerous goods (i.e. for which special sign
        plating is prescribed).
    :cvar MAINTENANCE_VEHICLES: Maintenance vehicles.
    :cvar SNOW_PLOUGHS: Snow ploughs.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    DISTANCE_TO_THE_BEGINNINGOF_THE_APPLICATION_ZONE = "distanceToTheBeginningofTheApplicationZone"
    EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = "exceptAnyPowerDrivenVehicleDrawingTrailer"
    EXCEPT_BUS = "exceptBus"
    EXCEPT_GOODS_VEHICLES = "exceptGoodsVehicles"
    EXCEPT_SEMI_TRAILER = "exceptSemiTrailer"
    EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS = "exceptVehiclesCarryingDangerousGoods"
    IN_CASE_OF_ICE_OR_SNOW = "inCaseOfIceOrSnow"
    LENGTH_OF_THE_APPLICATION_ZONE = "lengthOfTheApplicationZone"
    RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = "restrictedToAnyPowerDrivenVehicleDrawingTrailer"
    RESTRICETD_TO_BUS = "restricetdToBus"
    RESTRICTED_TO_GOODS_VEHICLES = "restrictedToGoodsVehicles"
    RESTRICTED_TO_SEMI_TRAILER = "restrictedToSemiTrailer"
    RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS = "restrictedToVehiclesCarryingDangerousGoods"
    MAINTENANCE_VEHICLES = "maintenanceVehicles"
    SNOW_PLOUGHS = "snowPloughs"
    OTHER = "other"


class VmsFaultEnum(Enum):
    """
    Types of variable message sign faults.

    :cvar COMMUNICATIONS_FAILURE: Comunications failure affecting VMS.
    :cvar INCORRECT_MESSAGE_DISPLAYED: Incorrect message is being
        displayed.
    :cvar INCORRECT_PICTOGRAM_DISPLAYED: Incorrect pictogram is being
        displayed.
    :cvar OUT_OF_SERVICE: Not currently in service (e.g. intentionally
        disconnected or switched off during roadworks).
    :cvar POWER_FAILURE: Power to VMS has failed.
    :cvar UNABLE_TO_CLEAR_DOWN: Unable to clear down information
        displayed on VMS.
    :cvar UNKNOWN: Unknown VMS fault.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_MESSAGE_DISPLAYED = "incorrectMessageDisplayed"
    INCORRECT_PICTOGRAM_DISPLAYED = "incorrectPictogramDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"


class VmsLuminanceLevelEnum(Enum):
    """
    Levels of luminance applicable to VMS.

    :cvar SWITCHED_OFF: Luminance level is zero as light source is
        switched off.
    :cvar TESTING: Luminance is set at testing level.
    :cvar NIGHT: Luminance is set at level defined for night time.
    :cvar OVERCAST: Luminance is set at level defined for overcast or
        dull day time conditions.
    :cvar BROAD_DAYLIGHT: Luminance is set at level defined for normal
        broad day light conditions.
    :cvar SUN_IN_EYES: Luminance is set at level defined for conditions
        where drivers will have sun in their eyes.
    :cvar SUN_ON_BACK: Luminance is set at level defined for conditions
        where drivers will have sun behind them.
    :cvar FOGGY_DAY: Luminance is set at level defined for foggy day
        time conditions.
    :cvar FOGGY_NIGHT: Luminance is set at level defined for foggy night
        time conditions.
    """
    SWITCHED_OFF = "switchedOff"
    TESTING = "testing"
    NIGHT = "night"
    OVERCAST = "overcast"
    BROAD_DAYLIGHT = "broadDaylight"
    SUN_IN_EYES = "sunInEyes"
    SUN_ON_BACK = "sunOnBack"
    FOGGY_DAY = "foggyDay"
    FOGGY_NIGHT = "foggyNight"


class VmsMessageInformationTypeEnum(Enum):
    """
    Types of information displayable on a VMS.

    :cvar CAMPAIGN_MESSAGE: Campaign type information which is non time
        specific that may request certain actions (e.g. "do not drink
        and drive") or which is intended to influence drivers'
        behaviour.
    :cvar DATE_TIME: Current date and/or time information.
    :cvar FUTURE_INFORMATION: Information which may inform road users
        about future situations which potentially may cause congestion
        or influence future travel plans (e.g. future roadworks,
        closures, sporting events, public concerts, suspension of train
        or ferry services).
    :cvar INSTRUCTION_OR_MESSAGE: Instructions or messages to road users
        which are relevant at the current time, (e.g. "do not throw out
        any burning objects" or an Amber alert message).
    :cvar SITUATION_WARNING: Information warning of a current situation
        likely to affect traffic on the road ahead.
    :cvar TEMPERATURE: Temperature information.
    :cvar TRAFFIC_MANAGEMENT: Information comprising traffic management
        instructions.
    :cvar TRAVEL_TIME: Travel time information.
    """
    CAMPAIGN_MESSAGE = "campaignMessage"
    DATE_TIME = "dateTime"
    FUTURE_INFORMATION = "futureInformation"
    INSTRUCTION_OR_MESSAGE = "instructionOrMessage"
    SITUATION_WARNING = "situationWarning"
    TEMPERATURE = "temperature"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"


class VmsTypeEnum(Enum):
    """
    Type of variable message sign.

    :cvar COLOUR_GRAPHIC: A colour graphic display.
    :cvar CONTINUOUS_SIGN: A sign implementing fixed messages which are
        selected by electromechanical means.
    :cvar MONOCHROME_GRAPHIC: A monochrome graphic display.
    :cvar MATRIX_SIGN: Simple display made up of a fixed matrix of
        pixels (e.g. sets of LEDs or lights) capable of showing a
        limited set of aspects (or matrix images). The display area is
        regarded as a pictogram area in DATEX II.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    COLOUR_GRAPHIC = "colourGraphic"
    CONTINUOUS_SIGN = "continuousSign"
    MONOCHROME_GRAPHIC = "monochromeGraphic"
    MATRIX_SIGN = "matrixSign"
    OTHER = "other"


class WeatherRelatedRoadConditionTypeEnum(Enum):
    """
    Types of road surface conditions which are related to the weather.

    :cvar BLACK_ICE: Severe skid risk due to black ice (i.e. clear ice,
        which is impossible or very difficult to see).
    :cvar DEEP_SNOW: Deep snow on the roadway.
    :cvar DRY: The road surface is dry.
    :cvar FREEZING_OF_WET_ROADS: The wet road surface is subject to
        freezing.
    :cvar FREEZING_PAVEMENTS: The pavements for pedestrians are subject
        to freezing.
    :cvar FREEZING_RAIN: Severe skid risk due to rain falling on sub-
        zero temperature road surface and freezing.
    :cvar FRESH_SNOW: Fresh snow (with little or no traffic yet) on the
        roadway.
    :cvar ICE: Increased skid risk due to ice (of any kind).
    :cvar ICE_BUILD_UP: Ice is building up on the roadway causing a
        serious skid hazard.
    :cvar ICE_WITH_WHEEL_BAR_TRACKS: Ice on the road frozen in the form
        of wheel tracks.
    :cvar ICY_PATCHES: Severe skid risk due to icy patches (i.e.
        intermittent ice on roadway).
    :cvar LOOSE_SNOW: Powdery snow on the road which is subject to being
        blown by the wind.
    :cvar NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS: Conditions for
        pedestrians are consistent with those normally expected in
        winter.
    :cvar PACKED_SNOW: Packed snow (heavily trafficked) on the roadway.
    :cvar ROAD_SURFACE_MELTING: The road surface is melting, or has
        melted due to abnormally high temperatures.
    :cvar SLIPPERY_ROAD: The road surface is slippery due to bad weather
        conditions.
    :cvar SLUSH_ON_ROAD: Increased skid risk due to melting snow (slush)
        on road.
    :cvar SLUSH_STRINGS: Melting snow (slush) on the roadway is formed
        into wheel tracks.
    :cvar SNOW_DRIFTS: Snow drifting is in progress or patches of deep
        snow are present due to earlier drifting.
    :cvar SNOW_ON_PAVEMENT: Snow is on the pedestrian pavement.
    :cvar SNOW_ON_THE_ROAD: Snow is lying on the road surface.
    :cvar SURFACE_WATER: Water is resting on the roadway which provides
        an increased hazard to vehicles.
    :cvar WET: Road surface is wet.
    :cvar WET_AND_ICY_ROAD: Increased skid risk due to partly thawed,
        wet road with packed snow and ice, or rain falling on packed
        snow and ice.
    :cvar WET_ICY_PAVEMENT: Partly thawed, wet pedestrian pavement with
        packed snow and ice, or rain falling on packed snow and ice.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    BLACK_ICE = "blackIce"
    DEEP_SNOW = "deepSnow"
    DRY = "dry"
    FREEZING_OF_WET_ROADS = "freezingOfWetRoads"
    FREEZING_PAVEMENTS = "freezingPavements"
    FREEZING_RAIN = "freezingRain"
    FRESH_SNOW = "freshSnow"
    ICE = "ice"
    ICE_BUILD_UP = "iceBuildUp"
    ICE_WITH_WHEEL_BAR_TRACKS = "iceWithWheelBarTracks"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS = "normalWinterConditionsForPedestrians"
    PACKED_SNOW = "packedSnow"
    ROAD_SURFACE_MELTING = "roadSurfaceMelting"
    SLIPPERY_ROAD = "slipperyRoad"
    SLUSH_ON_ROAD = "slushOnRoad"
    SLUSH_STRINGS = "slushStrings"
    SNOW_DRIFTS = "snowDrifts"
    SNOW_ON_PAVEMENT = "snowOnPavement"
    SNOW_ON_THE_ROAD = "snowOnTheRoad"
    SURFACE_WATER = "surfaceWater"
    WET = "wet"
    WET_AND_ICY_ROAD = "wetAndIcyRoad"
    WET_ICY_PAVEMENT = "wetIcyPavement"
    OTHER = "other"


class WeekOfMonthEnum(Enum):
    """
    Weeks of the month.

    :cvar FIRST_WEEK_OF_MONTH: First week of the month.
    :cvar SECOND_WEEK_OF_MONTH: Second week of the month.
    :cvar THIRD_WEEK_OF_MONTH: Third week of the month.
    :cvar FOURTH_WEEK_OF_MONTH: Fourth week of the month.
    :cvar FIFTH_WEEK_OF_MONTH: Fifth week of the month (at most only 3
        days and non in February when not a leap year).
    """
    FIRST_WEEK_OF_MONTH = "firstWeekOfMonth"
    SECOND_WEEK_OF_MONTH = "secondWeekOfMonth"
    THIRD_WEEK_OF_MONTH = "thirdWeekOfMonth"
    FOURTH_WEEK_OF_MONTH = "fourthWeekOfMonth"
    FIFTH_WEEK_OF_MONTH = "fifthWeekOfMonth"


class WinterEquipmentManagementTypeEnum(Enum):
    """
    Instructions relating to the use of winter equipment.

    :cvar DO_NO_USE_STUD_TYRES: Do not use stud tyres.
    :cvar USE_SNOW_CHAINS: Use snow chains.
    :cvar USE_SNOW_CHAINS_OR_TYRES: Use snow chains or snow tyres.
    :cvar USE_SNOW_TYRES: Use snow tyres.
    :cvar WINTER_EQUIPMENT_ON_BOARD_REQUIRED: The carrying of winter
        equipment (snow chains and/or snow tyres) is required.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    DO_NO_USE_STUD_TYRES = "doNoUseStudTyres"
    USE_SNOW_CHAINS = "useSnowChains"
    USE_SNOW_CHAINS_OR_TYRES = "useSnowChainsOrTyres"
    USE_SNOW_TYRES = "useSnowTyres"
    WINTER_EQUIPMENT_ON_BOARD_REQUIRED = "winterEquipmentOnBoardRequired"
    OTHER = "other"


@dataclass
class ExtensionType:
    class Meta:
        name = "_ExtensionType"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class AcceptedPaymentCards:
    """
    Use this class to describe details in case acceptedMeansOfPayment is set to
    'paymentCard'.

    :ivar payment_cards: List of accepted payment cards.
    :ivar other_payment_cards: Further accepted payment cards.
    :ivar payment_card_brands: List of accepted brands for payment
        cards.
    :ivar other_payment_card_brands: Further accepted brands of payment
        cards.
    :ivar accepted_payment_cards_extension:
    """
    payment_cards: List[PaymentCardTypesEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    other_payment_cards: List[str] = field(
        default_factory=list,
        metadata={
            "name": "otherPaymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    payment_card_brands: List[PaymentCardBrandsEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentCardBrands",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_payment_card_brands: List[str] = field(
        default_factory=list,
        metadata={
            "name": "otherPaymentCardBrands",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    accepted_payment_cards_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "acceptedPaymentCardsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AffectedCarriagewayAndLanes:
    """Supplementary positional information which details carriageway and lane
    locations.

    Several instances may exist where the element being described
    extends over more than one carriageway.

    :ivar carriageway: Indicates the section of carriageway to which the
        location relates.
    :ivar lane: Indicates the specific lane to which the location
        relates.
    :ivar footpath: Indicates whether the pedestrian footpath is the
        subject or part of the subject of the location. (True = footpath
        is subject)
    :ivar length_affected: This indicates the length of road measured in
        metres affected by the associated traffic element.
    :ivar affected_carriageway_and_lanes_extension:
    """
    carriageway: Optional[CarriagewayEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    lane: List[LaneEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    footpath: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    length_affected: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthAffected",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    affected_carriageway_and_lanes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "affectedCarriagewayAndLanesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCLinear:
    """
    A linear section along a road defined between two points on the road by
    reference to a pre-defined ALERT-C location table.

    :ivar alert_clocation_country_code: EBU country code.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar alert_clinear_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clinear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCPoint:
    """
    A single point on the road network defined by reference to a pre-defined
    ALERT-C location table and which has an associated direction of traffic
    flow.

    :ivar alert_clocation_country_code: EBU country code.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar alert_cpoint_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_cpoint_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AxleSpacing:
    """
    The spacing details between the axle sets of an individual vehicle numbered
    from the front to the back of the vehicle.

    :ivar axle_spacing: The spacing interval, indicated by the
        axleSpacingSequenceIdentifier, between the axles of an
        individual vehicle from front to back of the vehicle.
    :ivar axle_spacing_sequence_identifier: Indicates the sequence of
        the interval between the axles of the individual vehicle from
        front to back (e.g. 1, 2, 3...). This cannot exceed
        (numberOfAxles -1) if the numberOfAxles is also given as part of
        the VehicleCharacteristics.
    :ivar axle_spacing_extension:
    """
    axle_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_spacing_sequence_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_spacing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AxleWeight:
    """
    The weight details of a specific axle on the vehicle.

    :ivar axle_position_identifier: Indicates the position of the axle
        on the vehicle numbered from front to back (i.e. 1, 2, 3...).
        This cannot exceed the numberOfAxles if provided as part of
        VehicleCharacteristics.
    :ivar axle_weight: The weight of the specific axle, indicated by the
        axleSequenceIdentifier, on the vehicle numbered from front to
        back of the vehicle.
    :ivar maximum_permitted_axle_weight: The maximum permitted weight of
        this specific axle on the vehicle.
    :ivar axle_weight_extension:
    """
    axle_position_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axlePositionIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_permitted_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumPermittedAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    axle_weight_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleWeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class CatalogueReference:
    """
    Identification of the supplier's data catalogue in a data exchange context.

    :ivar key_catalogue_reference: Identification of the supplier's data
        catalogue in a data exchange context.
    :ivar catalogue_reference_extension:
    """
    key_catalogue_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyCatalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    catalogue_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "catalogueReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Cause:
    """
    Contains details of the cause of a record within a situation.
    """
    cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "causeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DayWeekMonth:
    """
    Specification of periods defined by the intersection of days, weeks and
    months.

    :ivar applicable_day: Applicable day of the week. "All days of the
        week" is expressed by non-inclusion of this attribute.
    :ivar applicable_week: Applicable week of the month (1 to 5).  "All
        weeks of the month" is expressed by non-inclusion of this
        attribute.
    :ivar applicable_month: Applicable month of the year.  "All months
        of the year" is expressed by non-inclusion of this attribute.
    :ivar day_week_month_extension:
    """
    applicable_day: List[DayEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 7,
        }
    )
    applicable_week: List[WeekOfMonthEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableWeek",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 5,
        }
    )
    applicable_month: List[MonthOfYearEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 12,
        }
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    delay_band: Optional[DelayBandEnum] = field(
        default=None,
        metadata={
            "name": "delayBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    delays_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "delaysType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    delay_time_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "delayTimeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    delays_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "delaysExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Destination:
    """The specification a destination.

    This may be either a point location or an area location.
    """
    destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "destinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Dimension:
    """A component that provides dimension information.

    The product of width and height must not be necessarily be the
    square footage (e.g. in multi-storey buildings or when some zones
    are not part of the square footage).

    :ivar dimension_length: Length.
    :ivar dimension_width: Width.
    :ivar dimension_height: Height.
    :ivar dimension_usable_area: The area measured in square metres,
        that is available for some specific purpose.
    :ivar dimension_extension:
    """
    dimension_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dimension_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dimension_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dimension_usable_area: Optional[int] = field(
        default=None,
        metadata={
            "name": "dimensionUsableArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dimension_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dimensionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DistanceAlongLinearElement:
    """
    Distance of a point along a linear element either measured from the start
    node or a defined referent on that linear element, where the start node is
    relative to the element definition rather than the direction of traffic
    flow.
    """
    distance_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "distanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ExternalReferencing:
    """
    A location defined by reference to an external/other referencing system.

    :ivar external_location_code: A code in the external referencing
        system which defines the location.
    :ivar external_referencing_system: Identification of the
        external/other location referencing system.
    :ivar external_referencing_extension:
    """
    external_location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Fault:
    """
    Information about a fault relating to a specific piece of equipment or
    process.

    :ivar fault_identifier: Unique identifier of the fault.
    :ivar fault_description: Textual description of the fault.
    :ivar fault_creation_time: The date and time at which the fault was
        originally recorded/reported.
    :ivar fault_last_update_time: The date and time at which the fault
        information as specified in this instance was last updated.
    :ivar fault_severity: The severity of the fault in terms of how it
        affects the usability of the equipment or the reliability of the
        data generated by the equipment.
    :ivar fault_extension:
    """
    fault_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "faultIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    fault_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "faultDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    fault_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "faultCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    fault_last_update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "faultLastUpdateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    fault_severity: Optional[FaultSeverityEnum] = field(
        default=None,
        metadata={
            "name": "faultSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "faultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class FilterExitManagement:
    """
    Filter indicators management information.

    :ivar filter_end: This attribute, set to true, indicates that the
        filter, for which a previous record version has been published,
        becomes inactive.
    :ivar filter_out_of_range: This attribute is set to true when a
        previous version of this record has been published and now, for
        this new record version, the record goes out of the filter
        range.
    :ivar filter_exit_management_extension:
    """
    filter_end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterEnd",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    filter_out_of_range: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOutOfRange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    filter_exit_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterExitManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class FilterReference:
    """
    Details of a supplier's filter in a data exchange context.

    :ivar delete_filter: Indicates that a client defined filter has to
        be deleted.
    :ivar filter_operation_approved: Indicates that a client defined
        filter was either stored or deleted successfully.
    :ivar key_filter_reference: The unique key identifier of a supplier
        applied filter.
    :ivar filter_reference_extension:
    """
    delete_filter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteFilter",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    filter_operation_approved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOperationApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    key_filter_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyFilterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    filter_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GrossWeightCharacteristic:
    """
    Gross weight characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar gross_vehicle_weight: The gross weight of the vehicle and its
        load, including any trailers.
    :ivar gross_weight_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfLocations:
    """One or more physically separate locations.

    Multiple locations may be related, as in an itinerary (or route), or
    may be unrelated. It is not for identifying the same physical
    location using different Location objects for different referencing
    systems.
    """
    group_of_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfPeopleInvolved:
    """
    Group of people involved in the event having common characteristics and/or
    status.

    :ivar number_of_people: The number of people of this group that are
        involved.
    :ivar injury_status: The injury status of the people involved.
    :ivar involvement_role: The involvement role of the people.
    :ivar category_of_people_involved: The category of persons involved.
    :ivar group_of_people_involved_extension:
    """
    number_of_people: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    injury_status: Optional[InjuryStatusTypeEnum] = field(
        default=None,
        metadata={
            "name": "injuryStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    involvement_role: Optional[InvolvementRolesEnum] = field(
        default=None,
        metadata={
            "name": "involvementRole",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    category_of_people_involved: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "categoryOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_people_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfPeopleInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class HeaderInformation:
    """
    Management information relating to the data contained within a publication.

    :ivar area_of_interest: The extent of the geographic area to which
        the related information should be distributed.
    :ivar confidentiality: The extent to which the related information
        may be circulated, according to the recipient type. Recipients
        must comply with this confidentiality statement.
    :ivar information_status: The status of the related information
        (real, test, exercise ....).
    :ivar urgency: This indicates the urgency with which a message
        recipient or Client should distribute the enclosed information.
        Urgency particularly relates to functions within RDS-TMC
        applications.
    :ivar header_information_extension:
    """
    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "areaOfInterest",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    confidentiality: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    information_status: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    urgency: Optional[UrgencyEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class HeaviestAxleWeightCharacteristic:
    """
    Weight characteristic of the heaviest axle on the vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar heaviest_axle_weight: The weight of the heaviest axle on the
        vehicle.
    :ivar heaviest_axle_weight_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    heaviest_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    heaviest_axle_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class HeightCharacteristic:
    """
    Height characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_height: The height of the highest part, excluding
        antennae, of an individual vehicle above the road surface, in
        metres.
    :ivar height_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    height_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class InternationalIdentifier:
    """
    An identifier/name whose range is specific to the particular country.

    :ivar country: ISO 3166-1 two character country code.
    :ivar national_identifier: Identifier or name unique within the
        specified country.
    :ivar international_identifier_extension:
    """
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LengthCharacteristic:
    """
    Length characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_length: The overall distance between the front and
        back of an individual vehicle, including the length of any
        trailers, couplings, etc.
    :ivar length_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    length_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "lengthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LifeCycleManagement:
    """
    Information relating to the life cycle management of the situation record.

    :ivar cancel: Indication that all the element information previously
        sent is not considered valid, due to an incorrect content.
    :ivar end: A binary attribute specifying whether the situation
        element is finished (true) or not (false). If finished (i.e. end
        is true) then the overallEndTime in the OverallPeriod class
        associated with the SituationRecord must be populated.
    :ivar life_cycle_management_extension:
    """
    cancel: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    end: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    life_cycle_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "lifeCycleManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LocationCharacteristicsOverride:
    """
    Location characteristics which override values set in the referenced
    measurement point.

    :ivar measurement_lanes_override: Overrides for this single measured
        value instance the lane(s) defined for the set of measurements.
    :ivar reversed_flow: Indicates that the direction of flow for the
        measured lane(s) is the reverse of the normal direction of
        traffic flow.  Default is "no", which indicates traffic flow is
        in the normal sense as defined by the referenced measurement
        point.
    :ivar location_characteristics_override_extension:
    """
    measurement_lanes_override: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "measurementLanesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reversed_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reversedFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_characteristics_override_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverrideExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maintenance_vehicle_actions: List[MaintenanceVehicleActionsEnum] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceVehicleActions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maintenance_vehicles_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceVehiclesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar mobility_extension:
    """
    mobility_type: Optional[MobilityEnum] = field(
        default=None,
        metadata={
            "name": "mobilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    mobility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "mobilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MultilingualString:
    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "min_occurs": 1,
            }
        )


@dataclass
class NumberOfAxlesCharacteristic:
    """
    Number of axles characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar number_of_axles: The total number of axles of an individual
        vehicle.
    :ivar number_of_axles_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_axles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfAxles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_axles_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "numberOfAxlesCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OffsetDistance:
    """
    The non negative offset distance from the ALERT-C referenced point to the
    actual point.

    :ivar offset_distance: The non negative offset distance from the
        ALERT-C referenced point to the actual point. The ALERT-C
        locations in the Primary and Secondary locations must always
        encompass the linear section being specified, thus Offset
        Distance is towards the other point.
    :ivar offset_distance_extension:
    """
    offset_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    offset_distance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "offsetDistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrAreaLocationReference:
    """a two-dimensional part of the surface of the earth which is bounded by a
    closed curve.

    An area location may cover parts of the road network but does not
    necessarily need to. It is represente according to the OpenLR
    standard for Area Locations
    """
    openlr_area_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrAreaLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrGridAttributes:
    """
    attributes required for the grid method.

    :ivar openlr_num_columns: the number that the base rectangle should
        be multiplied in the east direction
    :ivar openlr_num_rows: the number that the base rectangle should be
        multiplied in the north direction
    :ivar openlr_grid_attributes_extension:
    """
    openlr_num_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNumColumns",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_num_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNumRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_grid_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrGridAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrLineAttributes:
    """
    Line attributes are part of a location reference point and consists of
    functional road class (FRC),form of way (FOW) and bearing (BEAR) data.

    :ivar openlr_functional_road_class: The functional road class (FRC)
        can hold eight different values as described in the logical
        format.
    :ivar openlr_form_of_way: The form of way (FOW) can hold eight
        different values as described in the logical format.
    :ivar openlr_bearing: defines the bearing field as an integer value
        between 0 and 360 whereby “0” is included and “360” is excluded
        from that range.
    :ivar openlr_line_attributes_extension:
    """
    openlr_functional_road_class: Optional[OpenlrFunctionalRoadClassEnum] = field(
        default=None,
        metadata={
            "name": "openlrFunctionalRoadClass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_form_of_way: Optional[OpenlrFormOfWayEnum] = field(
        default=None,
        metadata={
            "name": "openlrFormOfWay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_line_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLineAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrOffsets:
    """
    Offsets are used to locate the start and end of a location more precisely
    than bounding to the nodes in a network.

    :ivar openlr_positive_offset: The positive offset along the line of
        the location.
    :ivar openlr_negative_offset: The negative offset along the line of
        the location.
    :ivar openlr_offsets_extension:
    """
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_negative_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNegativeOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_offsets_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrOffsetsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrPathAttributes:
    """
    The field path attributes is part of a location reference point (except for
    the last location reference point) and consists of lowest functional road
    class (LFRCNP) and distance to next point (DNP) data.

    :ivar openlr_lowest_frcto_next_lrpoint: The lowest FRC to the next
        point indicates the lowest functional road class used in the
        location reference path to the next LR-point.
    :ivar openlr_distance_to_next_lrpoint: The DNP attribute measures
        the distance in meters between two consecutive LR-points along
        the location reference path as described in the logical format.
    :ivar openlr_path_attributes_extension:
    """
    openlr_lowest_frcto_next_lrpoint: Optional[OpenlrFunctionalRoadClassEnum] = field(
        default=None,
        metadata={
            "name": "openlrLowestFRCToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_distance_to_next_lrpoint: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrDistanceToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_path_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPathAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingEquipmentOrServiceFacilityStatus:
    """The number of E&amp;S can be overridden here (for example during
    restoration).

    Furthermore, the current availability of E&amp;S can be given (for
    example number of free electric charging stations). The E&amp;S are
    identified from the static model by an index.

    :ivar number_of_equipment_or_service_facility_override: Overrides
        the static value 'numberOfEquipmentOrServiceFacility' (for
        example because of long- or midterm closures, such as
        renovation).
    :ivar number_of_subitems_override: Overrides the static value
        'numberOfSubitems' (for example because of long- or midterm
        closures, such as renovation).
    :ivar vacant_equipment_or_service_facility_subitems: Sets the number
        of currently vacant elements of either equipment (e.g. free
        toilets) or service facility sub items (e.g. free restaurant
        places).
    :ivar service_facility_opening_status: Specifies whether this
        service facility is open or not.
    :ivar equipment_operation_status: Specifies whether this equipment
        is available / is in operation or not.
    :ivar parking_equipment_or_service_facility_status_extension:
    """
    number_of_equipment_or_service_facility_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfEquipmentOrServiceFacilityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_subitems_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubitemsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vacant_equipment_or_service_facility_subitems: Optional[int] = field(
        default=None,
        metadata={
            "name": "vacantEquipmentOrServiceFacilitySubitems",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    service_facility_opening_status: Optional[OpeningStatusEnum] = field(
        default=None,
        metadata={
            "name": "serviceFacilityOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    equipment_operation_status: Optional[OperationStatusEnum] = field(
        default=None,
        metadata={
            "name": "equipmentOperationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingPermit:
    """
    A permission for parking.

    :ivar parking_permit_type: Type of permission for parking.
    :ivar parking_permit_scheme: Scheme of permission for parking.
    :ivar parking_permit_identifier: Identifier of permission for
        parking.
    :ivar parking_permit_extension:
    """
    parking_permit_type: Optional[PermitTypeEnum] = field(
        default=None,
        metadata={
            "name": "parkingPermitType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_permit_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingPermitScheme",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    parking_permit_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingPermitIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    parking_permit_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingPermitExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSpaceStatus:
    """
    Status (occupied or closed) for a single parking space which was defined in
    the static part of the model.

    :ivar parking_space_occupied: True: Parking space is occupied;
        False: Parking space is free.
    :ivar parking_space_closed: True: The parking space is closed / not
        accessible. False or omitted: The parking space is accessible.
        This is no statement about its occupation.
    :ivar parking_space_declaration_valid_now: Override validity of
        'ParkingSpace': True = Parking space declaration is valid now;
        False = Parking space declaration is invalid now; Omitted =
        Static validity information is significant (if static validity
        is omitted too, declaration is valid).
    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar last_calibration: Date of last calibration of the detection
        system in question.
    :ivar parking_space_status_extension:
    """
    parking_space_occupied: Optional[bool] = field(
        default=None,
        metadata={
            "name": "parkingSpaceOccupied",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "parkingSpaceClosed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_declaration_valid_now: Optional[bool] = field(
        default=None,
        metadata={
            "name": "parkingSpaceDeclarationValidNow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_or_calculation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    last_calibration: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastCalibration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSpaceStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingUsageScenarioStatus:
    """
    The current status for this parking usage scenario.

    :ivar usage_scenario_operation_status: The current status for this
        parking usage scenario.
    :ivar parking_usage_scenario_status_extension:
    """
    usage_scenario_operation_status: Optional[OperationStatusEnum] = field(
        default=None,
        metadata={
            "name": "usageScenarioOperationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_usage_scenario_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PermitsAndProhibitions:
    """
    Defines sets of action and regulations to specify permitted and prohibited
    issues.

    :ivar activity: An activity, which is regulated.
    :ivar regulation: Regulation for the specified activity.
    :ivar permits_and_prohibitions_extension:
    """
    activity: Optional[RestAreaActivityEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    regulation: Optional[RegulationEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    permits_and_prohibitions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "permitsAndProhibitionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PictogramDisplayAreaSettings:
    """
    Settings specific to a distinct pictogram display area on the VMS (where
    pictogramIndex indicates which pictogram area it relates to if there is
    more than one pictogram display area on the VMS).

    :ivar pictogram_lanterns_on: Indicates if the lanterns are turned on
        or off for the pictogram display area.
    :ivar pictogram_luminance_override: Indicates whether the automatic
        luminance level of the VMS for the pictogram display area is
        being overriden (i.e. by a level set by the instation or
        operator).
    :ivar pictogram_luminance_level: Luminance level, expressed as an
        integer, that is set for the pictogram display area of the VMS.
        This may be set automatically by the VMS or by the instation or
        operator.
    :ivar pictogram_luminance_level_name: Luminance level, expressed as
        a symbolic name, that is set for the pictogram display area of
        the VMS. This may be set automatically by the VMS or by the
        instation or operator.
    :ivar pictogram_display_area_settings_extension:
    """
    pictogram_lanterns_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramLanternsOn",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_luminance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_luminance_level_name: Optional[VmsLuminanceLevelEnum] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceLevelName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_display_area_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PointCoordinates:
    """
    A pair of coordinates defining the geodetic position of a single point
    using the European Terrestrial Reference System 1989 (ETRS89).

    :ivar latitude: Latitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar longitude: Longitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar point_coordinates_extension:
    """
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    point_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PredefinedLocationContainer:
    """
    A container which may comprise the definition of a predefined itinerary,
    non ordered group of locations or single location.
    """
    predefined_location_container_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationContainerExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    subject_type_of_works: Optional[SubjectTypeOfWorksEnum] = field(
        default=None,
        metadata={
            "name": "subjectTypeOfWorks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_subjects: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubjects",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subjects_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subjectsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Target:
    """
    The details of a DATEX II target client.

    :ivar address: The IP address of a DATEX II target client.
    :ivar protocol: The exchange protocol used between the supplier and
        the client.
    :ivar target_extension:
    """
    address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    target_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "targetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TextDisplayAreaSettings:
    """
    Settings specific to a distinct text display area on the VMS.

    :ivar text_lanterns_on: Indicates if the lanterns are turned on or
        off for the text display area.
    :ivar text_luminance_override: Indicates whether the automatic
        luminance level of the VMS for the text display area is being
        overriden (i.e. by a level set by the instation or operator).
    :ivar text_luminance_level: Luminance level, expressed as an
        integer, that is set for the text display area of the VMS. This
        may be set automatically by the VMS or by the instation or
        operator.
    :ivar text_luminance_level_name: Luminance level, expressed as a
        symbolic name, that is set for the text display area of the VMS.
        This may be set automatically by the VMS or by the instation or
        operator.
    :ivar text_display_area_settings_extension:
    """
    text_lanterns_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textLanternsOn",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_luminance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textLuminanceOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "textLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_luminance_level_name: Optional[VmsLuminanceLevelEnum] = field(
        default=None,
        metadata={
            "name": "textLuminanceLevelName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_display_area_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "textDisplayAreaSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TimePeriodOfDay:
    """
    Specification of a continuous period of time within a 24 hour period.
    """
    time_period_of_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodOfDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegHeight:
    """
    Height information which provides additional discrimination for the
    applicable area.

    :ivar height: A measurement of height in metres
    :ivar height_type: A descriptive identification of relative height
        using TPEG-Loc location referencing.
    :ivar tpeg_height_extension:
    """
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    height_type: Optional[TpegLoc04HeightTypeEnum] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_height_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegPoint:
    """
    A point on the road network which is either a junction point or a non
    junction point.
    """
    tpeg_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegPointLocation:
    """
    A single point on the road network defined by a TPEG-Loc structure and
    which has an associated direction of traffic flow.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_point_location_extension:
    """
    tpeg_direction: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class UsedPaymentCard:
    """
    The used payment card for this parking vehicle.

    :ivar payment_card: Use this class to describe details in case
        usedMeansOfPayment is set to 'paymentCard'.
    :ivar other_payment_card: The payment card used for this parking
        vehicle in case the paymentCard attribute is set to 'other'.
    :ivar payment_card_brand: The payment card brand used for this
        parking vehicle.
    :ivar other_payment_card_brand: The payment card brand used for this
        parking vehicle in case the paymentCardBrand attribute is set to
        'other'.
    :ivar used_payment_card_extension:
    """
    payment_card: Optional[PaymentCardTypesEnum] = field(
        default=None,
        metadata={
            "name": "paymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    other_payment_card: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherPaymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    payment_card_brand: Optional[PaymentCardBrandsEnum] = field(
        default=None,
        metadata={
            "name": "paymentCardBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_payment_card_brand: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherPaymentCardBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    used_payment_card_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "usedPaymentCardExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleCharacteristicsExtended:
    """
    Extension point for 'VehicleCharacteristics' to support additional
    attributes and literals like additional fuel types, load types etc.

    :ivar emission_classification: The valid list of entries for this
        attribute has to be specified between the communication-
        partners. Usually it's some country specific classification code
        for emissions, which must be scored by vehicles to be valid.
    :ivar operation_free_of_emission: Only vehicles that do not produce
        emissions (e.g. electric driven). Hybrid driven cars are
        allowed, when they switch to emission free mode within the
        considered situation.
    :ivar load_type2: Loads currently not supported in 'LoadTypeEnum'.
    :ivar vehicle_type2: Vehicle types currently not supported in
        'VehicleTypeEnum'.
    :ivar fuel_type2: Fuel types currently not supported in
        'FuelTypeEnum'.
    :ivar vehicle_usage2: Usage types currently not supported in
        'VehicleUsageTypeEnum'.
    """
    emission_classification: List[str] = field(
        default_factory=list,
        metadata={
            "name": "emissionClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    operation_free_of_emission: Optional[bool] = field(
        default=None,
        metadata={
            "name": "operationFreeOfEmission",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    load_type2: Optional[LoadType2Enum] = field(
        default=None,
        metadata={
            "name": "loadType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_type2: Optional[VehicleType2Enum] = field(
        default=None,
        metadata={
            "name": "vehicleType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    fuel_type2: Optional[FuelType2Enum] = field(
        default=None,
        metadata={
            "name": "fuelType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_usage2: Optional[VehicleUsage2Enum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsSetting:
    """
    Provides information on variable message signs and the information
    currently displayed.
    """
    vms_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsSupplementaryPanelCharacteristics:
    """
    Characteristics of a panel which may display details (sometimes regulatory
    in nature) that are supplemental to the main pictogram, comprising an
    additional line of text and/or a pictogram.

    :ivar supplementary_pictogram_code_list_identifier: Indicates which
        supplementary pictogram code list is referenced.
    :ivar supplementary_panel_pixels_across: Number of pixels
        horizontally across the supplementary panel display area.
    :ivar supplementary_panel_pixels_down: Number of pixels vertically
        down the supplementary panel display area.
    :ivar supplementary_panel_display_height: The vertical height
        measured in metres of the supplementary panel display area.
    :ivar supplementary_panel_display_width: The horizontal width
        measured in metres of the supplementary panel display area.
    :ivar supplementary_panel_position_x: The X-coordinate (horizontal)
        position of the supplementary panel measured from the bottom
        left of the sign's overall display area to the bottom left of
        the supplementary panel.
    :ivar supplementary_panel_position_y: The Y-coordinate (vertical)
        position of the supplementary panel measured from the bottom
        left of the sign's overall display area to the bottom left of
        the supplementary panel.
    :ivar relative_position_to_pictogram_area: The position of the panel
        in which the supplementary details are displayed relative to the
        position of the pictogram display area which it is used to
        qualify (e.g. below).
    :ivar vms_supplementary_panel_characteristics_extension:
    """
    supplementary_pictogram_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    supplementary_panel_pixels_across: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_panel_pixels_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_panel_display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_panel_display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_panel_position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_panel_position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    relative_position_to_pictogram_area: Optional[PositionRelativeEnum] = field(
        default=None,
        metadata={
            "name": "relativePositionToPictogramArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_panel_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanelCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsTextDisplayCharacteristics:
    """
    Characteristics specific to the textual display area on the VMS.

    :ivar text_lanterns_present: Indicates whether the VMS is equipped
        with flashing lanterns associated with the textual display area.
    :ivar text_page_sequencing_capable: Indicates whether the text
        display on the VMS is capable of sequencing through multiple
        pages of text. True = capable.
    :ivar text_pixels_across: Number of pixels horizontally across the
        textual display area of the VMS.
    :ivar text_pixels_down: Number of pixels vertically down the textual
        display area of the VMS.
    :ivar text_display_height: The vertical height measured in metres of
        the specific text display area.
    :ivar text_display_width: The horizontal width measured in metres of
        the specific text display area.
    :ivar max_number_of_characters: Maximum number of displayable
        characters on a single line in the textual display area of the
        VMS.
    :ivar max_number_of_rows: Maximum number of rows of displayable
        characters in the textual display area of the VMS.
    :ivar legend_code_list_identifier: Indicates which legend/text code
        list is referenced. This may be specific to the VMS type defined
        by vmsTypeCode.
    :ivar max_font_height: Maximum font height in pixels.
    :ivar min_font_height: Minimum font height in pixels.
    :ivar max_font_width: Maximum font width in pixels.
    :ivar min_font_width: Minimum font width in pixels.
    :ivar max_font_spacing: Maximum font spacing in pixels.
    :ivar min_font_spacing: Minimum font spacing in pixels.
    :ivar max_text_luminance_level: Maximum integer luminance level that
        is available on the textual display area of the VMS.
    :ivar max_number_of_sequential_pages: Maximum number of text pages
        which the VMS is capable of scrolling through sequentially, (2
        to n).
    :ivar text_position_absolute: The position of the area in which the
        text is displayed, e.g. at the left, right, top or bottom of the
        VMS display.
    :ivar text_position_x: The X-coordinate (horizontal) position of the
        area in which the text is displayed measured from the bottom
        left of the sign's overall display area to the bottom left of
        the specific text display area.
    :ivar text_position_y: The Y-coordinate (vertical) position of the
        area in which the text is displayed measured from the bottom
        left of the sign's overall display area to the bottom left of
        the specific text display area.
    :ivar vms_text_display_characteristics_extension:
    """
    text_lanterns_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textLanternsPresent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_page_sequencing_capable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textPageSequencingCapable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_pixels_across: Optional[int] = field(
        default=None,
        metadata={
            "name": "textPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_pixels_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "textPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "textDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "textDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_number_of_characters: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfCharacters",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_number_of_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    legend_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "legendCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    max_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    min_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    min_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    min_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_text_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxTextLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_number_of_sequential_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfSequentialPages",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_position_absolute: Optional[PositionAbsoluteEnum] = field(
        default=None,
        metadata={
            "name": "textPositionAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_display_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTextDisplayCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsTextLine:
    """
    A single line of text on a text display area or supplementary panel.

    :ivar vms_text_line: A free-text string that is displayed on a
        single line on the text display area.
    :ivar vms_text_line_language: The language of the displayed line of
        text, specified by an ISO 639-2 3-alpha code.
    :ivar vms_text_line_colour: The colour of the displayed line of
        text.
    :ivar vms_text_line_flashing: Indication of whether the displayed
        line of text is flashing.
    :ivar vms_text_line_html: The displayed line of text defined by an
        HTML string showing text formatting tags.
    :ivar vms_text_line_extension:
    """
    vms_text_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    vms_text_line_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLineLanguage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_colour: Optional[ColourEnum] = field(
        default=None,
        metadata={
            "name": "vmsTextLineColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vmsTextLineFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_html: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLineHtml",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_text_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTextLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class WidthCharacteristic:
    """
    Width characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_width: The maximum width of an individual vehicle, in
        metres.
    :ivar width_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    width_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "widthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ChargeBandVersionedReference(VersionedReference):
    class Meta:
        name = "_ChargeBandVersionedReference"

    target_class: str = field(
        init=False,
        default="ChargeBand",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ContactDetailsVersionedReference(VersionedReference):
    class Meta:
        name = "_ContactDetailsVersionedReference"

    target_class: str = field(
        init=False,
        default="ContactDetails",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MeasurementSiteRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_MeasurementSiteRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="MeasurementSiteRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MeasurementSiteTableVersionedReference(VersionedReference):
    class Meta:
        name = "_MeasurementSiteTableVersionedReference"

    target_class: str = field(
        init=False,
        default="MeasurementSiteTable",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingAccessReference(Reference):
    class Meta:
        name = "_ParkingAccessReference"

    target_class: str = field(
        init=False,
        default="ParkingAccess",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_ParkingRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="ParkingRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingRouteDetailsVersionedReference(VersionedReference):
    class Meta:
        name = "_ParkingRouteDetailsVersionedReference"

    target_class: str = field(
        init=False,
        default="ParkingRouteDetails",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingTableVersionedReference(VersionedReference):
    class Meta:
        name = "_ParkingTableVersionedReference"

    target_class: str = field(
        init=False,
        default="ParkingTable",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedItineraryVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedItineraryVersionedReference"

    target_class: str = field(
        init=False,
        default="PredefinedItinerary",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedLocationVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedLocationVersionedReference"

    target_class: str = field(
        init=False,
        default="PredefinedLocation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedNonOrderedLocationGroupVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedNonOrderedLocationGroupVersionedReference"

    target_class: str = field(
        init=False,
        default="PredefinedNonOrderedLocationGroup",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SituationRecordExtensionType:
    class Meta:
        name = "_SituationRecordExtensionType"

    situation_record_extended_approved: Optional[SituationRecordExtendedApproved] = field(
        default=None,
        metadata={
            "name": "situationRecordExtendedApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class SituationRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="SituationRecord",
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
        default="Situation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsUnitRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_VmsUnitRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="VmsUnitRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsUnitTableVersionedReference(VersionedReference):
    class Meta:
        name = "_VmsUnitTableVersionedReference"

    target_class: str = field(
        init=False,
        default="VmsUnitTable",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlertCDirection:
    """
    The direction of traffic flow along the road to which the information
    relates.

    :ivar alert_cdirection_coded: The direction of traffic flow to which
        the situation, traffic data or information is related. Positive
        is in the direction of coding of the road.
    :ivar alert_cdirection_named: ALERT-C name of a direction e.g.
        Brussels -&gt; Lille.
    :ivar alert_cdirection_sense: Indicates for circular routes (i.e.
        valid only for ring roads) the sense in which navigation should
        be made from the primary location to the secondary location, to
        avoid ambiguity. TRUE indicates positive RDS direction, i.e.
        direction of coding of road.
    :ivar alert_cdirection_extension:
    """
    alert_cdirection_coded: Optional[AlertCDirectionEnum] = field(
        default=None,
        metadata={
            "name": "alertCDirectionCoded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cdirection_named: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCDirectionNamed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    alert_cdirection_sense: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alertCDirectionSense",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    alert_cdirection_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCDirectionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCLocation:
    """
    Identification of a specific point, linear or area location in an ALERT-C
    location table.

    :ivar alert_clocation_name: Name of ALERT-C location.
    :ivar specific_location: Unique code within the ALERT-C location
        table which identifies the specific point, linear or area
        location.
    :ivar alert_clocation_extension:
    """
    alert_clocation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    specific_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "specificLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_clocation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class BasicData:
    """
    Data that is either measured or calculated (elaborated) at the same time or
    over the same time period.

    :ivar measurement_or_calculation_period: The time elapsed between
        the beginning and the end of the sampling or measurement period.
        This item may differ from the unit attribute; e.g. an hourly
        flow can be estimated from a 5-minute measurement period.
    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar pertinent_location: The location (e.g. the stretch of road or
        area) to which the data value(s) is or are pertinent/relevant.
        This may be different from the location of the measurement
        equipment (i.e. the measurement site location).
    :ivar basic_data_extension:
    :ivar measurement_or_calculated_time_precision: The precision to
        which the time of measurement or calculation is given.
    """
    measurement_or_calculation_period: Optional[float] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_or_calculation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pertinent_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "pertinentLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    basic_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "basicDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_or_calculated_time_precision: Optional[TimePrecisionEnum] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculatedTimePrecision",
            "type": "Attribute",
        }
    )


@dataclass
class Charge:
    """
    A particular charge for a specified interval belonging a charge band.

    :ivar charge: Charge for the specified interval (for vehicle of
        defined characteristics, if any specified) up to the maximum
        defined duration and during the defined period(s).
    :ivar charge_interval: Interval for which the charge applies (e.g.
        charge applies for 2 hours (to specify in seconds)). If no
        interval is specified, the price is valid for the whole period
        (kind of flat fee).
    :ivar charge_type: The type of charge. Day- week- month- and year-
        charges can be specified without this enumeration by specifying
        the interval.
    :ivar charge_type_description: Additional description for this kind
        of charge type, especially if the enumeration does not fit.
    :ivar max_iterations_of_charge: This charge must not be applied more
        often within this charge band than specified in this attribute.
        Thus it is possible to specify the first hour for free, for
        example.
    :ivar min_iterations_of_charge: This charge must be applied within
        this charge band at least as often as specified in this
        attribute. Thus it is possible to specify the first hour in an
        expensive manner, for example.
    :ivar charge_order_index: A non-unique index which forms an order
        for applying charges, i.e. a charge may never be applied
        afterwards a charge with a higher index. For same indices there
        is no order-restriction. You can skip charges unless their
        'minIterationsOfCharge' is not &gt; 0.
    :ivar time_period_of_day: The TimePeriodOfDay limits the validity of
        the charge to this period (e.g. night-tariffs).
    :ivar charge_extension:
    """
    charge: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        }
    )
    charge_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "chargeInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_type: Optional[ChargeTypeEnum] = field(
        default=None,
        metadata={
            "name": "chargeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_type_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chargeTypeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_iterations_of_charge: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxIterationsOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    min_iterations_of_charge: Optional[int] = field(
        default=None,
        metadata={
            "name": "minIterationsOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_order_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "chargeOrderIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_period_of_day: Optional[TimePeriodOfDay] = field(
        default=None,
        metadata={
            "name": "timePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "chargeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ChargeBandByReference:
    """
    Using (a) prior defined charge band(s), identified by its reference.

    :ivar charge_band_reference: A reference to a charge band.
    :ivar charge_band_by_reference_extension:
    """
    charge_band_reference: Optional[ChargeBandVersionedReference] = field(
        default=None,
        metadata={
            "name": "chargeBandReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    charge_band_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "chargeBandByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    comment_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    comment_type: Optional[CommentTypeEnum] = field(
        default=None,
        metadata={
            "name": "commentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    comment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DataValue:
    """A data value of something that can be measured or calculated.

    Any provided meta-data values specified in the attributes override
    any specified generic characteristics such as defined for a specific
    measurement in the MeasurementSiteTable.

    :ivar data_error: Indication of whether the value is deemed to be
        erroneous by the supplier, (true = erroneous). If not present
        the data value is assumed to be ok. This may be used when
        automatic fault detection information relating to sensors is
        available.
    :ivar reason_for_data_error: The reason why the value is deemed to
        be erroneous by the supplier.
    :ivar data_value_extension:
    :ivar accuracy: The extent to which the value is expected to be free
        from error, measured as a percentage of the data value. 100%
        means fully accurate.
    :ivar computational_method: Method of computation which has been
        used to compute this data value.
    :ivar number_of_incomplete_inputs: The number of inputs detected but
        not completed during the sampling or measurement period; e.g.
        vehicles detected entering but not exiting the detection zone.
    :ivar number_of_input_values_used: The number of input values used
        in the sampling or measurment period to determine the data
        value.
    :ivar smoothing_factor: Coefficient required when a moving average
        is computed to give specific weights to the former average and
        the new data. A typical formula is, F being the smoothing
        factor: New average = (old average) F + (new data) (1 - F).
    :ivar standard_deviation: The standard deviation of the sample of
        input values from which this value was derived, measured in the
        units of the data value.
    :ivar supplier_calculated_data_quality: A measure of data quality
        assigned to the value by the supplier. 100% equates to
        ideal/perfect quality. The method of calculation is supplier
        specific and needs to be agreed between supplier and client.
    """
    data_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reason_for_data_error: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForDataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    computational_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Attribute",
        }
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Attribute",
        }
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Attribute",
        }
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Attribute",
        }
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Attribute",
        }
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Attribute",
        }
    )


@dataclass
class DedicatedAccess:
    """
    Reference to an access of any type (vehicles, pedestrian, ...).

    :ivar dedicated_access: Specifies a reference to an access, object
        (i.e. an entrance, an exit or both). A Point location and
        further characteristics can be specified for those objects.
    :ivar distance_from_parking_space: Distance from this access to the
        parking space or group of parking spaces. Especially interesting
        for handicapped people on the one hand or in case of the need of
        changing the side of a motorway.
    :ivar dedicated_access_extension:
    """
    dedicated_access: Optional[ParkingAccessReference] = field(
        default=None,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    distance_from_parking_space: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromParkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dedicated_access_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dedicatedAccessExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DistanceFromLinearElementStart(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node of
    the linear element, where start node is relative to the element definition
    rather than the direction of traffic flow.

    :ivar distance_along: A measure of distance along a linear element.
    :ivar distance_from_linear_element_start_extension:
    """
    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    distance_from_linear_element_start_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "distanceFromLinearElementStartExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ElaboratedDataFault(Fault):
    """
    Details of a fault which is being reported for the related elaborated data.

    :ivar elaborated_data_fault: The type of fault which is being
        reported for the specified elaborated data.
    :ivar elaborated_data_fault_extension:
    """
    elaborated_data_fault: Optional[ElaboratedDataFaultEnum] = field(
        default=None,
        metadata={
            "name": "elaboratedDataFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    elaborated_data_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ElectricCharging:
    """Additional information for the equipment 'electricChargingStation'.

    This component refers to the number of charging stations specified
    in the attribute 'numberOfEquipmentOrServiceFacilities'.

    :ivar charging_station_usage_type: Usage type of the electric
        charging station(s).
    :ivar charging_station_model_type: Model type of the electric
        charging station(s). Brand or company information can be
        specified in 'ParkingEquipmentOrServiceFacility'. For more than
        one type of model, use several instances of
        'ParkingEquipmentOrServiceFacility'.
    :ivar maximum_current: The maximum current of the electric charging
        station(s) (in Ampere).
    :ivar voltage: Available Voltage(s) of the electric charging
        station(s).
    :ivar charging_station_connector_type: Connector type(s) for the
        electric charging station(s).
    :ivar number_of_charging_points: Number of vehicles or devices,
        which can be charged simultaneously (sum over all electric
        charing stations specified with the 'numberOf...' attribute). If
        omitted, 1 charging point per station is assumed.
    :ivar electric_charging_extension:
    """
    charging_station_usage_type: List[ChargingStationUsageTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "chargingStationUsageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    charging_station_model_type: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chargingStationModelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumCurrent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    voltage: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charging_station_connector_type: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "chargingStationConnectorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_charging_points: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChargingPoints",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    electric_charging_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "electricChargingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class HazardousMaterials:
    """
    Details of hazardous materials.

    :ivar chemical_name: The chemical name of the hazardous substance
        carried by the vehicle.
    :ivar dangerous_goods_flash_point: The temperature at which the
        vapour from a hazardous substance will ignite in air.
    :ivar dangerous_goods_regulations: The code defining the
        regulations, international or national, applicable for a means
        of transport.
    :ivar hazard_code_identification: The dangerous goods description
        code.
    :ivar hazard_code_version_number: The version/revision number of
        date of issuance of the hazardous material code used.
    :ivar hazard_substance_item_page_number: A number giving additional
        hazard code classification of a goods item within the applicable
        dangerous goods regulation.
    :ivar trem_card_number: The identification of a transport emergency
        card giving advice for emergency actions.
    :ivar undg_number: A unique serial number assigned within the United
        Nations to substances and articles contained in a list of the
        dangerous goods most commonly carried.
    :ivar volume_of_dangerous_goods: The volume of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar weight_of_dangerous_goods: The weight of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar hazardous_materials_extension:
    """
    chemical_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    dangerous_goods_flash_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsFlashPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dangerous_goods_regulations: Optional[DangerousGoodsRegulationsEnum] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsRegulations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    hazard_code_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardCodeIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    hazard_code_version_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "hazardCodeVersionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    hazard_substance_item_page_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardSubstanceItemPageNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    trem_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "tremCardNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    undg_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "undgNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    volume_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "volumeOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    weight_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    hazardous_materials_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "hazardousMaterialsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar original_number_of_lanes: The normal number of usable lanes in
        the specified direction that the carriageway has before
        reduction due to roadworks or traffic events.
    :ivar residual_road_width: The total width of the combined
        operational lanes in the specified direction.
    :ivar traffic_constriction_type: The type of constriction to which
        traffic is subjected as a result of an event or operator action.
    :ivar delays:
    :ivar impact_extension:
    """
    capacity_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacityRemaining",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_lanes_restricted: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLanesRestricted",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_operational_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfOperationalLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    original_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    residual_road_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualRoadWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_constriction_type: Optional[TrafficConstrictionTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficConstrictionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    delays: Optional[Delays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    impact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "impactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class IndividualCharge:
    """
    Information on the individual charge for parking the specified vehicle.

    :ivar charge_band_reference: A reference to a charge band.
    :ivar charge_paid: The charge paid for this vehicle. If the vehicle
        is still parking, it's the charge amount accumulated so far.
    :ivar charge_currency: A three-character code according to ISO 4217
        for the currency in which the parking charge is specified (e.g.
        EUR, GBP, SEK, CZK).
    :ivar used_means_of_payment: The payment method used to pay for this
        parking vehicle. If it is 'paymentCard', use 'UsedPaymentCard'
        to specify more details.
    :ivar with_reservation: Specifies, whether there was a reservation
        made for this vehicle.
    :ivar used_payment_card:
    :ivar individual_charge_extension:
    """
    charge_band_reference: Optional[ChargeBandVersionedReference] = field(
        default=None,
        metadata={
            "name": "chargeBandReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_paid: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "chargePaid",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        }
    )
    charge_currency: Optional[CurrencyEnum] = field(
        default=None,
        metadata={
            "name": "chargeCurrency",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    used_means_of_payment: Optional[MeansOfPaymentEnum] = field(
        default=None,
        metadata={
            "name": "usedMeansOfPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    with_reservation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "withReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    used_payment_card: Optional[UsedPaymentCard] = field(
        default=None,
        metadata={
            "name": "usedPaymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    individual_charge_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "individualChargeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Itinerary(GroupOfLocations):
    """
    Multiple (i.e. more than one) physically separate locations arranged as an
    ordered set that defines an itinerary or route.

    :ivar route_destination: Destination of a route or final location in
        an itinerary.
    :ivar itinerary_extension:
    """
    route_destination: List[Destination] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LinearElement:
    """
    A linear element along a single linear object, consistent with ISO 19148
    definitions.

    :ivar road_name: Name of the road of which the linear element forms
        a part.
    :ivar road_number: Identifier/number of the road of which the linear
        element forms a part.
    :ivar linear_element_reference_model: The identifier of a road
        network reference model which segments the road network
        according to specific business rules.
    :ivar linear_element_reference_model_version: The version of the
        identified road network reference model.
    :ivar linear_element_nature: An indication of the nature of the
        linear element.
    :ivar linear_element_extension:
    """
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    linear_element_reference_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    linear_element_reference_model_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModelVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    linear_element_nature: Optional[LinearElementNatureEnum] = field(
        default=None,
        metadata={
            "name": "linearElementNature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Location(GroupOfLocations):
    """The specification of a location either on a network (as a point or a
    linear location) or as an area.

    This may be provided in one or more referencing systems.

    :ivar external_referencing:
    :ivar location_for_display: A location which may be used by clients
        for visual display on user interfaces.
    :ivar location_extension:
    """
    external_referencing: List[ExternalReferencing] = field(
        default_factory=list,
        metadata={
            "name": "externalReferencing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "locationForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ManagedCause(Cause):
    """
    A cause of this situation record which is managed by the publication
    creator, i.e. one which is represented by another situation record produced
    by the same publication creator.

    :ivar managed_cause: A reference to another situation record
        produced by the same publication creator which defines a cause
        of the event defined here.
    :ivar managed_cause_extension:
    """
    managed_cause: Optional[SituationRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Management:
    """
    Information relating to the management of the situation record.
    """
    life_cycle_management: Optional[LifeCycleManagement] = field(
        default=None,
        metadata={
            "name": "lifeCycleManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    filter_exit_management: Optional[FilterExitManagement] = field(
        default=None,
        metadata={
            "name": "filterExitManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasurementEquipmentFault(Fault):
    """
    Details of a fault which is being reported for the related measurement
    equipment.

    :ivar measurement_equipment_fault: The type of fault which is being
        reported for the specified measurement equipment.
    :ivar measurement_equipment_fault_extension:
    """
    measurement_equipment_fault: Optional[MeasurementEquipmentFaultEnum] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measurement_equipment_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NamedArea:
    """An area defined by a name and/or in terms of known boundaries, such as
    country or county boundaries or allocated control area of particular
    authority.

    The attributes do not form a union; instead, the smallest
    intersection forms the resulting area.

    :ivar country: ISO 3166-1 two character country code.
    :ivar nation: Name of a nation (e.g. Wales) which is a sub-division
        of an ISO recognised country.
    :ivar county: Name of a county (administrative sub-division).
    :ivar area_name: Name of an area.
    :ivar police_force_control_area: Name of a police force area.
    :ivar road_operator_control_area: Name of a road operator control
        area.
    :ivar named_area_extension:
    """
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    nation: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    county: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    area_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "areaName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    police_force_control_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "policeForceControlArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_operator_control_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadOperatorControlArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "namedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonManagedCause(Cause):
    """
    A cause of this situation record which is not managed by the publication
    creator, i.e. one which is not represented by another situation record
    produced by the same publication creator.

    :ivar cause_description: Description of a cause which is not managed
        by the publication creator (e.g. an off network cause).
    :ivar cause_type: Indicates an external influence that may be the
        causation of components of a situation.
    :ivar non_managed_cause_extension:
    """
    cause_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "causeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    cause_type: Optional[CauseTypeEnum] = field(
        default=None,
        metadata={
            "name": "causeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    non_managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonManagedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonOrderedLocations(GroupOfLocations):
    """
    Multiple (i.e. more than one) physically separate locations which have no
    specific order.
    """
    non_ordered_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonOrderedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrBaseLocationReferencePoint:
    """
    Base class used to hold data about a reference point.
    """
    openlr_coordinate: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_line_attributes: Optional[OpenlrLineAttributes] = field(
        default=None,
        metadata={
            "name": "openlrLineAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_base_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrBaseLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrExtendedArea:
    """
    Extension to provide Area information in openLR format.
    """
    openlr_area_location_reference: Optional[OpenlrAreaLocationReference] = field(
        default=None,
        metadata={
            "name": "openlrAreaLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )


@dataclass
class OpenlrGeoCoordinate:
    """
    A geo-coordinate pair is a position in a map defined by its longitude and
    latitude coordinate values.
    """
    openlr_coordinate: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_geo_coordinate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrPolygonCorners:
    """geo-coordinate pairs.

    The coordinate pairs defining the corners of the underlying
    geometrical polygon.
    """
    openlr_coordinate: List[PointCoordinates] = field(
        default_factory=list,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 3,
        }
    )
    openlr_polygon_corners_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPolygonCornersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrRectangle:
    """
    two geo-coordinate pairs defining the rectangular.

    :ivar openlr_lower_left: The lower left corner of the rectangle
    :ivar openlr_upper_right: the upper right corner of the rectangle
    :ivar openlr_rectangle_extension:
    """
    openlr_lower_left: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrLowerLeft",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_upper_right: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrUpperRight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_rectangle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrRectangleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingAccessStatus:
    """
    The opening and fault status of one access.

    :ivar access_reference: The reference to an access defined in the
        static part of the model.
    :ivar access_opening_status: The opening status of this access.
    :ivar access_fault: A fault indicator for this special access.
    :ivar parking_access_status_extension:
    """
    access_reference: Optional[ParkingAccessReference] = field(
        default=None,
        metadata={
            "name": "accessReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    access_opening_status: Optional[OpeningStatusEnum] = field(
        default=None,
        metadata={
            "name": "accessOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    access_fault: List[ParkingFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_access_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingAccessStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRouteStatus:
    """
    The status of a parking route (active/inactive) defined in the static part
    of the model.

    :ivar parking_route_reference: A reference to a parking route.
    :ivar parking_route_active: Defines if this parking route is
        currently active or not.
    :ivar parking_route_status_extension:
    """
    parking_route_reference: Optional[ParkingRouteDetailsVersionedReference] = field(
        default=None,
        metadata={
            "name": "parkingRouteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_route_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "parkingRouteActive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_route_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRouteStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingStandardsAndSecurity:
    """
    Security measures and standards or standard-like categorization for a
    parking site.

    :ivar label_security_level: Formal assessment for the security level
        defined by the LABEL project  http://truckparkinglabel.eu.
    :ivar label_service_level: Formal assessment for the service level
        defined by the LABEL project  http://truckparkinglabel.eu.
    :ivar label_security_level_self_assessment: Self-assessment for the
        security level defined by the LABEL project
        http://truckparkinglabel.eu.
    :ivar label_service_level_self_assessment: Self-assessment for the
        service level defined by the LABEL project
        http://truckparkinglabel.eu.
    :ivar parking_security: Specifies security measures related to the
        parking site or particular spaces.
    :ivar parking_additional_security: Security equipment of the parking
        site that is not covered by the enumeration
        'ParkingSecurityEnum'.
    :ivar parking_supervision: Defines the kind of supervision of the
        parking site.
    :ivar parking_security_national_classification: A national
        classification of the parking security.
    :ivar certified_secure_parking: Presence of a certification for
        secure parking.
    :ivar date_of_certification: Date of certification.
    :ivar parking_standards_and_security_extension:
    """
    label_security_level: Optional[LABELSecurityLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelSecurityLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_service_level: Optional[LABELServiceLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelServiceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_security_level_self_assessment: Optional[LABELSecurityLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelSecurityLevelSelfAssessment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_service_level_self_assessment: Optional[LABELServiceLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelServiceLevelSelfAssessment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_security: List[ParkingSecurityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_additional_security: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "parkingAdditionalSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_supervision: List[ParkingSupervisionEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSupervision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_security_national_classification: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingSecurityNationalClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    certified_secure_parking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "certifiedSecureParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    date_of_certification: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dateOfCertification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_standards_and_security_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingStandardsAndSecurityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PayloadPublication:
    """
    A payload publication of traffic related information or associated
    management information created at a specific point in time that can be
    exchanged via a DATEX II interface.

    :ivar feed_description: A description of the information which is to
        be found in the publications originating from the particular
        feed (URL).
    :ivar feed_type: A classification of the information which is to be
        found in the publications originating from the particular feed.
    :ivar publication_time: Date/time at which the payload publication
        was created.
    :ivar publication_creator:
    :ivar payload_publication_extension:
    :ivar lang: The default language used throughout the payload
        publication.
    """
    feed_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "feedDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PercentageDistanceAlongLinearElement(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node
    expressed as a percentage of the whole length of the linear element, where
    start node is relative to the element definition rather than the direction
    of traffic flow.

    :ivar percentage_distance_along: A measure of distance along a
        linear element from the start of the element expressed as a
        percentage of the total length of the linear object.
    :ivar percentage_distance_along_linear_element_extension:
    """
    percentage_distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentageDistanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    percentage_distance_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "percentageDistanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PointByCoordinates:
    """
    A single point defined only by a coordinate set with an optional bearing
    direction.

    :ivar bearing: A bearing at the point measured in degrees (0 - 359).
        Unless otherwise specified the reference direction corresponding
        to 0 degrees is North.
    :ivar point_coordinates:
    :ivar point_by_coordinates_extension:
    """
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PublicHoliday:
    """Specification of the public holiday type in a specific country or
    region.

    Use this component only when specialDayType is set to
    'publicHoliday' or 'holidays'.

    :ivar country: ISO 3166-1 two character country code.
    :ivar country_subdivision: ISO 3166-2 country sub-division code (up
        to 3 characters).
    :ivar region: Region of country (e.g. "Scotland", "Wales" etc. if
        country = GB)
    :ivar public_holiday_type: Specifies the public holiday type for the
        country or region.
    :ivar public_holiday_name: Specification of public holiday, if the
        enumeration values do not fit.
    :ivar public_holiday_extension:
    """
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    country_subdivision: Optional[str] = field(
        default=None,
        metadata={
            "name": "countrySubdivision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    region: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    public_holiday_type: Optional[PublicHolidayTypeEnum] = field(
        default=None,
        metadata={
            "name": "publicHolidayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    public_holiday_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "publicHolidayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    public_holiday_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "publicHolidayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class RGBColour:
    """
    An RGB colour described by values for red, green and blue (0..255) as well
    as an optional name.

    :ivar rgb_red_value: The red value of the RGB colour (0..255).
    :ivar rgb_green_value: The green value of the RGB colour (0..255).
    :ivar rgb_blue_value: The blue value of the RGB colour (0..255).
    :ivar colour_name: The name of the colour.
    :ivar rgb_colour_extension:
    """
    rgb_red_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "rgbRedValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    rgb_green_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "rgbGreenValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    rgb_blue_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "rgbBlueValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    colour_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "colourName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    rgb_colour_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "rgbColourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ReferenceSettings:
    """Specification of the default value for traffic status on a group of
    predefined locations on the road network.

    Only when traffic status differs from this value at a location in
    the group need a value be sent.

    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar traffic_status_default: The default value of traffic status
        that can be assumed to apply to the locations defined by the
        associated predefined location set.
    :ivar reference_settings_extension:
    """
    predefined_non_ordered_location_group_reference: Optional[PredefinedNonOrderedLocationGroupVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_status_default: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatusDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reference_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "referenceSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Referent:
    """
    A referent on a linear object that has a known location such as a node, a
    reference marker (e.g. a markerpost), an intersection etc.

    :ivar referent_identifier: The identifier of the referent, unique on
        the specified linear element (i.e. road or part of).
    :ivar referent_name: The name of the referent, e.g. a junction or
        intersection name.
    :ivar referent_type: The type of the referent.
    :ivar referent_description: Description of the referent.
    :ivar point_coordinates:
    :ivar referent_extension:
    """
    referent_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "referentIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    referent_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "referentName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    referent_type: Optional[ReferentTypeEnum] = field(
        default=None,
        metadata={
            "name": "referentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    referent_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "referentDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    referent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "referentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Road:
    """
    Identification of a road by its name, identifier, type ...

    :ivar name_of_road: The name of the road.
    :ivar road_identifier: Identifier/number of the road.
    :ivar type_of_road: Type of the road.
    :ivar road_destination: Name of some city, area, compass direction
        or other identification the road is leading to (to determine the
        direction in question).
    :ivar road_origination: Name of some city, area, compass direction
        or other identification this road comes from.
    :ivar distance_to_this_road: Distance to the road in metres (from
        the calling component/object).
    :ivar road_extension:
    """
    name_of_road: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "nameOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_identifier: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    type_of_road: Optional[RoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "typeOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_destination: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "roadDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_origination: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "roadOrigination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_to_this_road: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceToThisRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Source:
    """
    Details of the source from which the information was obtained.

    :ivar source_country: ISO 3166-1 two character country code of the
        source of the information.
    :ivar source_identification: Identifier of the organisation or the
        traffic equipment which has produced the information relating to
        this version of the information.
    :ivar source_name: The name of the organisation which has produced
        the information relating to this version of the information.
    :ivar source_type: Information about the technology used for
        measuring the data or the method used for obtaining qualitative
        descriptions relating to this version of the information.
    :ivar reliable: An indication as to whether the source deems the
        associated information to be reliable/correct. "True" indicates
        it is deemed reliable.
    :ivar source_extension:
    """
    source_country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "name": "sourceCountry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    source_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    source_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    source_type: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reliable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    source_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "sourceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Subscription:
    """
    This item contains all information relating to a customer subscription.

    :ivar delete_subscription: Indicates that this subscription has to
        be deleted.
    :ivar delivery_interval: Value of the interval of data delivery in
        the "periodic" delivery mode.
    :ivar operating_mode: The mode of operation of the exchange.
    :ivar subscription_start_time: Gives the date/time at which the
        subscription becomes active.
    :ivar subscription_state: The current state of the the client's
        subscription.
    :ivar subscription_stop_time: Gives the date/time at which the
        subscription expires.
    :ivar update_method: The type of updates of situations requested by
        the client.
    :ivar target:
    :ivar filter_reference:
    :ivar catalogue_reference:
    :ivar subscription_extension:
    """
    delete_subscription: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteSubscription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    delivery_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "deliveryInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    operating_mode: Optional[OperatingModeEnum] = field(
        default=None,
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    subscription_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    subscription_state: Optional[SubscriptionStateEnum] = field(
        default=None,
        metadata={
            "name": "subscriptionState",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    subscription_stop_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStopTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    update_method: Optional[UpdateMethodEnum] = field(
        default=None,
        metadata={
            "name": "updateMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    target: List[Target] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    filter_reference: Optional[FilterReference] = field(
        default=None,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    catalogue_reference: Optional[CatalogueReference] = field(
        default=None,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subscription_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subscriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SupplementaryPositionalDescription:
    """
    A collection of supplementary positional information which improves the
    precision of the location.

    :ivar location_descriptor: Specifies a descriptor which helps to
        identify the specific location.
    :ivar sequential_ramp_number: The sequential number of an
        exit/entrance ramp from a given location in a given direction
        (normally used to indicate a specific exit/entrance in a complex
        junction/intersection).
    :ivar affected_carriageway_and_lanes:
    :ivar supplementary_positional_description_extension:
    :ivar location_precision: Indicates that the location is given with
        a precision which is better than the stated value in metres.
    """
    location_descriptor: List[LocationDescriptorEnum] = field(
        default_factory=list,
        metadata={
            "name": "locationDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    sequential_ramp_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequentialRampNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    affected_carriageway_and_lanes: List[AffectedCarriagewayAndLanes] = field(
        default_factory=list,
        metadata={
            "name": "affectedCarriagewayAndLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "locationPrecision",
            "type": "Attribute",
        }
    )


@dataclass
class TimePeriodByHour(TimePeriodOfDay):
    """
    Specification of a continuous period within a 24 hour period by times.

    :ivar start_time_of_period: Start of time period.
    :ivar end_time_of_period: End of time period.
    :ivar time_period_by_hour_extension:
    """
    start_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    end_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    time_period_by_hour_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodByHourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegAreaLocation:
    """
    A geographic or geometric area defined by a TPEG-Loc structure which may
    include height information for additional geospatial discrimination.

    :ivar tpeg_area_location_type: The type of TPEG location.
    :ivar tpeg_height:
    :ivar tpeg_area_location_extension:
    """
    tpeg_area_location_type: Optional[TpegLoc01AreaLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegDescriptor:
    """
    A collection of information providing descriptive references to locations
    using the TPEG-Loc location referencing approach.

    :ivar descriptor: A text string which describes or elaborates the
        location.
    :ivar tpeg_descriptor_extension:
    """
    descriptor: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegLinearLocation:
    """
    A linear section along a single road defined between two points on the same
    road by a TPEG-Loc structure.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_linear_location_type: The type of TPEG location.
    :ivar to: The location at the down stream end of the linear section
        of road.
    :ivar from_value: The location at the up stream end of the linear
        section of road.
    :ivar tpeg_linear_location_extension:
    """
    tpeg_direction: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_type: Optional[TpegLoc01LinearLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegSimplePoint(TpegPointLocation):
    """
    A point on the road network which is not bounded by any other points on the
    road network.

    :ivar tpeg_simple_point_location_type: The type of TPEG location.
    :ivar point: A single point defined by a coordinate set and TPEG
        decriptors.
    :ivar tpeg_simple_point_extension:
    """
    tpeg_simple_point_location_type: Optional[TpegLoc01SimplePointLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    point: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_simple_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class UrlLink:
    """
    Details of a Uniform Resource Locator (URL) address pointing to a resource
    available on the Internet from where further relevant information may be
    obtained.

    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar url_link_description: Description of the relevant information
        available on the Internet from the URL link.
    :ivar url_link_type: Details of the type of relevant information
        available on the Internet from the URL link.
    :ivar url_link_extension:
    """
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    url_link_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "urlLinkDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link_type: Optional[UrlLinkTypeEnum] = field(
        default=None,
        metadata={
            "name": "urlLinkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "urlLinkExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign panel.

    :ivar vms_fault: The type of fault which is being reported for the
        specified variable message sign panel.
    :ivar vms_fault_extension:
    """
    vms_fault: Optional[VmsFaultEnum] = field(
        default=None,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsPictogramDisplayCharacteristics:
    """
    Characteristics specific to the pictogram display area(s) on the VMS where
    pictogramDisplayAreaIndex indicates which pictogram area it relates to.

    :ivar pictogram_lanterns_present: Indicates whether the VMS is
        equipped with flashing lanterns associated with the pictogram
        display area.
    :ivar pictogram_sequencing_capable: Indicates whether the pictogram
        display area on the VMS is capable of sequencing through
        multiple pictograms. True = capable.
    :ivar pictogram_pixels_across: Number of pixels horizontally across
        the pictogram display area of the VMS.
    :ivar pictogram_pixels_down: Number of pixels vertically down the
        pictogram display area of the VMS.
    :ivar pictogram_display_height: The vertical height measured in
        metres of the specific pictogram display area.
    :ivar pictogram_display_width: The horizontal width measured in
        metres of the specific pictogram display area.
    :ivar pictogram_code_list_identifier: Indicates which pictogram code
        list is referenced.
    :ivar max_pictogram_luminance_level: Maximum integer luminance level
        that is available on the pictogram display area of the VMS.
    :ivar pictogram_number_of_colours: The number of colours the
        pictogram display area is capable of rendering.
    :ivar max_number_of_sequential_pictograms: The maximum number of
        pictograms that can be sequenced through on the pictogram
        display area.
    :ivar pictogram_position_absolute: The position of the area in which
        the pictogram is displayed, i.e. at the left, right, top or
        bottom of the VMS display.
    :ivar pictogram_position_x: The X-coordinate (horizontal) position
        of the area in which the pictogram is displayed measured from
        the bottom left of the sign's overall display area to the bottom
        left of the specific pictogram display area.
    :ivar pictogram_position_y: The Y-coordinate (vertical) position of
        the area in which the pictogram is displayed measured from the
        bottom left of the sign's overall display area to the bottom
        left of the specific pictogram display area.
    :ivar pictogram_position_relative_to_text: The position of the area
        in which the pictogram is displayed relative to the textual area
        of the VMS (e.g. to the left, to the right ....).
    :ivar vms_supplementary_panel_characteristics:
    :ivar vms_pictogram_display_characteristics_extension:
    """
    pictogram_lanterns_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramLanternsPresent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_sequencing_capable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramSequencingCapable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_pixels_across: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_pixels_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    max_pictogram_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxPictogramLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_number_of_colours: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramNumberOfColours",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    max_number_of_sequential_pictograms: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfSequentialPictograms",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_position_absolute: Optional[PositionAbsoluteEnum] = field(
        default=None,
        metadata={
            "name": "pictogramPositionAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "pictogramPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "pictogramPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_position_relative_to_text: Optional[PositionRelativeEnum] = field(
        default=None,
        metadata={
            "name": "pictogramPositionRelativeToText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_panel_characteristics: Optional[VmsSupplementaryPanelCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanelCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsSupplementaryPictogram:
    """
    An additional pictogram that is displayed in the panel which is
    supplemental to the associated pictogram display.

    :ivar supplementary_pictogram_description: Description of the
        supplementary displayed pictogram.
    :ivar supplementary_pictogram_code: The code of the supplementary
        pictogram from the supplementary pictogram code list referenced
        in the VmsSupplementaryPanelCharacteristics for the VMS that is
        identified in the relevant VMS Unit table.
    :ivar supplementary_pictogram_url: Reference to a URL from where an
        image of the displayed supplementary pictogram can be be
        obtained.
    :ivar additional_supplementary_pictogram_description: Additional
        free text description of the supplementary pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar vms_supplementary_pictogram_extension:
    """
    supplementary_pictogram_description: Optional[VmsDatexSupplementalPictogramEnum] = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_pictogram_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    supplementary_pictogram_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    additional_supplementary_pictogram_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalSupplementaryPictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsUnitFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign control unit.

    :ivar vms_unit_fault: The type of fault which is being reported for
        the VMS unit.
    :ivar vms_unit_fault_extension:
    """
    vms_unit_fault: Optional[VmsFaultEnum] = field(
        default=None,
        metadata={
            "name": "vmsUnitFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_unit_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus:
    class Meta:
        name = "_ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus"

    parking_equipment_or_service_facility_status: Optional[ParkingEquipmentOrServiceFacilityStatus] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_service_facility_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "equipmentOrServiceFacilityIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus:
    class Meta:
        name = "_ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus"

    parking_space_status: Optional[ParkingSpaceStatus] = field(
        default=None,
        metadata={
            "name": "parkingSpaceStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus:
    class Meta:
        name = "_ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus"

    parking_usage_scenario_status: Optional[ParkingUsageScenarioStatus] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scenario_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PolygonAreaIndexPointCoordinates:
    class Meta:
        name = "_PolygonAreaIndexPointCoordinates"

    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VehicleCharacteristicsExtensionType:
    class Meta:
        name = "_VehicleCharacteristicsExtensionType"

    vehicle_characteristics_extended: Optional[VehicleCharacteristicsExtended] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings:
    class Meta:
        name = "_VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings"

    pictogram_display_area_settings: Optional[PictogramDisplayAreaSettings] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsTextLineIndexVmsTextLine:
    class Meta:
        name = "_VmsTextLineIndexVmsTextLine"

    vms_text_line: Optional[VmsTextLine] = field(
        default=None,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    line_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlertCArea:
    """
    An area defined by reference to a predefined ALERT-C location table.

    :ivar alert_clocation_country_code: EBU country code.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar area_location: Area location defined by a specific Alert-C
        location.
    :ivar alert_carea_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    area_location: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_carea_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCLinearByCode(AlertCLinear):
    """
    A linear section along a road defined by reference to a linear section in a
    pre-defined ALERT-C location table.

    :ivar alert_cdirection:
    :ivar location_code_for_linear_location: Linear location defined by
        a specific Alert-C location.
    :ivar alert_clinear_by_code_extension:
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    location_code_for_linear_location: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod2PrimaryPointLocation:
    """The point (called Primary point) which is either a single point or at
    the downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod2SecondaryPointLocation:
    """The point (called Secondary point) which is at the upstream end of a
    linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod4PrimaryPointLocation:
    """The point (called Primary point) which is either a single point or at
    the downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table plus a non-negative offset distance.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod4SecondaryPointLocation:
    """The point (called Secondary point) which is at the upstream end of a
    linear road section.

    The point is specified by a reference to a point in a pre-defined
    Alert-C location table plus a non-negative offset distance.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ApplicationRateValue(DataValue):
    """
    A measured or calculated value of the application rate of a substance.

    :ivar application_rate: A value of the rate of application of a
        substance expressed in kilogrammes per square metre.
    :ivar application_rate_value_extension:
    """
    application_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "applicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    application_rate_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "applicationRateValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AxleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicle axles.

    :ivar axle_flow_rate: A value of the flow rate of vehicle axles
        expressed in axles per hour.
    :ivar axle_flow_value_extension:
    """
    axle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ConcentrationOfVehiclesValue(DataValue):
    """
    A measured or calculated value of the concentration of vehicles on a unit
    stretch of road in a given direction.

    :ivar concentration_of_vehicles: A value of traffic density
        expressed in the number of vehicles per kilometre of road.
    :ivar concentration_of_vehicles_value_extension:
    """
    concentration_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "concentrationOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    concentration_of_vehicles_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "concentrationOfVehiclesValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DateTimeValue(DataValue):
    """
    A measured or calculated value of an instance in time.

    :ivar date_time: A time stamp defining an instance in time.
    :ivar date_time_value_extension:
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    date_time_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dateTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DirectionBearingValue(DataValue):
    """
    A measured or calculated value of direction as a bearing.

    :ivar direction_bearing: A value of direction expressed in terms of
        a bearing measured in whole degrees. Unless otherwise specified
        the reference direction corresponding to 0 degrees is North.
    :ivar direction_bearing_value_extension:
    """
    direction_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "directionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    direction_bearing_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "directionBearingValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DirectionCompassValue(DataValue):
    """
    A measured or calculated value of direction as a point of the compass.

    :ivar direction_compass: A value of direction expressed in terms of
        points of the compass.
    :ivar direction_compass_value_extension:
    """
    direction_compass: Optional[DirectionCompassEnum] = field(
        default=None,
        metadata={
            "name": "directionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    direction_compass_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "directionCompassValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DistanceFromLinearElementReferent(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from a "from referent"
    on the linear element, in the sense relative to the linear element
    definition rather than the direction of traffic flow or optionally towards
    a "towards referent".

    :ivar distance_along: A measure of distance along a linear element.
    :ivar from_referent: A known location along the linear element from
        which the distanceAlong is measured, termed the "fromReferent"
        in ISO 19148.
    :ivar towards_referent: A known location along the linear element
        towards which the distanceAlong is measured, termed the
        "towardsReferent" in ISO 19148.
    :ivar distance_from_linear_element_referent_extension:
    """
    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "fromReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    towards_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "towardsReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_linear_element_referent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "distanceFromLinearElementReferentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class DurationValue(DataValue):
    """
    A measured or calculated value of a period of time.

    :ivar duration: A period of time expressed in seconds.
    :ivar duration_value_extension:
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    duration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "durationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Exchange:
    """
    Details associated with the management of the exchange between the supplier
    and the client.

    :ivar changed_flag: Indicates that either a filter or a catalogue
        has been changed.
    :ivar client_identification: In a data exchange process, an
        identifier of the organisation or group of organisations which
        receives information from the DATEX II supplier system.
    :ivar delivery_break: Indicates that a data delivery is stopped for
        unplanned reasons, i.e. excluding the end of the order validity
        (attribute FIL) or the case when the filter expression is not
        met (attribute OOR).
    :ivar deny_reason: Indicates the reason for the refusal of the
        requested exchange.
    :ivar historical_start_date: For "Client Pull" exchange mode
        (operating mode 3 - snapshot) it defines the date/time at which
        the snapshot was produced.
    :ivar historical_stop_date: For "Client Pull" exchange mode
        (operating mode 3 - snapshot) it defines the date/time after
        which the snapshot is no longer considered valid.
    :ivar keep_alive: Indicator that this exchange is due to "keep
        alive" functionality.
    :ivar request_type: The type of request that has been made by the
        client on the supplier.
    :ivar response: The type of the response that the supplier is
        returning to the requesting client.
    :ivar subscription_reference: Unique identifier of the client's
        subscription with the supplier.
    :ivar supplier_identification:
    :ivar target:
    :ivar subscription:
    :ivar filter_reference:
    :ivar catalogue_reference:
    :ivar exchange_extension:
    """
    changed_flag: Optional[ChangedFlagEnum] = field(
        default=None,
        metadata={
            "name": "changedFlag",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    client_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    delivery_break: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deliveryBreak",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    deny_reason: Optional[DenyReasonEnum] = field(
        default=None,
        metadata={
            "name": "denyReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    historical_start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStartDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    historical_stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStopDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    keep_alive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    request_type: Optional[RequestTypeEnum] = field(
        default=None,
        metadata={
            "name": "requestType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    response: Optional[ResponseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subscription_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "subscriptionReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    supplier_identification: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "supplierIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    target: Optional[Target] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subscription: Optional[Subscription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    filter_reference: List[FilterReference] = field(
        default_factory=list,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    catalogue_reference: List[CatalogueReference] = field(
        default_factory=list,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exchange_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "exchangeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class FloatingPointMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in metres in a floating point
    format.

    :ivar floating_point_metre_distance: A value of distance expressed
        in metres in a floating point format.
    :ivar floating_point_metre_distance_value_extension:
    """
    floating_point_metre_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "floatingPointMetreDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    floating_point_metre_distance_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "floatingPointMetreDistanceValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class IntegerMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in whole metres.

    :ivar integer_metre_distance: A value of distance expressed in
        metres in a non negative integer format.
    :ivar integer_metre_distance_value_extension:
    """
    integer_metre_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "integerMetreDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    integer_metre_distance_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "integerMetreDistanceValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ItineraryByReference(Itinerary):
    """
    Multiple (i.e. more than one) physically separate locations which are
    ordered that constitute an itinerary or route where they are defined by
    reference to a predefined itinerary.

    :ivar predefined_itinerary_reference: A reference to a versioned
        instance of a predefined itinerary as specified in a
        PredefinedLocationsPublication.
    :ivar itinerary_by_reference_extension:
    """
    predefined_itinerary_reference: Optional[PredefinedItineraryVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    itinerary_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Junction:
    """
    Junction (on a highway), can also be an interchange or if applicable also a
    motorway service station (see junctionClassification).

    :ivar junction_classification: Explicit type of junction.
    :ivar junction_name: Name of the junction.
    :ivar junction_number: Number of the junction, might also include
        letters (example: 23A).
    :ivar motorway: A detailed identification of the motorway the
        junction belongs to.
    :ivar destination_motorway: In case of any type of intersection, the
        destination motorway(s) can be defined.
    :ivar junction_extension:
    """
    junction_classification: Optional[JunctionClassificationEnum] = field(
        default=None,
        metadata={
            "name": "junctionClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    junction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "junctionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "junctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    motorway: Optional[Road] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    destination_motorway: List[Road] = field(
        default_factory=list,
        metadata={
            "name": "destinationMotorway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "junctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class KilogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in grams per
    unit volume.

    :ivar kilograms_concentration: A value defining the amount of a
        substance in a given volume (concentration) expressed in
        kilograms per cubic metre.
    :ivar kilograms_concentration_value_extension:
    """
    kilograms_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "kilogramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    kilograms_concentration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "kilogramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LinearElementByCode(LinearElement):
    """
    A linear element along a single linear object defined by its identifier or
    code in a road network reference model (specified in LinearElement class)
    which segments the road network according to specific business rules.

    :ivar linear_element_identifier: An identifier or code of a linear
        element (or link) in the road network reference model that is
        specified in the LinearElement class.
    :ivar linear_element_by_code_extension:
    """
    linear_element_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    linear_element_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearElementByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LinearWithinLinearElement:
    """
    A linear section along a linear element where the linear element is either
    a part of or the whole of a linear object (i.e. a road), consistent with
    ISO 19148 definitions.

    :ivar administrative_area_of_linear_section: Identification of the
        road administration area which contains the specified linear
        section.
    :ivar direction_bound_on_linear_section: The direction of traffic
        flow on the linear section in terms of general destination
        direction.
    :ivar direction_relative_on_linear_section: The direction of traffic
        flow on the linear section relative to the direction in which
        the linear element is defined.
    :ivar height_grade_of_linear_section: Identification of whether the
        linear section that is part of the linear element is at, above
        or below the normal elevation of a linear element of that type
        (e.g. road or road section) at that location, typically used to
        indicate "grade" separation.
    :ivar linear_element:
    :ivar from_point: A point on the linear element that defines the
        start node of the linear section.
    :ivar to_point: A point on the linear element that defines the end
        node of the linear section.
    :ivar linear_within_linear_element_extension:
    """
    administrative_area_of_linear_section: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_bound_on_linear_section: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBoundOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_relative_on_linear_section: Optional[LinearReferencingDirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionRelativeOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    height_grade_of_linear_section: Optional[HeightGradeEnum] = field(
        default=None,
        metadata={
            "name": "heightGradeOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_element: Optional[LinearElement] = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "fromPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    to_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "toPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    linear_within_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearWithinLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LocationByReference(Location):
    """
    A location defined by reference to a predefined location.

    :ivar predefined_location_reference: A reference to a versioned
        predefined location.
    :ivar location_by_reference_extension:
    """
    predefined_location_reference: Optional[PredefinedLocationVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasuredValue:
    """
    Contains optional characteristics for the specific measured value (indexed
    to correspond with the defined characteristics of the measurement at the
    referenced measurement site) which override the static characteristics
    defined in the MeasurementSiteTable.

    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar location_characteristics_override:
    :ivar measurement_equipment_fault:
    :ivar basic_data:
    :ivar measured_value_extension:
    """
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_characteristics_override: Optional[LocationCharacteristicsOverride] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_equipment_fault: List[MeasurementEquipmentFault] = field(
        default_factory=list,
        metadata={
            "name": "measurementEquipmentFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    basic_data: Optional[BasicData] = field(
        default=None,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measured_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MicrogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in
    micrograms per unit volume.

    :ivar micrograms_concentration: A value of the amount of a substance
        in a given volume (concentration) expressed in µg/m3
        (microgrammes/cubic metre).
    :ivar micrograms_concentration_value_extension:
    """
    micrograms_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "microgramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    micrograms_concentration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "microgramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NetworkLocation(Location):
    """
    The specification of a location on a network (as a point or a linear
    location).
    """
    supplementary_positional_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonOrderedLocationGroupByList(NonOrderedLocations):
    """
    A group of (i.e. more than one) physically separate locations which have no
    specific order and where each location is explicitly listed.

    :ivar location_contained_in_group: A location contained in a non
        ordered group of locations.
    :ivar non_ordered_location_group_by_list_extension:
    """
    location_contained_in_group: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 2,
        }
    )
    non_ordered_location_group_by_list_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonOrderedLocationGroupByListExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonOrderedLocationGroupByReference(NonOrderedLocations):
    """
    A group of (i.e. more than one) physically separate locations which have no
    specific order that are defined by reference to a predefined non ordered
    location group.

    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar non_ordered_location_group_by_reference_extension:
    """
    predefined_non_ordered_location_group_reference: Optional[PredefinedNonOrderedLocationGroupVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    non_ordered_location_group_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonOrderedLocationGroupByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OccupancyChangeValue(DataValue):
    """
    A measured or calculated value of change of occupied parking spaces
    expressed as integer.

    :ivar occupancy_change: A measured or calculated absolut change of
        occupied parking spaces within a specified time expressed as
        integer.
    :ivar occupancy_change_value_extension:
    """
    occupancy_change: Optional[int] = field(
        default=None,
        metadata={
            "name": "occupancyChange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    occupancy_change_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "occupancyChangeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrCircleLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing a center position and a
    radius.

    :ivar radius: The radius of the geometric area identified.
    :ivar openlr_geo_coordinate:
    :ivar openlr_circle_location_reference_extension:
    """
    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_geo_coordinate: Optional[OpenlrGeoCoordinate] = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_circle_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrCircleLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrGridLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing repeating rectangles.
    """
    openlr_rectangle: Optional[OpenlrRectangle] = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_grid_attributes: Optional[OpenlrGridAttributes] = field(
        default=None,
        metadata={
            "name": "openlrGridAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_grid_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrGridLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrLastLocationReferencePoint(OpenlrBaseLocationReferencePoint):
    """
    The sequence of location reference points is terminated by a last location
    reference point.
    """
    openlr_last_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrLocationReferencePoint(OpenlrBaseLocationReferencePoint):
    """
    The basis of a location reference is a sequence of location reference
    points (LRPs).
    """
    openlr_path_attributes: Optional[OpenlrPathAttributes] = field(
        default=None,
        metadata={
            "name": "openlrPathAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrPolygonLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing points that bound the
    area.
    """
    openlr_polygon_corners: Optional[OpenlrPolygonCorners] = field(
        default=None,
        metadata={
            "name": "openlrPolygonCorners",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_polygon_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPolygonLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrRectangleLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing a rectangular shape
    defined by two geo-coordinate pairs.
    """
    openlr_rectangle: Optional[OpenlrRectangle] = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_rectangle_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrRectangleLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRoute:
    """
    A parking route, defined by ParkingRouteDetails or by a reference.

    :ivar parking_route_colour: A colour assigned to a parking route for
        visualisation purpose.
    :ivar parking_route_extension:
    """
    parking_route_colour: Optional[RGBColour] = field(
        default=None,
        metadata={
            "name": "parkingRouteColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRouteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingStatusColourMapping:
    """
    Defines a pair of 'parkingSiteStatus' and a corresponding colour.

    :ivar parking_site_status: The status of the parking site (spaces
        available or not).
    :ivar rgb_colour:
    :ivar parking_status_colour_mapping_extension:
    """
    parking_site_status: Optional[ParkingSiteStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    rgb_colour: Optional[RGBColour] = field(
        default=None,
        metadata={
            "name": "rgbColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_status_colour_mapping_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingStatusColourMappingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PcuFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of passenger car units.

    :ivar pcu_flow_rate: A value of passenger car unit flow rate
        expressed in passenger car units per hour.
    :ivar pcu_flow_value_extension:
    """
    pcu_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "pcuFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pcu_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pcuFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PercentageValue(DataValue):
    """
    A measured or calculated value expressed as a percentage.

    :ivar percentage: A value expressed as a percentage.
    :ivar percentage_value_extension:
    """
    percentage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    percentage_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "percentageValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PointAlongLinearElement:
    """
    A point on a linear element where the linear element is either a part of or
    the whole of a linear object (i.e. a road), consistent with ISO 19148
    definitions.

    :ivar administrative_area_of_point: Identification of the road
        administration area which contains the specified point.
    :ivar direction_bound_at_point: The direction of traffic flow at the
        specified point in terms of general destination direction.
    :ivar direction_relative_at_point: The direction of traffic flow at
        the specified point relative to the direction in which the
        linear element is defined.
    :ivar height_grade_of_point: Identification of whether the point on
        the linear element is at, above or below the normal elevation of
        a linear element of that type (e.g. road or road section) at
        that location, typically used to indicate "grade" separation.
    :ivar linear_element:
    :ivar distance_along_linear_element:
    :ivar point_along_linear_element_extension:
    """
    administrative_area_of_point: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_bound_at_point: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBoundAtPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_relative_at_point: Optional[LinearReferencingDirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionRelativeAtPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    height_grade_of_point: Optional[HeightGradeEnum] = field(
        default=None,
        metadata={
            "name": "heightGradeOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_element: Optional[LinearElement] = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    distance_along_linear_element: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "distanceAlongLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    point_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PolygonArea:
    """
    defines points for a closed polygon-shape describing the area.

    :ivar section_name: Name of the polygon area. Especially useful when
        the area consists of more than one polygon.
    :ivar point_coordinates:
    :ivar polygon_area_extension:
    """
    section_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sectionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_coordinates: List[PolygonAreaIndexPointCoordinates] = field(
        default_factory=list,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    polygon_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "polygonAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PrecipitationIntensityValue(DataValue):
    """
    A measured or calculated value of the accumulation rate of precipitation.

    :ivar millimetres_per_hour_intensity: A value of precipitation
        intensity expressed in units of millimetres per hour.
    :ivar precipitation_intensity_value_extension:
    """
    millimetres_per_hour_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "millimetresPerHourIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    precipitation_intensity_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationIntensityValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PredefinedLocation(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a single predefined location.

    :ivar predefined_location_name: A name assigned to the predefined
        location (e.g. extracted out of the network operator's
        gazetteer).
    :ivar location:
    :ivar predefined_location_extension:
    :ivar id:
    :ivar version:
    """
    predefined_location_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    predefined_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class PredefinedLocationsPublication(PayloadPublication):
    """
    A publication containing one or more groups of predefined locations
    organised either as litineraries, non ordered groups or as individual
    locations.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    predefined_location_container: List[PredefinedLocationContainer] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationContainer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    predefined_locations_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class RoadNode(Road):
    """
    A road node as part of the specialised road identified by the name of a
    junctionon on this road.

    :ivar junction_name: Name of the junction.
    :ivar road_node_extension:
    """
    junction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "junctionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    road_node_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadNodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SpecialDay:
    """Specification of a special day, for example schoolDay, electionDay, ...

    Gives also the possibility to define a public holiday (country
    specific).

    :ivar intersect_with_applicable_days: When true, the period is the
        intersection of applicable days and this special day. When
        false, the period is the union of applicable days and this
        special day.”
    :ivar special_day_type: Specification of a special day, for example
        schoolDay, electionDay, ..  .
    :ivar special_day_name: Specification of a special day, if the
        enumeration values do not fit.
    :ivar public_holiday:
    :ivar special_day_extension:
    """
    intersect_with_applicable_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "intersectWithApplicableDays",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_type: Optional[SpecialDayTypeEnum] = field(
        default=None,
        metadata={
            "name": "specialDayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "specialDayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    public_holiday: List[PublicHoliday] = field(
        default_factory=list,
        metadata={
            "name": "publicHoliday",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    special_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "specialDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SpeedValue(DataValue):
    """
    A measured or calculated value of speed.

    :ivar speed: A value of speed expressed in kilometres per hour.
    :ivar speed_value_extension:
    """
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TemperatureValue(DataValue):
    """
    A measured or calculated value of temperature.

    :ivar temperature: A value of temperature expressed in degrees
        Celsius.
    :ivar temperature_value_extension:
    """
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    temperature_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegAreaDescriptor(TpegDescriptor):
    """
    A descriptor for describing an area location.

    :ivar tpeg_area_descriptor_type: The nature of the descriptor used
        to define the location under consideration (derived from the
        TPEG Loc table 03).
    :ivar tpeg_area_descriptor_extension:
    """
    tpeg_area_descriptor_type: Optional[TpegLoc03AreaDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_area_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegPointDescriptor(TpegDescriptor):
    """
    A descriptor for describing a point location.
    """
    tpeg_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficStatusValue(DataValue):
    """
    A measured or calculated value of the status of traffic conditions on a
    section of road in a specified direction.

    :ivar traffic_status_value: A status value of traffic conditions on
        the identified section of road in the specified direction.
    :ivar traffic_status_value_extension:
    """
    traffic_status_value: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatusValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_status_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficStatusValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleCharacteristics:
    """
    The characteristics of a vehicle, e.g. lorry of gross weight greater than
    30 tonnes.

    :ivar fuel_type: The type of fuel used by the vehicle.
    :ivar load_type: The type of load carried by the vehicle, especially
        in respect of hazardous loads.
    :ivar vehicle_equipment: The type of equipment in use or on board
        the vehicle.
    :ivar vehicle_type: Vehicle type.
    :ivar vehicle_usage: The type of usage of the vehicle (i.e. for what
        purpose is the vehicle being used).
    :ivar gross_weight_characteristic:
    :ivar height_characteristic:
    :ivar length_characteristic:
    :ivar width_characteristic:
    :ivar heaviest_axle_weight_characteristic:
    :ivar number_of_axles_characteristic:
    :ivar vehicle_characteristics_extension:
    """
    fuel_type: Optional[FuelTypeEnum] = field(
        default=None,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    load_type: Optional[LoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "loadType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_equipment: Optional[VehicleEquipmentEnum] = field(
        default=None,
        metadata={
            "name": "vehicleEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_usage: Optional[VehicleUsageEnum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    gross_weight_characteristic: List[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    height_characteristic: List[HeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    length_characteristic: List[LengthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "lengthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    width_characteristic: List[WidthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "widthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    heaviest_axle_weight_characteristic: List[HeaviestAxleWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heaviestAxleWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    number_of_axles_characteristic: List[NumberOfAxlesCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "numberOfAxlesCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    vehicle_characteristics_extension: Optional[VehicleCharacteristicsExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleCountValue(DataValue):
    """
    A measured or calculated value of absolute count of vehicles within a
    specified period of time expressed as non negative integer.

    :ivar vehicle_count: A measured or calculated absolute count of
        vehicles within a specified period of time expressed as non
        negative integer.
    :ivar vehicle_count_value_extension:
    """
    vehicle_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleCount",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_count_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCountValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicles.

    :ivar vehicle_flow_rate: A value of vehicle flow rate expressed in
        vehicles per hour.
    :ivar vehicle_flow_value_extension:
    """
    vehicle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsManagedLogicalLocation:
    """
    The logical location (e.g. a car park, a section of road, a junction etc.)
    which a VMS contributes to the management of.

    :ivar managed_logical_location: Identification of the logical
        location (e.g. a car park, a section of road , a junction etc.)
        which this sign contributes to the management of.
    :ivar distance_from_logical_location: Distance in metres of the VMS
        from the logical location which this sign contributes to the
        management of.
    :ivar managed_location: The location which is managed by the
        variable message sign, such as the location of a junction or a
        car park.
    :ivar vms_managed_logical_location_extension:
    """
    managed_logical_location: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "managedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_logical_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    managed_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "managedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_managed_logical_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsManagedLogicalLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsSupplementaryPanel:
    """
    A panel which may display information or a regulatory instruction which is
    supplemental to the associated pictogram, comprising either an additional
    line of text or a pictogram or both.

    :ivar supplementary_message_description: Free text description of
        the message that is displayed in the panel which is supplemental
        to the main pictogram display.
    :ivar vms_supplementary_pictogram:
    :ivar vms_supplementary_text: One line of text displayed in the
        panel which is supplemental to the pictogram display.
    :ivar vms_supplementary_panel_extension:
    """
    supplementary_message_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "supplementaryMessageDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_pictogram: Optional[VmsSupplementaryPictogram] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_text: Optional[VmsTextLine] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_panel_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsText:
    """A page of text (comprising one or more ordered lines) that are displayed
    simultaneously on the VMS.

    Where more than one page is defined these are sequentially displayed
    according to their "pageNumber".

    :ivar vms_legend_code: The code of the legend/text from the legend
        code list referenced in the VmsTextDisplayCharacteristics.
    :ivar vms_text_image_url: Reference to a URL from where an image of
        the displayed legend text can be be obtained.
    :ivar vms_text_line:
    :ivar vms_text_extension:
    """
    vms_legend_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsLegendCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_text_image_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextImageUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line: List[VmsTextLineIndexVmsTextLine] = field(
        default_factory=list,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTextExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class WeatherData(BasicData):
    """
    Measured or derived values relating to the weather at a specific location
    or locations.
    """
    weather_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class IntermediatePointOnLinearElement:
    class Meta:
        name = "_IntermediatePointOnLinearElement"

    referent: Optional[Referent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LocationContainedInItinerary:
    class Meta:
        name = "_LocationContainedInItinerary"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics:
    class Meta:
        name = "_VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics"

    vms_pictogram_display_characteristics: Optional[VmsPictogramDisplayCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics:
    class Meta:
        name = "_VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics"

    vms_pictogram_display_characteristics: Optional[VmsPictogramDisplayCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlertCMethod2Linear(AlertCLinear):
    """A linear section along a road between two points, Primary and Secondary,
    which are pre-defined in an ALERT-C location table.

    Direction is FROM the Secondary point TO the Primary point, i.e. the
    Primary point is downstream of the Secondary point.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: Optional[AlertCMethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_secondary_point_location: Optional[AlertCMethod2SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod2Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table and which has an associated direction of
    traffic flow.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: Optional[AlertCMethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod4Linear(AlertCLinear):
    """A linear section along a road between two points, Primary and Secondary,
    which are pre-defined ALERT-C locations plus offset distance.

    Direction is FROM the Secondary point TO the Primary point, i.e. the
    Primary point is downstream of the Secondary point.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCMethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location: Optional[AlertCMethod4SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AlertCMethod4Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table plus an offset distance and which has an
    associated direction of traffic flow.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCMethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AreaExtended:
    """
    Extension class for area used in parking publication extension.
    """
    named_area: Optional[NamedArea] = field(
        default=None,
        metadata={
            "name": "namedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    polygon_area: List[PolygonArea] = field(
        default_factory=list,
        metadata={
            "name": "polygonArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class D2LogicalModel1:
    """
    The DATEX II logical model comprising exchange, content payload and
    management sub-models.
    """
    class Meta:
        name = "D2LogicalModel"

    exchange: Optional[Exchange] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    payload_publication: Optional[PayloadPublication] = field(
        default=None,
        metadata={
            "name": "payloadPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    d2_logical_model_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "d2LogicalModelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    model_base_version: str = field(
        init=False,
        default="2",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GroupOfVehiclesInvolved:
    """
    Group of the vehicles involved having common characteristics and/or status.

    :ivar number_of_vehicles: The number of vehicles of this group that
        are involved.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar group_of_vehicles_involved_extension:
    """
    number_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_vehicles_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfVehiclesInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Humidity:
    """
    Details of atmospheric humidity.

    :ivar relative_humidity: The amount of water vapour in the air, as a
        percentage of the amount of water vapour in saturated air at the
        same temperature and at atmospheric pressure. The measurement is
        taken between 1.5 and 2 m above the ground and behind a
        meteorological screen.
    :ivar humidity_extension:
    """
    relative_humidity: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "relativeHumidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    humidity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ItineraryByIndexedLocations(Itinerary):
    """Multiple physically separate locations arranged as an ordered set that
    defines an itinerary or route.

    The index qualifier indicates the order.

    :ivar location_contained_in_itinerary: A location contained in an
        itinerary (i.e. an ordered set of locations defining a route or
        itinerary).
    :ivar itinerary_by_indexed_locations_extension:
    """
    location_contained_in_itinerary: List[LocationContainedInItinerary] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInItinerary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    itinerary_by_indexed_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryByIndexedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LinearElementByPoints(LinearElement):
    """
    A linear element along a single linear object defined by its start and end
    points.

    :ivar start_point_of_linear_element: The referent at a known
        location on the linear object which defines the start of the
        linear element.
    :ivar intermediate_point_on_linear_element: A referent at a known
        location on the linear object which is neither the start or end
        of the linear element.
    :ivar end_point_of_linear_element: The referent at a known location
        on the linear object which defines the end of the linear
        element.
    :ivar linear_element_by_points_extension:
    """
    start_point_of_linear_element: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "startPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    intermediate_point_on_linear_element: List[IntermediatePointOnLinearElement] = field(
        default_factory=list,
        metadata={
            "name": "intermediatePointOnLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    end_point_of_linear_element: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "endPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    linear_element_by_points_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearElementByPointsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasurementSpecificCharacteristics:
    """
    Characteristics which are specific to an individual measurement type
    (specified in a known order) at the given measurement site.

    :ivar accuracy: The extent to which the value is expected to be free
        from error, measured as a percentage of the data value. 100%
        means fully accurate.
    :ivar period: The time elapsed between the beginning and the end of
        the sampling or measurement period. This item may differ from
        the unit attribute; e.g. an hourly flow can be estimated from a
        5-minute measurement period.
    :ivar smoothing_factor: Coefficient required when a moving average
        is computed to give specific weights to the former average and
        the new data. A typical formula is, F being the smoothing
        factor: New average = (old average) F + (new data) (1 - F).
    :ivar specific_lane: The lane to which the specific measurement at
        the measurement site relates. This overrides any lane specified
        for the measurement site as a whole.
    :ivar specific_measurement_value_type: The type of this specific
        measurement at the measurement site.
    :ivar specific_vehicle_characteristics:
    :ivar measurement_specific_characteristics_extension:
    """
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    specific_lane: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "specificLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    specific_measurement_value_type: Optional[MeasuredOrDerivedDataTypeEnum] = field(
        default=None,
        metadata={
            "name": "specificMeasurementValueType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "specificVehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_specific_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrBasePointLocation:
    """
    Holds common data that are used both in OpenlrPointAccessPoint and
    OpenlrPointAlongLine.

    :ivar openlr_side_of_road: Side of road
    :ivar openlr_orientation: Orientation
    :ivar openlr_positive_offset: The positive offset along the line of
        the location.
    :ivar openlr_location_reference_point:
    :ivar openlr_last_location_reference_point:
    :ivar openlr_base_point_location_extension:
    """
    openlr_side_of_road: Optional[OpenlrSideOfRoadEnum] = field(
        default=None,
        metadata={
            "name": "openlrSideOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_orientation: Optional[OpenlrOrientationEnum] = field(
        default=None,
        metadata={
            "name": "openlrOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_location_reference_point: Optional[OpenlrLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_last_location_reference_point: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_base_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrBasePointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrClosedLineLocationReference(OpenlrAreaLocationReference):
    """the openLR method of areadefinition by providing a closed path (i.e. a
    circuit) in the road network.

    The boundary always consists of road segments
    """
    openlr_location_reference_point: List[OpenlrLocationReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    openlr_last_line: Optional[OpenlrLineAttributes] = field(
        default=None,
        metadata={
            "name": "openlrLastLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_closed_line_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrClosedLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrLineLocationReference:
    """
    A LineLocationReference is defined by an ordered sequence of location
    reference points and a terminating last location reference point.
    """
    openlr_location_reference_point: List[OpenlrLocationReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    openlr_last_location_reference_point: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_offsets: Optional[OpenlrOffsets] = field(
        default=None,
        metadata={
            "name": "openlrOffsets",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_line_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingAssignment:
    """One set of prohibited/only allowed/convenient assignment for parking
    space(s), parking site(s) or an access.

    Same kind of data forms a union (e.g. lorries OR buses), different
    kind of data forms an intersection (e.g. residents AND long-term).

    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar parking_duration: Temporal parking classification for this
        assignment (long term, short term, ...). Depending on the used
        role, these classifications are either assigned or prohibited.
    :ivar vehicle_characteristics:
    :ivar hazardous_materials: Hazardous Material which is prohibited to
        park there.
    :ivar time_period_by_hour: Used for example for mixed parking areas.
        If at least one restrictedValidity is given, spaces are not
        available outside the union of all given time ranges. EndTime
        might be a lower value than start time, whem validity contains
        midnight.
    :ivar parking_permit:
    :ivar parking_assignment_extension:
    """
    applicable_for_user: List[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_duration: List[ParkingDurationEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_characteristics: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    hazardous_materials: List[HazardousMaterials] = field(
        default_factory=list,
        metadata={
            "name": "hazardousMaterials",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_period_by_hour: List[TimePeriodByHour] = field(
        default_factory=list,
        metadata={
            "name": "timePeriodByHour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_permit: List[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_assignment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingAssignmentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRouteByReference(ParkingRoute):
    """
    A route defined by a reference to an earlier specified route.

    :ivar parking_route_reference: A reference to a parking route.
    :ivar parking_route_by_reference_extension:
    """
    parking_route_reference: Optional[ParkingRouteDetailsVersionedReference] = field(
        default=None,
        metadata={
            "name": "parkingRouteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_route_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRouteByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRouteDetails(ParkingRoute):
    """Urban context: Defining parking routes leading to the parking site.

    Truck parking context: Can be used to define a dynamic route
    management.

    :ivar parking_route_name: Name of the parking route.
    :ivar parking_route_type: The type of parking route. If not
        specified, the route is designed for any type of vehicles.
    :ivar dynamic_route_management: Indicates that there is dynamic
        route management for truck parking, i.e. a management system
        concerning several truck parkings (including this one) along a
        route.
    :ivar parking_route_icon_index: An index, which can identify some
        icon for visualisation of the route. Note that form and usage of
        this index as well as the icons itself are not further
        determined here.
    :ivar parking_route_direction: The direction of traffic, for which
        the parking route can be used. If not specified, the route can
        be used in the order of the given locations.
    :ivar parking_route_direction2: Additional directions of traffic,
        for which the parking route can be used. If not specified, the
        route can be used in the order of the given locations.
    :ivar group_of_locations:
    :ivar parking_route_details_extension:
    :ivar id:
    :ivar version:
    """
    parking_route_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingRouteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_type: Optional[ParkingRouteTypeEnum] = field(
        default=None,
        metadata={
            "name": "parkingRouteType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dynamic_route_management: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dynamicRouteManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_icon_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingRouteIconIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    parking_route_direction: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "parkingRouteDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_direction2: Optional[ParkingRouteDirectionEnum] = field(
        default=None,
        metadata={
            "name": "parkingRouteDirection2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_details_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRouteDetailsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class ParkingThresholds:
    """Configuration parameters of the parking site, used among others for the
    dynamic attribute 'parkingStatus'.

    This component or all elements of it can be overridden in the
    dynamic model.

    :ivar almost_full_decreasing: The number of available spaces above
        which the state of the parking site is considered to change from
        'almost full' to 'spaces available' as the parking site's
        occupancy decreases. Must be greater than 'almostFullIncreasing'
        value.
    :ivar almost_full_increasing: The number of available spaces below
        which the state of the site is considered to change from 'spaces
        available' to 'almost full' as the site's occupancy increases.
        Must be lower or equal to 'almostFullDecreasing' and greater
        'fullDecreasing'.
    :ivar entrance_full: The number of available spaces below which the
        parking site is considered to be 'full' at its entrance (e.g.
        full sign is displayed at entrance or on managing VMS).
    :ivar full_decreasing: The number of available spaces above which
        the state of the parking site is considered to change from
        'full' to 'almost full' as the site's occupancy decreases. Must
        be greater or equal to 'fullIncreasing' value and lower than
        'almostFullIncreasing'.
    :ivar full_increasing: The number of available spaces below which
        the state of the parking site is considered to change from
        'almost full' to 'full' as the site's occupancy increases. Must
        be lower than or equal to 'fullDecreasing' value.
    :ivar overcrowding: The number of vehicles on the parking above
        which the overcrowding state of the parking site is considered
        to change to 'overcrowding'.  Can be used as an alternative to
        the overcrowding level attributes.
    :ivar overcrowding_level1: The number of vehicles on the parking
        site above which the overcrowding state of the parking site is
        considered to change from 'noOvercrowding' to
        'overcrowdingLevel1'. Must be lower than the
        'overcrowdingLevel2' value.
    :ivar overcrowding_level2: The number of vehicles on the parking
        site above which the overcrowding state of the parking site is
        considered to change from 'overcrowdingLevel1' to
        'overcrowdingLevel2'. Must be greater than the
        'overcrowdingLevel1' value.
    :ivar parking_last_maximum_occupancy: The last known occupancy
        (number of parking vehicles on the site) under safe conditions.
    :ivar parking_status_colour_mapping:
    :ivar parking_thresholds_extension:
    """
    almost_full_decreasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "almostFullDecreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    almost_full_increasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "almostFullIncreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    entrance_full: Optional[int] = field(
        default=None,
        metadata={
            "name": "entranceFull",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    full_decreasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "fullDecreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    full_increasing: Optional[int] = field(
        default=None,
        metadata={
            "name": "fullIncreasing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding_level1: Optional[int] = field(
        default=None,
        metadata={
            "name": "overcrowdingLevel1",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overcrowding_level2: Optional[int] = field(
        default=None,
        metadata={
            "name": "overcrowdingLevel2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_last_maximum_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingLastMaximumOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_colour_mapping: List[ParkingStatusColourMapping] = field(
        default_factory=list,
        metadata={
            "name": "parkingStatusColourMapping",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_thresholds_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingThresholdsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PeriodExtended:
    """
    An extension point for Period offering the possibility to describe special
    days and public holidays.

    :ivar recurring_special_day: A recurring period in terms of special
        days.
    """
    recurring_special_day: List[SpecialDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringSpecialDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PointExtended:
    """
    Extension point for 'Point' to support the description of junctions (and
    other alternative point descriptions).

    :ivar description: Textual description for a point location
    :ivar junction:
    """
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    junction: Optional[Junction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Pollution:
    """
    Details of atmospheric pollution.

    :ivar pollutant_type: The type of pollutant in the air.
    :ivar pollutant_concentration: The average concentration of the
        pollutant in the air.
    :ivar pollution_extension:
    """
    pollutant_type: Optional[PollutantTypeEnum] = field(
        default=None,
        metadata={
            "name": "pollutantType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pollutant_concentration: Optional[MicrogramsConcentrationValue] = field(
        default=None,
        metadata={
            "name": "pollutantConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pollution_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PrecipitationDetail:
    """
    Details of precipitation (rain, snow etc.).

    :ivar precipitation_type: The type of precipitation which is
        affecting the driving conditions.
    :ivar precipitation_intensity: The height of the precipitation
        received per unit time.
    :ivar deposition_depth: The equivalent depth of the water layer
        resulting from precipitation or deposition on a non-porous
        horizontal surface. Non liquid precipitation is considered as
        melted in water form.
    :ivar precipitation_detail_extension:
    """
    precipitation_type: Optional[PrecipitationTypeEnum] = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    precipitation_intensity: Optional[PrecipitationIntensityValue] = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    deposition_depth: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "depositionDepth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    precipitation_detail_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationDetailExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PredefinedNonOrderedLocationGroup(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a predefined group of non ordered
    locations (i.e. more than one).

    :ivar predefined_non_ordered_location_group_name: A name assigned to
        the predefined group of non ordered locations.
    :ivar predefined_location:
    :ivar predefined_non_ordered_location_group_extension:
    :ivar id:
    :ivar version:
    """
    predefined_non_ordered_location_group_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    predefined_location: List[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 2,
        }
    )
    predefined_non_ordered_location_group_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class RoadSurfaceConditionMeasurements:
    """
    Measurements of the road surface condition which relate specifically to the
    weather.

    :ivar road_surface_temperature: The temperature measured on the road
        surface.
    :ivar protection_temperature: The road surface temperature down to
        which the surface is protected from freezing.
    :ivar de_icing_application_rate: Indicates the rate at which de-
        icing agents have been applied to the specified road.
    :ivar de_icing_concentration: Indicates the concentration of de-
        icing agent present in surface water on the specified road.
    :ivar depth_of_snow: The depth of snow recorded on the road surface.
    :ivar water_film_thickness: The depth of standing water to be found
        on the road surface.
    :ivar road_surface_condition_measurements_extension:
    """
    road_surface_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "roadSurfaceTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    protection_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "protectionTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    de_icing_application_rate: Optional[ApplicationRateValue] = field(
        default=None,
        metadata={
            "name": "deIcingApplicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    de_icing_concentration: Optional[KilogramsConcentrationValue] = field(
        default=None,
        metadata={
            "name": "deIcingConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    depth_of_snow: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "depthOfSnow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    water_film_thickness: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "waterFilmThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_surface_condition_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SpeedPercentile:
    """
    Details of percentage (from an observation set) of vehicles whose speeds
    fall below a stated value.

    :ivar vehicle_percentage: The percentage of vehicles from the
        observation set whose speeds fall below the stated speed
        (speedPercentile).
    :ivar speed_percentile: The speed below which the associated
        percentage of vehicles in the measurement set are travelling at.
    :ivar speed_percentile_extension:
    """
    vehicle_percentage: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "vehiclePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_percentile: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_percentile_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedPercentileExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Temperature:
    """
    Details of atmospheric temperature.

    :ivar air_temperature: The air temperature measured in the shade
        between 1.5 and 2 metres above ground level.
    :ivar dew_point_temperature: The temperature to which the air would
        have to cool (at constant pressure and water vapour content) in
        order to reach saturation.
    :ivar maximum_temperature: The maximum temperature during the
        forecast or measurement period.
    :ivar minimum_temperature: The minimum temperature during the
        forecast or measurement period.
    :ivar temperature_extension:
    """
    air_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "airTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dew_point_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "dewPointTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "maximumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    minimum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "minimumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    temperature_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegGeometricArea(TpegAreaLocation):
    """
    A geometric area defined by a centre point and a radius.

    :ivar radius: The radius of the geometric area identified.
    :ivar centre_point: Centre point of a circular geometric area.
    :ivar name: Name of area.
    :ivar tpeg_geometric_area_extension:
    """
    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    centre_point: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    name: Optional[TpegAreaDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tpeg_geometric_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegIlcPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a junction by defining the intersecting roads.

    :ivar tpeg_ilc_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_ilc_point_descriptor_extension:
    """
    tpeg_ilc_point_descriptor_type: Optional[TpegLoc03IlcPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_ilc_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a point at a junction on a road network.

    :ivar tpeg_junction_point_descriptor_type: The nature of the
        descriptor used to define the location under consideration
        (derived from the TPEG Loc table 03).
    :ivar tpeg_junction_point_descriptor_extension:
    """
    tpeg_junction_point_descriptor_type: Optional[TpegLoc03JunctionPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegNamedOnlyArea(TpegAreaLocation):
    """
    An area defined by a well-known name.

    :ivar name: Name of area.
    :ivar tpeg_named_only_area_extension:
    """
    name: List[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    tpeg_named_only_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegOtherPointDescriptor(TpegPointDescriptor):
    """
    General descriptor for describing a point.

    :ivar tpeg_other_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_other_point_descriptor_extension:
    """
    tpeg_other_point_descriptor_type: Optional[TpegLoc03OtherPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_other_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficData(BasicData):
    """
    Measured or derived values relating to traffic or individual vehicle
    movements on a specific section or at a specific point on the road network.

    :ivar for_vehicles_with_characteristics_of: Used to define the
        vehicle characteristics to which the TrafficValue is applicable
        primarily in Elaborated Data Publications, but may also be used
        in Measured Data Publications to override vehicle
        characteristics defined for the measurement site.
    :ivar traffic_data_extension:
    """
    for_vehicles_with_characteristics_of: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficStatus(BasicData):
    """
    The status of traffic conditions on a specific section or at a specific
    point on the road network.

    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar traffic_status: Status of traffic conditions on the identified
        section of road in the specified direction.
    :ivar traffic_status_extension:
    """
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_status: Optional[TrafficStatusValue] = field(
        default=None,
        metadata={
            "name": "trafficStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TravelTimeData(BasicData):
    """Derived/computed travel time information relating to a linear section of the road network; forecast = true means a forecast for a vehicle at the start of the specified location, forecast = false means calculation/measurement at the end.

    :ivar travel_time_trend_type: The current trend in the travel time
        between the defined locations in the specified direction.
    :ivar travel_time_type: Indication of the way in which the travel
        time is derived.
    :ivar vehicle_type: Vehicle type.
    :ivar travel_time: Derived/computed travel time information relating
        to a specific group of locations.
    :ivar free_flow_travel_time: The travel time which would be expected
        under ideal free flow conditions.
    :ivar normally_expected_travel_time: The travel time which is
        expected for the given period (e.g. date/time, holiday status
        etc.) and any known quasi-static conditions (e.g. long term
        roadworks). This value is derived from historical analysis.
    :ivar free_flow_speed: The free flow speed expected under ideal
        conditions, corresponding to the freeFlowTravelTime.
    :ivar travel_time_data_extension:
    """
    travel_time_trend_type: Optional[TravelTimeTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    travel_time_type: Optional[TravelTimeTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "travelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    free_flow_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "freeFlowTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    normally_expected_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "normallyExpectedTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    free_flow_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "freeFlowSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    travel_time_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "travelTimeDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Vehicle:
    """
    Details of an individual vehicle.

    :ivar vehicle_colour: The colour of the vehicle.
    :ivar vehicle_country_of_origin: Specification of the country in
        which the vehicle is registered.  The code is the 2-alpha code
        as given in EN ISO 3166-1 which is updated by the ISO 3166
        Maintenance Agency.
    :ivar vehicle_identifier: A vehicle identification number (VIN)
        comprising 17 characters that is based on either ISO 3779 or ISO
        3780  and uniquely identifies the individual vehicle. This is
        normally securely attached to the vehicle chassis.
    :ivar vehicle_manufacturer: Indicates the stated manufacturer of the
        vehicle i.e. Ford.
    :ivar vehicle_model: Indicates the model (or range name) of the
        vehicle i.e. Mondeo.
    :ivar vehicle_registration_plate_identifier: An identifier or code
        displayed on a vehicle registration plate attached to the
        vehicle used for official identification purposes. The
        registration identifier is numeric or alphanumeric and is unique
        within the issuing authority's region.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar axle_spacing_on_vehicle: The spacing between axles on the
        vehicles.
    :ivar specific_axle_weight: The weight details relating to a
        specific axle on the vehicle.
    :ivar hazardous_goods_associated_with_vehicle: Details of hazardous
        goods carried by the vehicle.
    :ivar vehicle_extension:
    """
    vehicle_colour: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_country_of_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleCountryOfOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vehicle_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleManufacturer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vehicle_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vehicle_registration_plate_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleRegistrationPlateIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    axle_spacing_on_vehicle: List[AxleSpacing] = field(
        default_factory=list,
        metadata={
            "name": "axleSpacingOnVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    specific_axle_weight: List[AxleWeight] = field(
        default_factory=list,
        metadata={
            "name": "specificAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    hazardous_goods_associated_with_vehicle: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "hazardousGoodsAssociatedWithVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleCountWithinInterval:
    """Gives incoming and/or outgoing vehicles and/or change of occupied spaces
    within a given interval.

    The interval is given in positive or negative seconds related to
    'measurementOrCalculationTime' or 'measurementDefaultTime'.

    :ivar measurement_or_calcualtion_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar measurement_interval: Interval for which the data applies.
        Usually, this value should be negative. Example: - 300 = last 5
        minutes up to 'measurementOrCalculationTime' or
        'measurementTimeDefault'. Use a positive value only for
        predictions. Example: 600 = next ten minutes.
    :ivar number_of_incoming_vehicles: Number of vehicles of specified
        type that entered the specified parking within the given
        interval.
    :ivar number_of_outgoing_vehicles: Number of vehicles of specified
        type that left the specified parking within the given interval.
    :ivar change_of_occupied_spaces: The change in the number of
        occupied spaces for specified vehicles within the given
        interval. Negative values mean less occupied spaces than at the
        beginning of the interval.
    :ivar counted_vehicles:
    :ivar vehicle_count_within_interval_extension:
    """
    measurement_or_calcualtion_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementOrCalcualtionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "measurementInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_incoming_vehicles: Optional[VehicleCountValue] = field(
        default=None,
        metadata={
            "name": "numberOfIncomingVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_outgoing_vehicles: Optional[VehicleCountValue] = field(
        default=None,
        metadata={
            "name": "numberOfOutgoingVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    change_of_occupied_spaces: Optional[OccupancyChangeValue] = field(
        default=None,
        metadata={
            "name": "changeOfOccupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    counted_vehicles: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "countedVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_count_within_interval_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCountWithinIntervalExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleRate:
    """Gives information about fill and exit rates OR vehicle flow rate
    (without direction).

    If the time stamp is omitted, 'measurementTimeDefault' is used.

    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar fill_rate: The rate at which vehicles are entering the
        parking.
    :ivar exit_rate: The rate at which vehicles are exiting the parking.
    :ivar vehicle_flow_rate: A value of vehicle flow rate expressed in
        vehicles per hour.
    :ivar measured_vehicles:
    :ivar vehicle_rate_extension:
    """
    measurement_or_calculation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    fill_rate: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exit_rate: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_flow_rate: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measured_vehicles: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "measuredVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_rate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleRateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Visibility:
    """
    Details of atmospheric visibility.

    :ivar minimum_visibility_distance: The minimum distance, measured or
        estimated, beyond which drivers may be unable to clearly see a
        vehicle or an obstacle.
    :ivar visibility_extension:
    """
    minimum_visibility_distance: Optional[IntegerMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "minimumVisibilityDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    visibility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsDynamicCharacteristics:
    """
    Provides the current characteristic settings for the VMS which can be
    dynamically configured and therefore which override any corresponding
    characteristics set for the VMS in the relevant VmsUnitPublication.

    :ivar number_of_pictogram_display_areas: Number of pictogram display
        areas which the VMS contains.
    :ivar vms_text_display_characteristics:
    :ivar vms_pictogram_display_characteristics:
    :ivar vms_dynamic_characteristics_extension:
    """
    number_of_pictogram_display_areas: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPictogramDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_display_characteristics: Optional[VmsTextDisplayCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsTextDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_characteristics: List[VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_dynamic_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsDynamicCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsPictogram:
    """A main pictogram displayable on the VMS panel.

    Note a main pictogram may have an associated supplementary panel
    which may itself contain a further pictogram and line of text.

    :ivar pictogram_description: Description of the (main) displayed
        pictogram.
    :ivar pictogram_code: The code of the pictogram from the pictogram
        code list referenced in the VmsPictogramDisplayCharacteristics
        for the VMS that is identified in the relevant VMS Unit table.
    :ivar pictogram_url: Reference to a URL from where an image of the
        displayed pictogram can be be obtained.
    :ivar additional_pictogram_description: Additional description of
        the pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar pictogram_in_inverse_colour: The pictogram is displayed in
        inverse colour (i.e. the colours are the inverse of normal).
    :ivar presence_of_red_triangle: Indication of the presence of a red
        triangle around the pictogram, often used to indicate imminence,
        typically within 2km, of signed danger.
    :ivar vienna_convention_compliant: Indicates that the displayed
        pictogram conforms with the Vienna Convention defined pictogram
        list as modified by "UNECE Consolidated Resolution on Road Signs
        and Signals".
    :ivar distance_attribute: Value of distance that is displayable as
        part of the pictogram (e.g. for keep minimum safe distance).
    :ivar height_attribute: Value of height that is displayable as part
        of the pictogram (e.g. for a vehicle height restriction).
    :ivar length_attribute: Value of length that is displayable as part
        of the pictogram (e.g. for a vehicle length restriction).
    :ivar speed_attribute: Value of speed that is displayable as part of
        the pictogram (e.g. for a maximum speed limit).
    :ivar weight_attribute: Value of weight that is displayable as part
        of the pictogram (e.g. for a maximum weight restriction).
    :ivar weight_per_axle_attribute: Value of axle weight that is
        displayable as part of the pictogram (e.g. for a maximum axle
        weight restriction).
    :ivar width_attribute: Value of width that is displayable as part of
        the pictogram (e.g. for a vehicle width restriction).
    :ivar vms_supplementary_panel:
    :ivar vms_pictogram_extension:
    """
    pictogram_description: List[VmsDatexPictogramEnum] = field(
        default_factory=list,
        metadata={
            "name": "pictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    pictogram_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    additional_pictogram_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalPictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_in_inverse_colour: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramInInverseColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    presence_of_red_triangle: Optional[bool] = field(
        default=None,
        metadata={
            "name": "presenceOfRedTriangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vienna_convention_compliant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "viennaConventionCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    height_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    length_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    speed_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "speedAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    weight_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    weight_per_axle_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightPerAxleAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    width_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "widthAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_panel: Optional[VmsSupplementaryPanel] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsRecord:
    """A sub-record in the VMS Unit table defining the characteristics of a
    single variable message sign that is controlled by a specific VMS unit.

    Locations are on or adjacent to the road network but may be updated
    over time if relating to a mobile VMS unit.

    :ivar vms_description: The description of the VMS (possibly giving a
        description of its location or its normal use).
    :ivar vms_owner: Owner (authority or organisation) of the VMS. This
        may not necessarily be the same as the authority or organisation
        which is currently controlling the VMS.
    :ivar vms_physical_mounting: Description of how the VMS is
        physically mounted or deployed on the road.
    :ivar vms_type: Broad classification of the type of variable message
        sign.
    :ivar vms_type_code: Specification of the type of VMS defined by a
        code, normally country or even manufacturer specific (e.g. MS4).
    :ivar number_of_pictogram_display_areas: Number of pictogram display
        areas which the VMS contains.
    :ivar dynamically_configurable_display_areas: Identifies (when True)
        that the VMS has a display area that may be dynamically
        configured to display different combinations of text and
        pictogram areas. The current configuration will normally be
        given with each published current VMS setting.
    :ivar vms_display_height: Height in metres of the sign's overall
        display area.
    :ivar vms_display_width: Width in metres of the sign's overall
        display area.
    :ivar vms_height_above_roadway: Height in metres of the mounted sign
        above the roadway, measured to the bottom of the display area.
    :ivar vms_text_display_characteristics:
    :ivar vms_pictogram_display_characteristics:
    :ivar vms_location: The point location of the variable message sign.
        For mobile VMS which are regularly moved this need not be
        provided. Instead the VMS location should be provided in the
        VmsPublication along with current settings.
    :ivar vms_managed_logical_location:
    :ivar background_image_url: A URL reference from where an image of
        the "painted" static background on the VMS can be obtained.
    :ivar vms_record_extension:
    """
    vms_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vmsDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_owner: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vmsOwner",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_physical_mounting: Optional[PhysicalMountingEnum] = field(
        default=None,
        metadata={
            "name": "vmsPhysicalMounting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_type: Optional[VmsTypeEnum] = field(
        default=None,
        metadata={
            "name": "vmsType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTypeCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    number_of_pictogram_display_areas: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPictogramDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dynamically_configurable_display_areas: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dynamicallyConfigurableDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "vmsDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "vmsDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_height_above_roadway: Optional[float] = field(
        default=None,
        metadata={
            "name": "vmsHeightAboveRoadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_display_characteristics: Optional[VmsTextDisplayCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsTextDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_characteristics: List[VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "vmsLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_managed_logical_location: Optional[VmsManagedLogicalLocation] = field(
        default=None,
        metadata={
            "name": "vmsManagedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    background_image_url: Optional[UrlLink] = field(
        default=None,
        metadata={
            "name": "backgroundImageUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Wind:
    """
    Wind conditions on the road.

    :ivar wind_measurement_height: The height in metres above the road
        surface at which the wind is measured.
    :ivar wind_speed: The wind speed averaged over at least 10 minutes,
        measured at a default height of10 metres (meteorological
        standard) above the road surface, unless measurement height is
        specified.
    :ivar maximum_wind_speed: The maximum wind speed in a measurement
        period of 10 minutes.
    :ivar wind_direction_bearing: The average direction from which the
        wind blows, in terms of a bearing measured in degrees (0 - 359).
    :ivar wind_direction_compass: The average direction from which the
        wind blows, in terms of points of the compass.
    :ivar wind_extension:
    """
    wind_measurement_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "windMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    wind_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_wind_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "maximumWindSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    wind_direction_bearing: Optional[DirectionBearingValue] = field(
        default=None,
        metadata={
            "name": "windDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    wind_direction_compass: Optional[DirectionCompassValue] = field(
        default=None,
        metadata={
            "name": "windDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    wind_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PredefinedItineraryIndexPredefinedLocation:
    class Meta:
        name = "_PredefinedItineraryIndexPredefinedLocation"

    predefined_location: Optional[PredefinedLocation] = field(
        default=None,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SiteMeasurementsIndexMeasuredValue:
    class Meta:
        name = "_SiteMeasurementsIndexMeasuredValue"

    measured_value: Optional[MeasuredValue] = field(
        default=None,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextPage:
    class Meta:
        name = "_TextPage"

    vms_text: Optional[VmsText] = field(
        default=None,
        metadata={
            "name": "vmsText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "pageNumber",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HumidityInformation(WeatherData):
    """
    Measurements of atmospheric humidity.
    """
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class IndividualVehicleDataValues(TrafficData):
    """
    Measured or calculated data values relating to individual vehicles derived
    from detectors at the specified measurement site.

    :ivar individual_vehicle_speed: The measured speed of the individual
        vehicle at the specified measurement site.
    :ivar arrival_time: The time of the arrival of an individual vehicle
        in a detection zone.
    :ivar exit_time: The time when an individual vehicle leaves a
        detection zone.
    :ivar passage_duration_time: The time elapsed between an individual
        vehicle entering a detection zone and exiting the same detection
        zone as detected by entry and exit sensors.
    :ivar presence_duration_time: The period of time during which a
        vehicle activates a presence sensor.
    :ivar time_gap: The time interval between the arrival of this
        vehicle's front at a point on the roadway, and that of the
        departure of the rear of the preceding one.
    :ivar time_headway: The measured time interval between this
        vehicle's arrival at (or departure from) a point on the roadway,
        and that of the preceding one.
    :ivar distance_gap: The measured distance between the front of this
        vehicle and the rear of the preceding one, in metres at the
        specified measurement site.
    :ivar distance_headway: The measured distance between the front
        (respectively back) of this vehicle and the front (respectively
        back) of the preceding vehicle at the specified measurement
        site.
    :ivar individual_vehicle_data_values_extension:
    """
    individual_vehicle_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "individualVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    arrival_time: Optional[DateTimeValue] = field(
        default=None,
        metadata={
            "name": "arrivalTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exit_time: Optional[DateTimeValue] = field(
        default=None,
        metadata={
            "name": "exitTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    passage_duration_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "passageDurationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    presence_duration_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "presenceDurationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_gap: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_headway: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "timeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_gap: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "distanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_headway: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "distanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    individual_vehicle_data_values_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "individualVehicleDataValuesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrExtendedLinear:
    """
    Extension class for OpenLR Line location reference.

    :ivar first_direction: First OpenLR reference in first/main
        direction.
    :ivar opposite_direction: If both direction, this is tha reference
        in the opposite direction against firstDirection.
    """
    first_direction: Optional[OpenlrLineLocationReference] = field(
        default=None,
        metadata={
            "name": "firstDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    opposite_direction: Optional[OpenlrLineLocationReference] = field(
        default=None,
        metadata={
            "name": "oppositeDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrPoiWithAccessPoint(OpenlrBasePointLocation):
    """
    Point along line with access is a point location which is defined by a
    line,an offset value and a coordinate.

    :ivar openlr_coordinate: The coordinate of the actual point of
        interest
    :ivar openlr_poi_with_access_point_extension:
    """
    openlr_coordinate: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_poi_with_access_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPoiWithAccessPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpenlrPointAlongLine(OpenlrBasePointLocation):
    """
    Point along a line.
    """
    openlr_point_along_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPointAlongLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PollutionInformation(WeatherData):
    """
    Measurements of atmospheric pollution.
    """
    pollution: List[Pollution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    pollution_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PrecipitationInformation(WeatherData):
    """
    Measurements of precipitation.

    :ivar no_precipitation: Indication of whether precipitation is
        present or not. True indicates there is no precipitation.
    :ivar precipitation_detail:
    :ivar precipitation_information_extension:
    """
    no_precipitation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPrecipitation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    precipitation_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PredefinedItinerary(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a predefined itinerary.

    :ivar predefined_itinerary_name: A name assigned to the predefined
        itinerary.
    :ivar predefined_location:
    :ivar predefined_itinerary_extension:
    :ivar id:
    :ivar version:
    """
    predefined_itinerary_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    predefined_location: List[PredefinedItineraryIndexPredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    predefined_itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class RoadSurfaceConditionInformation(WeatherData):
    """
    Measurements of road surface conditions which are related to the weather.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar road_surface_condition_information_extension:
    """
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    road_surface_condition_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SiteMeasurements:
    """
    A  measurement data set derived from a specific measurement site.

    :ivar measurement_site_reference: A reference to a versioned
        measurement site record defined in a Measurement Site table.
    :ivar measurement_time_default: The time associated with the set of
        measurements. It may be the time of the beginning, the end or
        the middle of the measurement period.
    :ivar measured_value: Composition to the indexed measured value
        associated with the measurement site. The index uniquely
        associates the measurement value with the corresponding indexed
        measurement characteristics defined for the measurement site.
    :ivar site_measurements_extension:
    """
    measurement_site_reference: Optional[MeasurementSiteRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measurement_time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measured_value: List[SiteMeasurementsIndexMeasuredValue] = field(
        default_factory=list,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TemperatureInformation(WeatherData):
    """
    Measurements of atmospheric temperature.
    """
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    temperature_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegJunction(TpegPoint):
    """
    A point on the road network which is a road junction point.

    :ivar point_coordinates:
    :ivar name: A name which identifies a junction point on the road
        network
    :ivar ilc: A descriptor for describing a junction by identifying the
        intersecting roads at a road junction.
    :ivar other_name: A descriptive name which helps to identify the
        junction point.
    :ivar tpeg_junction_extension:
    """
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    name: Optional[TpegJunctionPointDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    ilc: List[TpegIlcPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    other_name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "name": "otherName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tpeg_junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegNonJunctionPoint(TpegPoint):
    """
    A point on the road network which is not a road junction point.

    :ivar point_coordinates:
    :ivar name: A descriptive name which helps to identify the non
        junction point. At least one descriptor must identify the road
        on which the point is located, i.e. must be of type 'linkName'
        or 'localLinkName'.
    :ivar tpeg_non_junction_point_extension:
    """
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    tpeg_non_junction_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNonJunctionPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficConcentration(TrafficData):
    """
    Averaged measurements or calculations of traffic concentration.

    :ivar concentration: An averaged measurement or calculation of the
        concentration of vehicles at the specified measurement site.
    :ivar occupancy: An averaged measurement or calculation of the
        percentage of time that a section of road at the specified
        measurement site is occupied by vehicles.
    :ivar traffic_concentration_extension:
    """
    concentration: Optional[ConcentrationOfVehiclesValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    occupancy: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_concentration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficConcentrationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficFlow(TrafficData):
    """
    Averaged measurements or calculations of traffic flow rates.

    :ivar axle_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of vehicle axles passing the
        specified measurement site.
    :ivar pcu_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of passenger car units passing
        the specified measurement site.
    :ivar percentage_long_vehicles: An averaged measurement or
        calculation of the percentage of long vehicles contained in the
        traffic flow at the specified measurement site.
    :ivar vehicle_flow: An averaged measurement of flow rate defined in
        terms of the number of vehicles passing the specified
        measurement site.
    :ivar traffic_flow_extension:
    """
    axle_flow: Optional[AxleFlowValue] = field(
        default=None,
        metadata={
            "name": "axleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pcu_flow: Optional[PcuFlowValue] = field(
        default=None,
        metadata={
            "name": "pcuFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    percentage_long_vehicles: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "percentageLongVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_flow: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "vehicleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_flow_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficFlowExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficHeadway(TrafficData):
    """Averaged measurements or calculations of traffic headway, i.e. the
    distance or time interval between vehicles.

    This measure is measured from the head of one vehicle to the head of
    the following vehicle.

    :ivar average_distance_headway: The average distance between the
        front (respectively back) of this vehicle and the front
        (respectively  back) of the preceding vehicle, averaged for all
        vehicles within a defined measurement period at the specified
        measurement site.
    :ivar average_time_headway: The average time gap between the front
        (respectively back) of this vehicle and the front (respectively
        back) of the preceding vehicle, averaged for all vehicles within
        a defined measurement period at the specified measurement site.
    :ivar traffic_headway_extension:
    """
    average_distance_headway: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "averageDistanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    average_time_headway: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "averageTimeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficSpeed(TrafficData):
    """
    Averaged measurements or calculations of traffic speed.

    :ivar average_vehicle_speed: An averaged measurement or calculation
        of the speed of vehicles at the specified location.
    :ivar speed_percentile:
    :ivar traffic_speed_extension:
    """
    average_vehicle_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "averageVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    speed_percentile: Optional[SpeedPercentile] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleCountAndRate:
    """Vehicle rates can be assigned to a parking site or to assigned parking
    spaces.

    Furthermore, they can reference to a measurement site or to an
    entrance/exit.

    :ivar measurement_site_reference: A reference to a versioned
        measurement site record defined in a Measurement Site table.
    :ivar measured_value_index: If a measurement site is specified, the
        index of the measured value can be specified here.
    :ivar dedicated_access: Specifies a reference to an access, object
        (i.e. an entrance, an exit or both). A Point location and
        further characteristics can be specified for those objects.
    :ivar measurement_time_default: The time associated with the set of
        measurements. It may be the time of the beginning, the end or
        the middle of the measurement period.
    :ivar last_calibration: Date of last calibration of the detection
        system in question.
    :ivar covering_petrol_station_area: Indication, if this detector
        also covers the area of a petrol station.
    :ivar vehicle_count_within_interval:
    :ivar vehicle_rate:
    :ivar vehicle_count_and_rate_extension:
    """
    measurement_site_reference: Optional[MeasurementSiteRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measured_value_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "measuredValueIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dedicated_access: Optional[ParkingAccessReference] = field(
        default=None,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    last_calibration: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastCalibration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    covering_petrol_station_area: Optional[bool] = field(
        default=None,
        metadata={
            "name": "coveringPetrolStationArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_count_within_interval: List[VehicleCountWithinInterval] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCountWithinInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_rate: List[VehicleRate] = field(
        default_factory=list,
        metadata={
            "name": "vehicleRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_count_and_rate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCountAndRateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VisibilityInformation(WeatherData):
    """
    Measurements of atmospheric visibility.
    """
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    visibility_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class WindInformation(WeatherData):
    """
    Measurements of wind conditions.
    """
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    wind_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AreaExtensionType:
    class Meta:
        name = "_AreaExtensionType"

    openlr_extended_area: Optional[OpenlrExtendedArea] = field(
        default=None,
        metadata={
            "name": "openlrExtendedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    area_extended: Optional[AreaExtended] = field(
        default=None,
        metadata={
            "name": "areaExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class MeasurementSiteRecordIndexMeasurementSpecificCharacteristics:
    class Meta:
        name = "_MeasurementSiteRecordIndexMeasurementSpecificCharacteristics"

    measurement_specific_characteristics: Optional[MeasurementSpecificCharacteristics] = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PeriodExtensionType:
    class Meta:
        name = "_PeriodExtensionType"

    period_extended: Optional[PeriodExtended] = field(
        default=None,
        metadata={
            "name": "periodExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram:
    class Meta:
        name = "_VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram"

    vms_pictogram: Optional[VmsPictogram] = field(
        default=None,
        metadata={
            "name": "vmsPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_sequencing_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramSequencingIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsUnitRecordVmsIndexVmsRecord:
    class Meta:
        name = "_VmsUnitRecordVmsIndexVmsRecord"

    vms_record: Optional[VmsRecord] = field(
        default=None,
        metadata={
            "name": "vmsRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class D2LogicalModel(D2LogicalModel1):
    class Meta:
        name = "d2LogicalModel"
        namespace = "http://datex2.eu/schema/2/2_0"


@dataclass
class Area(Location):
    """
    A geographic or geometric defined area which may be qualified by height
    information to provide additional geospatial discrimination (e.g. for snow
    in an area but only above a certain altitude).
    """
    alert_carea: Optional[AlertCArea] = field(
        default=None,
        metadata={
            "name": "alertCArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tpeg_area_location: Optional[TpegAreaLocation] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    area_extension: Optional[AreaExtensionType] = field(
        default=None,
        metadata={
            "name": "areaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasuredDataPublication(PayloadPublication):
    """
    A publication containing one or more measurement data sets, each set being
    measured at a single measurement site.

    :ivar measurement_site_table_reference: A reference to a versioned
        Measurement Site table.
    :ivar header_information:
    :ivar site_measurements:
    :ivar measured_data_publication_extension:
    """
    measurement_site_table_reference: Optional[MeasurementSiteTableVersionedReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    site_measurements: List[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    measured_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasurementSiteRecord:
    """
    An identifiable single measurement site entry/record in the Measurement
    Site table.

    :ivar measurement_site_record_version_time: The date/time that this
        version of the measurement site record was defined. The identity
        and version of the measurement site record are defined by the
        class stereotype implementation.
    :ivar computation_method: Method of computation which is used to
        compute the measured value(s) at the measurement site.
    :ivar measurement_equipment_reference: The reference given to the
        measurement equipment at the site.
    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar measurement_site_name: Name of a measurement site.
    :ivar measurement_site_number_of_lanes: The number of lanes over
        which the measured value is determined.
    :ivar measurement_site_identification: Identification of a
        measurement site used by the supplier or consumer systems.
    :ivar measurement_side: Side of the road on which measurements are
        acquired, corresponding to the direction of the road.
    :ivar measurement_specific_characteristics: Composition to the
        indexed measurement specific characteristics associated with the
        measurement site. The index uniquely associates the measurement
        characteristics with the corresponding indexed measurement
        values for the measurement site.
    :ivar measurement_site_location:
    :ivar measurement_site_record_extension:
    :ivar id:
    :ivar version:
    """
    measurement_site_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    computation_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_equipment_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_site_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementSiteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_site_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_site_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    measurement_side: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "measurementSide",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_specific_characteristics: List[MeasurementSiteRecordIndexMeasurementSpecificCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    measurement_site_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "measurementSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measurement_site_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class OpenlrPointLocationReference:
    """
    A point location is a zero-dimensional element in a map that specifies a
    geometric location.
    """
    openlr_geo_coordinate: Optional[OpenlrGeoCoordinate] = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_poi_with_access_point: Optional[OpenlrPoiWithAccessPoint] = field(
        default=None,
        metadata={
            "name": "openlrPoiWithAccessPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_point_along_line: Optional[OpenlrPointAlongLine] = field(
        default=None,
        metadata={
            "name": "openlrPointAlongLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_point_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPointLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingOccupancy:
    """
    Parking capacity information for the parking site as well as for
    AssignedParkingSpaces.

    :ivar parking_number_of_spaces_override: Possibility to override the
        static value 'parkingNumberOfSpaces'.
    :ivar parking_number_of_vacant_spaces: The total number of currently
        vacant parking spaces available in the specified parking site,
        group of parking sites or group of parking spaces.
    :ivar parking_number_of_vacant_spaces_lower_than: The number of
        vacant parking spaces is lower than the given value (example:
        Less than 10 spaces are free).
    :ivar parking_number_of_vacant_spaces_higher_than: The number of
        vacant parking spaces is higher than the given value (example:
        More than 10 spaces are free).
    :ivar parking_number_of_vacant_spaces_graded: Number of vacant
        spaces by grading (enumeration).
    :ivar parking_number_of_occupied_spaces: The number of currently
        occupied spaces in the specified parking site, group of parking
        sites or assigned parking.
    :ivar parking_number_of_vehicles: Number of vehicles (of specified
        type) on the parking site, the group of parking sites or the
        group of parking spaces. Parking too narrow or too wide may
        effect differences to the 'occupiedSpaces' value. Should not
        include petrol station traffic.
    :ivar parking_occupancy: The percentage value of parking spaces
        occupied in the specified parking site, group of parking sites
        or assigned parking.
    :ivar parking_occupancy_graded: Occupied parking spaces by a
        percentage-grading (enumeration).
    :ivar parking_occupancy_trend: The trend of the occupancy of the
        parking spaces in the specified parking site, group of parking
        sites or assigned parking.
    :ivar parking_not_allowed: In case of 'true', parking is not allowed
        (e.g. abnormal closure).
    :ivar vehicle_count_and_rate:
    :ivar parking_occupancy_extension:
    """
    parking_number_of_spaces_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfSpacesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_vacant_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_vacant_spaces_lower_than: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpacesLowerThan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_vacant_spaces_higher_than: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpacesHigherThan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_vacant_spaces_graded: Optional[ParkingVacantSpacesEnum] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpacesGraded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_occupied_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfOccupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_number_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy: Optional[float] = field(
        default=None,
        metadata={
            "name": "parkingOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy_graded: Optional[ParkingOccupancyEnum] = field(
        default=None,
        metadata={
            "name": "parkingOccupancyGraded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy_trend: Optional[ParkingOccupancyTrendEnum] = field(
        default=None,
        metadata={
            "name": "parkingOccupancyTrend",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_not_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "parkingNotAllowed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_count_and_rate: List[VehicleCountAndRate] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCountAndRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingOccupancyExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Period:
    """
    A continuous time period or a set of discontinuous time periods defined by
    the intersection of a set of criteria all within an overall delimiting
    interval.

    :ivar start_of_period: Start of period.
    :ivar end_of_period: End of a period.
    :ivar period_name: The name of the period.
    :ivar recurring_time_period_of_day: A recurring period of a day.
    :ivar recurring_day_week_month_period: A recurring period defined in
        terms of days of the week, weeks of the month and months of the
        year.
    :ivar period_extension:
    """
    start_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    end_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    period_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    recurring_time_period_of_day: List[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    recurring_day_week_month_period: List[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    period_extension: Optional[PeriodExtensionType] = field(
        default=None,
        metadata={
            "name": "periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TpegFramedPoint(TpegPointLocation):
    """
    A point on the road network which is framed between two other points on the
    same road.

    :ivar tpeg_framed_point_location_type: The type of TPEG location.
    :ivar framed_point: A single non junction point on the road network
        which is framed between two other specified points on the road
        network.
    :ivar to: The location at the down stream end of the section of road
        which frames the TPEGFramedPoint.
    :ivar from_value: The location at the up stream end of the section
        of road which frames the TPEGFramedPoint.
    :ivar tpeg_framed_point_extension:
    """
    tpeg_framed_point_location_type: Optional[TpegLoc01FramedPointLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    framed_point: Optional[TpegNonJunctionPoint] = field(
        default=None,
        metadata={
            "name": "framedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_framed_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsPictogramDisplayArea:
    """
    An area on a VMS used for the display of pictograms and associated
    supplemental information or instructions.

    :ivar synchronized_sequencing_with_text_pages: Indicates whether the
        sequence of pictograms are sequenced synchronously with the text
        pages. If there is a mismatch in the number of sequenced text
        pages and sequenced pictograms, the sequences are assumed to
        resynchronize at the start of each sequence.
    :ivar vms_pictogram:
    :ivar vms_pictogram_display_area_extension:
    """
    synchronized_sequencing_with_text_pages: Optional[bool] = field(
        default=None,
        metadata={
            "name": "synchronizedSequencingWithTextPages",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram: List[VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsUnitRecord:
    """
    A versioned single VMS unit entry/record in the VMS Unit table that defines
    the characteristics of the VMS unit.

    :ivar number_of_vms: Number of variable message signs contolled by
        the unit.
    :ivar vms_unit_identifier: Identification of a VMS unit used by the
        supplier or consumer systems.
    :ivar vms_unit_ipaddress: IP network address of the VMS unit.
    :ivar vms_unit_electronic_address: Electronic address of the VMS
        unit (if not IP addressable).
    :ivar vms_record:
    :ivar vms_unit_record_extension:
    :ivar id:
    :ivar version:
    """
    number_of_vms: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVms",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitIPAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_electronic_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitElectronicAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_record: List[VmsUnitRecordVmsIndexVmsRecord] = field(
        default_factory=list,
        metadata={
            "name": "vmsRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class LinearExtensionType:
    class Meta:
        name = "_LinearExtensionType"

    openlr_extended_linear: Optional[OpenlrExtendedLinear] = field(
        default=None,
        metadata={
            "name": "openlrExtendedLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class AreaDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary which
    is an area.
    """
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfParkingSpacesStatus(ParkingOccupancy):
    """
    The status of the assigned parking spaces in the specified parking site,
    i.e. the status of those spaces assigned for particular types of person or
    vehicle and/or for specific duration types (e.g. short stay).

    :ivar group_declaration_valid_now: Override validity of
        AssignedParkingSpaces: True = Parking space declaration is valid
        now; False = Parking space declaration is invalid now; Omitted =
        Static validity information is significant (if static validity
        is omitted too, declaration is valid).
    :ivar group_of_parking_spaces_closed: True: The group of parking
        spaces is closed / not accessible. False or omitted: The group
        of parking spaces is accessible. This is no statement about its
        occupation.
    :ivar group_of_parking_spaces_status_extension:
    """
    group_declaration_valid_now: Optional[bool] = field(
        default=None,
        metadata={
            "name": "groupDeclarationValidNow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_spaces_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesClosed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_spaces_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Linear(NetworkLocation):
    """
    A linear section along a single road with optional directionality defined
    between two points on the same road.
    """
    tpeg_linear_location: Optional[TpegLinearLocation] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    alert_clinear: Optional[AlertCLinear] = field(
        default=None,
        metadata={
            "name": "alertCLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_within_linear_element: Optional[LinearWithinLinearElement] = field(
        default=None,
        metadata={
            "name": "linearWithinLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_extension: Optional[LinearExtensionType] = field(
        default=None,
        metadata={
            "name": "linearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasurementSiteTable:
    """A Measurement Site Table comprising a number of sets of data, each
    describing the location from where a stream of measured data may be
    derived.

    Each location is known as a "measurement site" which can be a point,
    a linear road section or an area.

    :ivar measurement_site_table_identification: An alphanumeric
        identification for the measurement site table, possibly human
        readable.
    :ivar measurement_site_record:
    :ivar measurement_site_table_extension:
    :ivar id:
    :ivar version:
    """
    measurement_site_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    measurement_site_record: List[MeasurementSiteRecord] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    measurement_site_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class OpenlrExtendedPoint:
    """
    Extension class for OpenLR point.
    """
    openlr_point_location_reference: Optional[OpenlrPointLocationReference] = field(
        default=None,
        metadata={
            "name": "openlrPointLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )


@dataclass
class OverallPeriod:
    """
    A continuous or discontinuous period of validity defined by overall
    bounding start and end times and the possible intersection of valid periods
    (potentially recurring) with the complement of exception periods (also
    potentially recurring).

    :ivar overall_start_time: Start of bounding period of validity
        defined by date and time.
    :ivar overall_end_time: End of bounding period of validity defined
        by date and time.
    :ivar valid_period: A single time period, a recurring time period or
        a set of different recurring time periods during which validity
        is true.
    :ivar exception_period: A single time period, a recurring time
        period or a set of different recurring time periods during which
        validity is false.
    :ivar overall_period_extension:
    """
    overall_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    overall_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    valid_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "validPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exception_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "exceptionPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    overall_period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsUnitTable:
    """
    A versioned VMS Unit Table comprising a number of data records, each record
    defining the characteristics of a specific deployed variable message sign
    unit.

    :ivar vms_unit_table_identification: An alphanumeric identification
        for the VMS Unit table, possibly human readable.
    :ivar vms_unit_record:
    :ivar vms_unit_table_extension:
    :ivar id:
    :ivar version:
    """
    vms_unit_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_record: List[VmsUnitRecord] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    vms_unit_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea:
    class Meta:
        name = "_VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea"

    vms_pictogram_display_area: Optional[VmsPictogramDisplayArea] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ChargeBand:
    """
    A charge band in accordance with the specified conditions, possibly up to a
    maximum duration, during a specified period and for a vehicle of specified
    characteristics (in case of parking).

    :ivar charge_currency: A three-character code according to ISO 4217
        for the currency in which the parking charge is specified (e.g.
        EUR, GBP, SEK, CZK).
    :ivar maximum_duration: The maximum duration (e.g. of parking) for
        which the specified charge is applicable.
    :ivar charge_band_name: Name for this charge band.
    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar charge:
    :ivar applicable_for_period: Charge band limitation on a (complex)
        period, described by the validity model.
    :ivar applicable_for_vehicles: Charge band limitation on a set of
        vehicles described by their characteristics.
    :ivar parking_permit:
    :ivar charge_band_extension:
    :ivar id:
    :ivar version:
    """
    charge_currency: Optional[CurrencyEnum] = field(
        default=None,
        metadata={
            "name": "chargeCurrency",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    maximum_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chargeBandName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_user: List[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge: List[Charge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    applicable_for_period: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "applicableForPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_vehicles: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "applicableForVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_permit: List[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "chargeBandExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class Contact:
    """
    Address and contact information about some person, service or the parking
    site, provided in detail or via reference.

    :ivar contact_unknown: When true, the contact for the selected role
        and/or timeframe is unknown. Don't use the specialisations in
        this case.
    :ivar contact_not_defined: When true, there is currently no contact
        defined for the selected role and/or timeframe. Don't use the
        specialisations in this case.
    :ivar validity_of_contact:
    :ivar contact_extension:
    """
    contact_unknown: Optional[bool] = field(
        default=None,
        metadata={
            "name": "contactUnknown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_not_defined: Optional[bool] = field(
        default=None,
        metadata={
            "name": "contactNotDefined",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity_of_contact: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityOfContact",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class MeasurementSiteTablePublication(PayloadPublication):
    """
    A publication containing one or more Measurment Site Tables.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measurement_site_table: List[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    measurement_site_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingStatusValidity:
    """To be used only for historical or forecasted data.

    Choose between an explicit point of time, an offset or all points of
    time within a specified period.

    :ivar parking_status_time: Only use for forecasts or historical data
        to express the point of time for which the information of this
        parking is either reported or forecasted. Alternately you can
        define this point of time as an offset with
        'parkingStatusTimeOffsetToOrigin'.
    :ivar parking_status_time_offset_to_origin: Only use for forecasts
        or historical data to express the point of time for which the
        information of this parking is either reported or forecasted (in
        form of an offset in seconds to 'parkingStatusOriginTime'; use
        negative values for historical data).
    :ivar validity_time_specification: A specification of periods of
        validity defined by overall bounding start and end times and the
        possible intersection of valid periods with exception periods
        (exception periods overriding valid periods).
    :ivar parking_status_validity_extension:
    """
    parking_status_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingStatusTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_time_offset_to_origin: Optional[float] = field(
        default=None,
        metadata={
            "name": "parkingStatusTimeOffsetToOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingStatusValidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingUsageScenario:
    """A special type of usage available for the parking site or the group of
    parking spaces.

    In the 'ParkingStatusPublication', the operation type (in operation
    or not) can be defined.

    :ivar parking_usage_scenario: A special type of usage available for
        the parking site or a group of parking spaces. In the
        'ParkingStatusPublication', the operation type (in operation or
        not) can be defined.
    :ivar truck_parking_dynamic_management: Two modes for parking
        lorries in a efficient way according to their departure times.
        May only be used for parking scenario 'truckParking'.
    :ivar event_parking_type: Parking associated with an event. May only
        be used for parking scenario 'eventParking'.
    :ivar event_parking_type2: Parking associated with an event. May
        only be used for parking scenario 'eventParking'.
    :ivar scenario_availability:
    :ivar parking_usage_scenario_extension:
    """
    parking_usage_scenario: Optional[ParkingUsageScenarioEnum] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    truck_parking_dynamic_management: List[TruckParkingDynamicManagementEnum] = field(
        default_factory=list,
        metadata={
            "name": "truckParkingDynamicManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    event_parking_type: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "eventParkingType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    event_parking_type2: Optional[PublicEventType2Enum] = field(
        default=None,
        metadata={
            "name": "eventParkingType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    scenario_availability: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "scenarioAvailability",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_usage_scenario_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingVehicle:
    """
    Information about one individual parking vehicle.

    :ivar parking_record_reference: A reference to a static parking
        record object, i.e. a parking site or a group of parking sites.
    :ivar parking_space_reference: Points to the parking space, on which
        the vehicle is located. The reference is only unique in
        combination with 'parkingRecordReference'.
    :ivar group_of_parking_spaces_reference: Points to one or more
        groups of parking spaces, to which the parking space of the
        vehicle belongs. The reference is only unique in combination
        with 'parkingRecordReference'.
    :ivar parking_permit:
    :ivar vehicle:
    :ivar individual_charge:
    :ivar parking_period:
    :ivar parking_vehicle_extension:
    :ivar id:
    :ivar version:
    """
    parking_record_reference: Optional[ParkingRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "parkingRecordReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingSpaceReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    group_of_parking_spaces_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpacesReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    parking_permit: List[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    individual_charge: Optional[IndividualCharge] = field(
        default=None,
        metadata={
            "name": "individualCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_period: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "parkingPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingVehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class Validity:
    """
    Specification of validity, either explicitly or by a validity time period
    specification which may be discontinuous.

    :ivar validity_status: Specification of validity, either explicitly
        overriding the validity time specification or confirming it.
    :ivar overrunning: The activity or action described by the
        SituationRecord is still in progress, overrunning its planned
        duration as indicated in a previous version of this record.
    :ivar validity_time_specification: A specification of periods of
        validity defined by overall bounding start and end times and the
        possible intersection of valid periods with exception periods
        (exception periods overriding valid periods).
    :ivar validity_extension:
    """
    validity_status: Optional[ValidityStatusEnum] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsMessage:
    """A message displayed on a VMS which may comprise one or more sequentially
    displayed text pages and/or pictograms with supplementary details.

    When in a sequence of displayed messages sequencing of text pages
    and pictograms within a message are prohibited.

    :ivar associated_management_or_diversion_plan: The identification of
        the traffic management plan or diversion plan with which the
        message is associated.
    :ivar message_set_by: The organisation or authority which set the
        message currently being displayed.
    :ivar set_by_system: Indicates whether the message has been set
        automatically by a system. True =  automatically set.
    :ivar reason_for_setting: The reason why the sign has been set.
    :ivar coded_reason_for_setting: The reason, in terms of a high level
        coded classification, why the sign has been set.
    :ivar vms_message_information_type: Type of information being
        displayed.
    :ivar primary_setting: Identifies whether the message setting is
        primary (explicitly requested) or is secondary (derived
        according to an algorthm as the result of setting other signs).
        True = a primary setting.
    :ivar mare_nostrum_compliant: Indication that the displayed message
        (text and pictogram) conforms with the formulation recommended
        by the Mare Nostrum project.
    :ivar time_last_set: The date/time at which the sign was last set.
    :ivar requested_by: The authority, organisation or system which
        requested the setting of the message. This may be different from
        the authority or system which actually set the message on behalf
        of the requestor.
    :ivar situation_to_which_message_is_related: A reference to the
        managed situation to which the set message relates.
    :ivar situation_record_to_which_message_is_related: A reference to
        the situation record/element within a managed situation to which
        the set message relates.
    :ivar distance_from_situation_record: Distance of the VMS from the
        location of the related situation record/element. If the VMS is
        located within the extent of the situation record/element this
        should be set to zero.
    :ivar text_pictogram_sequencing_interval: The time duration that
        each text page or pictogram within a message is displayed for
        before the VMS displays the next text page and/or pictogram in
        the message.
    :ivar text_page:
    :ivar vms_pictogram_display_area:
    :ivar vms_message_extension:
    """
    associated_management_or_diversion_plan: Optional[str] = field(
        default=None,
        metadata={
            "name": "associatedManagementOrDiversionPlan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    message_set_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "messageSetBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    set_by_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "setBySystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reason_for_setting: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    coded_reason_for_setting: Optional[CodedReasonForSettingMessageEnum] = field(
        default=None,
        metadata={
            "name": "codedReasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_message_information_type: List[VmsMessageInformationTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vmsMessageInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    primary_setting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "primarySetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    mare_nostrum_compliant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mareNostrumCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_last_set: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeLastSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    requested_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "requestedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_to_which_message_is_related: Optional[VersionedReference] = field(
        default=None,
        metadata={
            "name": "situationToWhichMessageIsRelated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_record_to_which_message_is_related: Optional[VersionedReference] = field(
        default=None,
        metadata={
            "name": "situationRecordToWhichMessageIsRelated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_situation_record: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceFromSituationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_pictogram_sequencing_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPictogramSequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_page: List[TextPage] = field(
        default_factory=list,
        metadata={
            "name": "textPage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_area: List[VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_message_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsMessageExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsTablePublication(PayloadPublication):
    """
    A publication containing one or more VMS Unit Tables each comprising a set
    of records which hold details of VMS units.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_unit_table: List[VmsUnitTable] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    vms_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus:
    class Meta:
        name = "_ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus"

    group_of_parking_spaces_status: Optional[GroupOfParkingSpacesStatus] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    group_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "groupIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PointExtensionType:
    class Meta:
        name = "_PointExtensionType"

    openlr_extended_point: Optional[OpenlrExtendedPoint] = field(
        default=None,
        metadata={
            "name": "openlrExtendedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_extended: Optional[PointExtended] = field(
        default=None,
        metadata={
            "name": "pointExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class ContactByReference(Contact):
    """
    Contact information that is addressed via a reference.

    :ivar contact_reference: Contact information provided by a
        reference.
    :ivar contact_by_reference_extension:
    """
    contact_reference: Optional[ContactDetailsVersionedReference] = field(
        default=None,
        metadata={
            "name": "contactReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    contact_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ContactDetails(Contact):
    """
    Details for some person, service or the parking site itself, especially
    address information.

    :ivar contact_organisation_name: Name of the organisation or
        service. Do not use this attribute in combination with role
        "parkingSiteAddress".
    :ivar contact_person_name: Name of the contact person.
    :ivar contact_person_first_name: First name of the contact person.
    :ivar contact_person_position: The position of the contact person.
    :ivar contact_details_language: Language(s) this contact is able to
        speak resp. understand.
    :ivar contact_details_address: Complete address of the contact.
        Alternatively use the separate fields to describe the address.
    :ivar contact_details_street: Street of the contact.
    :ivar contact_details_house_number: House number of the contact.
        Supports a multiplicity up to two, to specify lower and upper
        numbers.
    :ivar contact_details_postcode: Postcode of the contact.
    :ivar contact_details_city: City of the contact.
    :ivar country: ISO 3166-1 two character country code.
    :ivar contact_details_telephone_number: Telephone Number of contact.
    :ivar contact_details_fax: Fax of the contact.
    :ivar contact_details_email: E-Mail address of the contact.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar contact_details_logo_url: Url to define a logo of this
        contact.
    :ivar available24hours: Specifies if the availability is 24 hours a
        day. If omitted, this information is unknown or heterogeneous.
    :ivar contact_details_responsibility: Specification of what service
        or equipment the contact is responsible for.
    :ivar contact_details_more_info: Additional information relating to
        the contact.
    :ivar publishing_agreement: Indication, whether the contact accepted
        publishing its contact information.
    :ivar contact_details_ownership: Information if the contact in
        question is a private or public institution.
    :ivar group_of_locations:
    :ivar contact_details_extension:
    :ivar id:
    :ivar version:
    """
    contact_organisation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactOrganisationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_person_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPersonName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_person_first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPersonFirstName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_person_position: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactPersonPosition",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsLanguage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_address: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactDetailsAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_street: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsStreet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_details_house_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsHouseNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
            "max_length": 1024,
        }
    )
    contact_details_postcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsPostcode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_details_city: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactDetailsCity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_telephone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsTelephoneNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_details_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsFax",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    contact_details_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsEMail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_logo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsLogoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    available24hours: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_responsibility: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsResponsibility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_more_info: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsMoreInfo",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    publishing_agreement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "publishingAgreement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_ownership: Optional[OwnershipTypeEnum] = field(
        default=None,
        metadata={
            "name": "contactDetailsOwnership",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_details_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactDetailsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class ElaboratedData:
    """An instance of data which is derived/computed from one or more
    measurements over a period of time.

    It may be a current value or a forecast value predicted from
    historical measurements.

    :ivar forecast: Indication of whether this elaborated data is a
        forecast (true = forecast).
    :ivar source:
    :ivar validity:
    :ivar elaborated_data_fault:
    :ivar basic_data:
    :ivar elaborated_data_extension:
    """
    forecast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    elaborated_data_fault: List[ElaboratedDataFault] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedDataFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    basic_data: Optional[BasicData] = field(
        default=None,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    elaborated_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OpeningTimes:
    """
    A specification of opening times (e.g. for a parking site, a service
    facility, an access or the availability for equipment).

    :ivar last_updated: The date/time at which this information was last
        updated.
    :ivar open_all_year: indicates whether the parking facility is
        available 365 days a year
    :ivar available24hours: Specifies if the availability is 24 hours a
        day. If omitted, this information is unknown or heterogeneous.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar opening_times_unknown: When true, the opening times are
        unknown.
    :ivar opening_times_not_specified: When true, the opening times are
        not specified.
    :ivar validity:
    :ivar opening_times_extension:
    """
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    open_all_year: Optional[bool] = field(
        default=None,
        metadata={
            "name": "openAllYear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    available24hours: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    opening_times_unknown: Optional[bool] = field(
        default=None,
        metadata={
            "name": "openingTimesUnknown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    opening_times_not_specified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "openingTimesNotSpecified",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    opening_times_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openingTimesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRecordStatus:
    """Contains the current status of one parking record defined in the static
    model (i.e. parking site or group of parking sites) or historical or
    forecasted data for one parking.

    Only for the second case, 'parkingStatusTime' must be specified.

    :ivar parking_record_reference: A reference to a static parking
        record object, i.e. a parking site or a group of parking sites.
    :ivar parking_status_origin_time: The time when the information in
        this message was generated. Unless 'ParkingStatusValidity' is
        used, this is also the time the information in this message
        refers to.
    :ivar parking_status_description: Additional textual information
        about the parking status. Can also be used as an alternative in
        case the enumeration values for 'parkingSiteStatus' or
        'groupOfParkingSitesStatus' do not fit.
    :ivar parking_queueing_time: The current queuing time (duration) for
        entering the parking site.
    :ivar parking_conditions: Defines if normal parking conditions are
        suspended or special parking conditions are in force.
    :ivar blurred_availability: When true, all information about
        availability (free spaces etc.) is blurred (usually because of
        business competition).
    :ivar parking_fault: A fault indicator for the parking site.
    :ivar winter_equipment_management_type: Type of winter equipment
        management action instigated by operator.
    :ivar parking_space_status:
    :ivar parking_occupancy:
    :ivar group_of_parking_spaces_status:
    :ivar parking_status_validity:
    :ivar override_parking_thresholds: Possibility to override the
        thresholds for the parking, which are in principle defined in
        the static part of the model (ParkingStatusPublication).
    :ivar parking_equipment_or_service_facility_status:
    :ivar parking_usage_scenario_status:
    :ivar parking_access_status:
    :ivar parking_route_status:
    :ivar parking_record_status_extension:
    """
    parking_record_reference: Optional[ParkingRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "parkingRecordReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_status_origin_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingStatusOriginTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_status_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingStatusDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_queueing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "parkingQueueingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_conditions: Optional[ParkingConditionsEnum] = field(
        default=None,
        metadata={
            "name": "parkingConditions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    blurred_availability: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "blurredAvailability",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_fault: List[ParkingFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    winter_equipment_management_type: List[WinterEquipmentManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_status: List[ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpaceStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy: Optional[ParkingOccupancy] = field(
        default=None,
        metadata={
            "name": "parkingOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    group_of_parking_spaces_status: List[ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpacesStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_validity: Optional[ParkingStatusValidity] = field(
        default=None,
        metadata={
            "name": "parkingStatusValidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    override_parking_thresholds: Optional[ParkingThresholds] = field(
        default=None,
        metadata={
            "name": "overrideParkingThresholds",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility_status: List[ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_usage_scenario_status: List[ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenarioStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_access_status: List[ParkingAccessStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingAccessStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_status: List[ParkingRouteStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingRouteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRecordStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingVMS:
    """
    A reference to a record that contains the metadata for a specific VMS unit
    that may be used to manage the parking site (e.g. to indicate to drivers
    the current availability of spaces).

    :ivar vms_unit_used_to_manage_parking: A reference to a record that
        contains the metadata for a specific VMS unit that may be used
        to manage the parking site (e.g. to indicate to drivers the
        current availability of spaces).
    :ivar vms_operator:
    :ivar parking_vmsextension:
    """
    vms_unit_used_to_manage_parking: Optional[VmsUnitRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsUnitUsedToManageParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_operator: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "vmsOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vmsextension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingVMSExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingVehiclesPublication:
    """
    Information about individual parking vehicles.

    :ivar parking_table_reference: It is possible to limit the
        publication to one or more ParkingTable and to set a reference
        to these tables here.
    :ivar parking_vehicle:
    """
    parking_table_reference: List[ParkingTableVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vehicle: List[ParkingVehicle] = field(
        default_factory=list,
        metadata={
            "name": "parkingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )


@dataclass
class Point(NetworkLocation):
    """
    A single geospatial point.
    """
    tpeg_point_location: Optional[TpegPointLocation] = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    alert_cpoint: Optional[AlertCPoint] = field(
        default=None,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_along_linear_element: Optional[PointAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "pointAlongLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    point_extension: Optional[PointExtensionType] = field(
        default=None,
        metadata={
            "name": "pointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar source:
    :ivar validity:
    :ivar impact:
    :ivar cause:
    :ivar general_public_comment: A comment which may be freely
        distributed to the general public
    :ivar non_general_public_comment: A comment which should not be
        distributed to the general public.
    :ivar url_link:
    :ivar group_of_locations:
    :ivar management:
    :ivar situation_record_extension:
    :ivar id:
    :ivar version:
    """
    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    confidentiality_override: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    severity: Optional[SeverityEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_record_extension: Optional[SituationRecordExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class TariffsAndPayment:
    """
    A table of charges under various conditions, primary used for parking.

    :ivar last_updated: The date/time at which this information was last
        updated.
    :ivar accepted_means_of_payment: Method(s) by which the user can
        make payments. In case of 'paymentCard' use AcceptedPaymentCards
        to specify more details.
    :ivar payment_mode: Modes how to realize the payment
        ('payAndDisplay', 'payByPrepaidToken', ...).
    :ivar payment_additional_description: Additional description, for
        instance instructions or telephone number for paying by SMS.
    :ivar free_of_charge: No fee at all. In this case, no further
        elements of the tariffs structure are needed.
    :ivar reservation_fee: A fee for reservation, if this is uniform for
        all situations. Can also be 0 to indicate free reservations.
        This attribute does not indicate if reservation is available at
        all and/or mandatory.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar charge_band:
    :ivar charge_band_by_reference:
    :ivar accepted_payment_cards:
    :ivar tariffs_and_payment_extension:
    """
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accepted_means_of_payment: List[MeansOfPaymentEnum] = field(
        default_factory=list,
        metadata={
            "name": "acceptedMeansOfPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    payment_mode: List[ParkingPaymentModeEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    payment_additional_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "paymentAdditionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    free_of_charge: Optional[bool] = field(
        default=None,
        metadata={
            "name": "freeOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reservation_fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "reservationFee",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "total_digits": 8,
            "fraction_digits": 2,
        }
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band: List[ChargeBand] = field(
        default_factory=list,
        metadata={
            "name": "chargeBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band_by_reference: List[ChargeBandByReference] = field(
        default_factory=list,
        metadata={
            "name": "chargeBandByReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accepted_payment_cards: Optional[AcceptedPaymentCards] = field(
        default=None,
        metadata={
            "name": "acceptedPaymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tariffs_and_payment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tariffsAndPaymentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSiteScenarioIndexParkingUsageScenario:
    class Meta:
        name = "_ParkingSiteScenarioIndexParkingUsageScenario"

    parking_usage_scenario: Optional[ParkingUsageScenario] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scenario_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingSpaceBasicsScenarioIndexParkingUsageScenario:
    class Meta:
        name = "_ParkingSpaceBasicsScenarioIndexParkingUsageScenario"

    parking_usage_scenario: Optional[ParkingUsageScenario] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scenario_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsMessageIndexVmsMessage:
    class Meta:
        name = "_VmsMessageIndexVmsMessage"

    vms_message: Optional[VmsMessage] = field(
        default=None,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    message_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "messageIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ElaboratedDataPublication(PayloadPublication):
    """
    A publication containing one or more elaborated data sets.

    :ivar forecast_default: The default value for the publication of
        whether the elaborated data is a forecast (true = forecast).
    :ivar period_default: The default value for the publication of the
        time elapsed between the beginning and the end of the sampling
        or measurement period. This item may differ from the unit
        attribute; e.g. an hourly flow can be estimated from a 5-minute
        measurement period.
    :ivar time_default: The default for the publication of the time at
        which the values have been computed/derived.
    :ivar header_information:
    :ivar reference_settings:
    :ivar elaborated_data:
    :ivar elaborated_data_publication_extension:
    """
    forecast_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "forecastDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    period_default: Optional[float] = field(
        default=None,
        metadata={
            "name": "periodDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    reference_settings: Optional[ReferenceSettings] = field(
        default=None,
        metadata={
            "name": "referenceSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    elaborated_data: List[ElaboratedData] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    elaborated_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfParkingSitesStatus(ParkingRecordStatus):
    """
    Dynamic status information for the static object 'GroupOfParkingSites'.

    :ivar group_of_parking_sites_status: The status of the group of
        parking sites (available spaces or not).
    :ivar group_of_parking_sites_status_extension:
    """
    group_of_parking_sites_status: Optional[GroupOfParkingSitesStatusEnum] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_sites_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonRoadEventInformation(SituationRecord):
    """
    Information about an event which is not on the road, but which may
    influence the behaviour of drivers and hence the characteristics of the
    traffic flow.
    """
    non_road_event_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonRoadEventInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class OperatorAction(SituationRecord):
    """
    Actions that a traffic operator can decide to implement to prevent or help
    correct dangerous or poor driving conditions, including maintenance of the
    road infrastructure.

    :ivar action_origin: Indicates whether the actions to be undertaken
        by the operator are the result of an internal operation or
        external influence.
    :ivar action_plan_identifier: The identifier of the traffic
        management action plan to which this action relates.
    :ivar operator_action_status: The status of the defined operator
        action.
    :ivar operator_action_extension:
    """
    action_origin: Optional[OperatorActionOriginEnum] = field(
        default=None,
        metadata={
            "name": "actionOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    action_plan_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionPlanIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    operator_action_status: Optional[OperatorActionStatusEnum] = field(
        default=None,
        metadata={
            "name": "operatorActionStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    operator_action_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingAccess:
    """
    Describes one entrance or exit (or both) to a parking site.

    :ivar access_category: Specifies the category(s) of this access.
    :ivar access_name: A name of the entrance or exit. This might be an
        indication to the corresponding road, for example.
    :ivar access_equipment: Specifies additional equipment for this
        access.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar access_only_assigned_for: Only the assignment given in this
        class is allowed for this access, i.e. other assignments are not
        allowed. By using this role, do not use the same set of
        attributes within the other two roles.
    :ivar access_assigned_among_others: The assignment given in this
        class is convenient for this access, but not exclusionary. By
        using this role, do not use the same set of attributes within
        the other two roles.
    :ivar access_prohibited_for: The assignment given in this class is
        prohibited for this access. By using this role, do not use the
        same set of attributes within the other two roles.
    :ivar primary_road: Identification for up to two primary roads
        located nearby the access or which make the parking accessible.
    :ivar location:
    :ivar opening_times:
    :ivar parking_access_extension:
    :ivar id:
    """
    access_category: List[AccessCategoryEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessCategory",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    access_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "accessName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    access_equipment: List[AccessEquipmentEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accessibility: List[AccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    photo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    access_only_assigned_for: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "accessOnlyAssignedFor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    access_assigned_among_others: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "accessAssignedAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    access_prohibited_for: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "accessProhibitedFor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    primary_road: List[Road] = field(
        default_factory=list,
        metadata={
            "name": "primaryRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    opening_times: Optional[OpeningTimes] = field(
        default=None,
        metadata={
            "name": "openingTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_access_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingAccessExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class ParkingEquipmentOrServiceFacility:
    """
    One type of equipment or additional service facility that is available at
    the parking site, parking space or group of parking spaces.

    :ivar equipment_or_service_facility_identifier: An internal
        identifier for the equipment or service facility, e.g. an
        inventory number. This attribute has an unbounded multiplicity
        to support identifiers for multiple occurrences of this element.
    :ivar availability: Specifies, if the element in question is
        available or not. Note that this is no dynamic information!
    :ivar number_of_equipment_or_service_facility: Number of the
        specified element (e.g. number of toilets, restaurants, park
        &amp; ride places, etc.) with respect to user restriction for
        the parking record, a complete group of spaces or a single
        space. Dynamic overridable.
    :ivar additional_description: Provides an additional description.
    :ivar other_equipment_or_service_facility: Specifies the additional
        equipment or service facility, if the enumerations provided do
        not fit. Use literal 'other' in this case.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar name_or_brand: Name or brand of the equipment or service
        facility, e.g. brand of petrol station, name of the WC-Service
        etc.
    :ivar comment: A free text comment that can be used by the operator
        to convey un-coded observations/information.
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar availability_and_opening_times: Specify the general
        availability of some equipment or service facility (by using
        just the 'OverallPeriod' component) or specify its opening times
        more detailed.
    :ivar tariffs_and_payment:
    :ivar group_of_locations:
    :ivar applicable_for_vehicles:
    :ivar parking_equipment_or_service_facility_extension:
    """
    equipment_or_service_facility_identifier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "equipmentOrServiceFacilityIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    availability: Optional[AvailabilityEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_equipment_or_service_facility: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    additional_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_equipment_or_service_facility: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "otherEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accessibility: List[AccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    name_or_brand: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "nameOrBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    photo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_user: List[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    availability_and_opening_times: Optional[OpeningTimes] = field(
        default=None,
        metadata={
            "name": "availabilityAndOpeningTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tariffs_and_payment: Optional[TariffsAndPayment] = field(
        default=None,
        metadata={
            "name": "tariffsAndPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_vehicles: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "applicableForVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSiteStatus(ParkingRecordStatus):
    """
    Dynamic status information for the static object 'ParkingSite'.

    :ivar parking_site_status: The status of the parking site (spaces
        available or not).
    :ivar parking_site_opening_status: The opening status of the parking
        site (open or not).
    :ivar parking_site_overcrowding_status: The overcrowding status of
        the parking site. Choose between using a two-stage approach or
        the more general statement ‘(not) overcrowding’. You can sharpen
        this information by using the ‘Thresholds’ component.
    :ivar parking_site_full_at_floor: The parking site is full at the
        specified floor(s).
    :ivar parking_site_status_extension:
    """
    parking_site_status: Optional[ParkingSiteStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_opening_status: Optional[OpeningStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_overcrowding_status: Optional[ParkingSiteOvercrowdingStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteOvercrowdingStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_full_at_floor: List[int] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteFullAtFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSiteStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingStatusPublication:
    """
    A publication containing the current status of one or more parking sites
    and/or group of parking sites.

    :ivar parking_table_reference: It is possible to limit the
        publication to one or more ParkingTable and to set a reference
        to these tables here.
    :ivar header_information:
    :ivar parking_record_status:
    """
    parking_table_reference: List[ParkingTableVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_status: List[ParkingRecordStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingRecordStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )


@dataclass
class PointDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary which
    is a point.
    """
    point: Optional[Point] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar related_situation: A reference to a related situation via its
        unique identifier.
    :ivar situation_version_time: The date/time that this current
        version of the Situation was written into the database of the
        supplier which is involved in the data exchange. Identity and
        version of the situation are defined by the class stereotype
        implementation.
    :ivar header_information:
    :ivar situation_record:
    :ivar situation_extension:
    :ivar id:
    :ivar version:
    """
    overall_severity: Optional[SeverityEnum] = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    related_situation: List[SituationVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    situation_record: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class TrafficElement(SituationRecord):
    """
    An event which is not planned by the traffic operator, which is affecting,
    or has the potential to affect traffic flow.
    """
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Vms:
    """Provides the current status and settings of the VMS and the currently
    displayed information.

    Where a VMS is displaying a sequence or alternating set of messages
    these are ordered according to the messageIndex qualifier.

    :ivar vms_working: Indicates whether the VMS is usable. Note it may
        still be usable with minor faults.
    :ivar vms_message_sequencing_interval: The time duration that each
        message is displayed for before the VMS displays the next
        message in the sequence.
    :ivar vms_message:
    :ivar text_display_area_settings:
    :ivar pictogram_display_area_settings:
    :ivar vms_location_override: The current point location of the VMS
        which overrides that stated in the associated VMSTable entry.
        Typically it is used for giving the updated location of a mobile
        VMS which has recently been moved.
    :ivar managed_logical_location_override: The current location that
        is being managed by the VMS which overrides any stated in the
        associated VMSTable entry. Typically it is used for giving the
        updated managed location of a mobile VMS which has recently been
        moved.
    :ivar vms_dynamic_characteristics:
    :ivar vms_fault:
    :ivar vms_extension:
    """
    vms_working: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vmsWorking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_message_sequencing_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "vmsMessageSequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_message: List[VmsMessageIndexVmsMessage] = field(
        default_factory=list,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    text_display_area_settings: Optional[TextDisplayAreaSettings] = field(
        default=None,
        metadata={
            "name": "textDisplayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pictogram_display_area_settings: List[VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings] = field(
        default_factory=list,
        metadata={
            "name": "pictogramDisplayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_location_override: Optional[Location] = field(
        default=None,
        metadata={
            "name": "vmsLocationOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    managed_logical_location_override: Optional[VmsManagedLogicalLocation] = field(
        default=None,
        metadata={
            "name": "managedLogicalLocationOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_dynamic_characteristics: Optional[VmsDynamicCharacteristics] = field(
        default=None,
        metadata={
            "name": "vmsDynamicCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_fault: List[VmsFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class AbnormalTraffic(TrafficElement):
    """
    A traffic condition which is not normal.

    :ivar abnormal_traffic_type: A characterization of the nature of
        abnormal traffic flow, i.e. specifically relating to the nature
        of the traffic movement.
    :ivar number_of_vehicles_waiting: The number of vehicles waiting in
        a queue.
    :ivar queue_length: The length of a queue or the average length of
        queues in separate lanes due to a situation.
    :ivar relative_traffic_flow: Assessment of the traffic flow
        conditions relative to normally expected conditions at this
        date/time.
    :ivar traffic_flow_characteristics: A characterization of the
        traffic flow.
    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar abnormal_traffic_extension:
    """
    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_vehicles_waiting: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehiclesWaiting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    queue_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "queueLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    relative_traffic_flow: Optional[RelativeTrafficFlowEnum] = field(
        default=None,
        metadata={
            "name": "relativeTrafficFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_flow_characteristics: Optional[TrafficFlowCharacteristicsEnum] = field(
        default=None,
        metadata={
            "name": "trafficFlowCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    abnormal_traffic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar total_number_of_people_involved: The total number of people
        that are involved.
    :ivar total_number_of_vehicles_involved: The total number of
        vehicles that are involved.
    :ivar vehicle_involved: The vehicle involved in the accident.
    :ivar group_of_vehicles_involved:
    :ivar group_of_people_involved:
    :ivar accident_extension:
    """
    accident_cause: Optional[AccidentCauseEnum] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accident_type: List[AccidentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_involved: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_vehicles_involved: List[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "activityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class CarParks(NonRoadEventInformation):
    """
    Provides information on the status of one or more car parks.

    :ivar car_park_configuration: The configuration/layout of a car
        park.
    :ivar car_park_identity: The identity of one or a group of car
        parks.
    :ivar car_park_occupancy: The percentage value of car parking spaces
        occupied.
    :ivar car_park_status: Indicates the status of one or more specified
        car parks.
    :ivar exit_rate: The rate at which vehicles are exiting the car
        park.
    :ivar fill_rate: The rate at which vehicles are entering the car
        park.
    :ivar number_of_vacant_parking_spaces: Indicates the number of
        vacant parking spaces available in a specified parking area.
    :ivar occupied_spaces: Number of currently occupied spaces.
    :ivar queuing_time: The current queuing time (duration) for entering
        the car park.
    :ivar total_capacity: Total number of car parking spaces.
    :ivar car_parks_extension:
    """
    car_park_configuration: Optional[CarParkConfigurationEnum] = field(
        default=None,
        metadata={
            "name": "carParkConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    car_park_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "carParkIdentity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    car_park_occupancy: Optional[float] = field(
        default=None,
        metadata={
            "name": "carParkOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    car_park_status: Optional[CarParkStatusEnum] = field(
        default=None,
        metadata={
            "name": "carParkStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exit_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    fill_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_vacant_parking_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVacantParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    occupied_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "occupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    queuing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "queuingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCapacity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    car_parks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "carParksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    driving_condition_type: Optional[DrivingConditionTypeEnum] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Equipment(ParkingEquipmentOrServiceFacility):
    """
    One type of equipment, that is available on the parking site.

    :ivar equipment_type: One type of equipment, that is available on
        the parking site.
    :ivar electric_charging:
    :ivar equipment_extension:
    """
    equipment_type: Optional[EquipmentTypeEnum] = field(
        default=None,
        metadata={
            "name": "equipmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    electric_charging: Optional[ElectricCharging] = field(
        default=None,
        metadata={
            "name": "electricCharging",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    equipment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "equipmentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    equipment_or_system_fault_type: Optional[EquipmentOrSystemFaultTypeEnum] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    faulty_equipment_or_system_type: Optional[EquipmentOrSystemTypeEnum] = field(
        default=None,
        metadata={
            "name": "faultyEquipmentOrSystemType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_system_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    compliance_option: Optional[ComplianceOptionEnum] = field(
        default=None,
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    applicable_for_traffic_direction: List[DirectionEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_traffic_type: List[TrafficTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    places_at_which_applicable: List[PlacesEnum] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    automatically_initiated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    mobility_of_obstruction: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfObstruction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class RoadOperatorServiceDisruption(NonRoadEventInformation):
    """
    Details of disruption to normal road operator services.

    :ivar road_operator_service_disruption_type: The type of road
        operator service which is disrupted.
    :ivar road_operator_service_disruption_extension:
    """
    road_operator_service_disruption_type: List[RoadOperatorServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOperatorServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class RoadsideServiceDisruption(NonRoadEventInformation):
    """
    Details of disruption to normal roadside services (e.g. specific services
    at a service area).

    :ivar roadside_service_disruption_type: The type of roadside service
        which is disrupted.
    :ivar roadside_service_disruption_extension:
    """
    roadside_service_disruption_type: List[RoadsideServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadsideServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    roadside_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class Roadworks(OperatorAction):
    """
    Highway maintenance, installation and construction activities that may
    potentially affect traffic operations.

    :ivar roadworks_duration: Indicates in general terms the expected
        duration of the roadworks.
    :ivar roadworks_scale: Indication of the scale of the roadworks in
        terms of the traffic disruption they are likely to cause.
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
    roadworks_duration: Optional[RoadworksDurationEnum] = field(
        default=None,
        metadata={
            "name": "roadworksDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    roadworks_scale: Optional[RoadworksScaleEnum] = field(
        default=None,
        metadata={
            "name": "roadworksScale",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    under_traffic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "underTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    urgent_roadworks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "urgentRoadworks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    mobility: Optional[Mobility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subjects: Optional[Subjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maintenance_vehicles: Optional[MaintenanceVehicles] = field(
        default=None,
        metadata={
            "name": "maintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    roadworks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ServiceFacility(ParkingEquipmentOrServiceFacility):
    """One type of service facility that is available on the parking site or
    located next to it.

    You can specify the number of this service facility type (e.g. 5
    restaurants) as well as the number of subitems (e.g. 200 restaurant
    places).

    :ivar service_facility_type: One type of service, that is available
        on the parking site.
    :ivar number_of_subitems: The quantity of sub items to this service
        facility type, e.g. the total number of restaurant places or
        fuel dispensers etc.
    :ivar distance_from_parking_site: If the service facility is not
        located on the parking site itself, its distance can be
        specified here in metres.
    :ivar service_facility_extension:
    """
    service_facility_type: Optional[ServiceFacilityTypeEnum] = field(
        default=None,
        metadata={
            "name": "serviceFacilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_subitems: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubitems",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_parking_site: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromParkingSite",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    service_facility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "serviceFacilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class SignSetting(OperatorAction):
    """
    Provides information on message signs and the information currently
    displayed.
    """
    vms_setting: Optional[VmsSetting] = field(
        default=None,
        metadata={
            "name": "vmsSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "signSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficViewRecord:
    """
    An identifiable instance of a single record within a traffic view which
    shall comprise at most one instance of each of the following:
    OperatorAction, TrafficElement, ElaboratedData and CCTVImages.

    :ivar record_sequence_number: A number identifying the sequence of
        the record within the set of records which comprise the traffic
        view.
    :ivar traffic_element:
    :ivar operator_action:
    :ivar elaborated_data:
    :ivar url_link:
    :ivar traffic_view_record_extension:
    :ivar id:
    """
    record_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "recordSequenceNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_element: Optional[TrafficElement] = field(
        default=None,
        metadata={
            "name": "trafficElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    operator_action: Optional[OperatorAction] = field(
        default=None,
        metadata={
            "name": "operatorAction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    elaborated_data: Optional[ElaboratedData] = field(
        default=None,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_view_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class TransitInformation(NonRoadEventInformation):
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    journey_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    journey_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "journeyReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    transit_service_information: Optional[TransitServiceInformationEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    transit_service_type: Optional[TransitServiceTypeEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scheduled_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "scheduledDepartureTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    transit_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "transitInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingRecordEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility:
    class Meta:
        name = "_ParkingRecordEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility"

    parking_equipment_or_service_facility: Optional[ParkingEquipmentOrServiceFacility] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_service_facility_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "equipmentOrServiceFacilityIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility:
    class Meta:
        name = "_ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility"

    parking_equipment_or_service_facility: Optional[ParkingEquipmentOrServiceFacility] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_service_facility_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "equipmentOrServiceFacilityIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VmsUnitVmsIndexVms:
    class Meta:
        name = "_VmsUnitVmsIndexVms"

    vms: Optional[Vms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    animal_presence_type: Optional[AnimalPresenceTypeEnum] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    authority_operation_type: Optional[AuthorityOperationTypeEnum] = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    authority_operation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    construction_work_type: Optional[ConstructionWorkTypeEnum] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    construction_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    disturbance_activity_type: Optional[DisturbanceActivityTypeEnum] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    disturbance_activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    environmental_obstruction_type: Optional[EnvironmentalObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    general_instruction_to_road_users_type: Optional[GeneralInstructionToRoadUsersTypeEnum] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    general_message_to_road_users: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "generalMessageToRoadUsers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    general_instruction_or_message_to_road_users_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalInstructionOrMessageToRoadUsersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    general_network_management_type: Optional[GeneralNetworkManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_manually_directed_by: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "trafficManuallyDirectedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    general_network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    obstruction_type: List[ObstructionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    infrastructure_damage_type: Optional[InfrastructureDamageTypeEnum] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    infrastructure_damage_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class LinearTrafficView:
    """
    An identifiable instance of a linear traffic view at a single point in time
    relating to a linear section of road, comprising one or more traffic view
    records.

    :ivar linear_predefined_location_reference: A reference to a
        versioned predefined location which is of type linear.
    :ivar traffic_view_record:
    :ivar linear_traffic_view_extension:
    :ivar id:
    """
    linear_predefined_location_reference: Optional[PredefinedLocationVersionedReference] = field(
        default=None,
        metadata={
            "name": "linearPredefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_view_record: List[TrafficViewRecord] = field(
        default_factory=list,
        metadata={
            "name": "trafficViewRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    linear_traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearTrafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class MaintenanceWorks(Roadworks):
    """
    Roadworks involving the maintenance or installation of infrastructure.

    :ivar road_maintenance_type: The type of road maintenance or
        installation work at the specified location.
    :ivar maintenance_works_extension:
    """
    road_maintenance_type: List[RoadMaintenanceTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    maintenance_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSpaceBasics:
    """
    Common properties of parking spaces and groups of parking spaces.

    :ivar parking_space_or_group_identifier: A public identifier or
        short description for the parking space or group of parking
        spaces, for example "6D" or "Truck parking west".
    :ivar parking_floor_or_level: The floor or level of the parking site
        on which the assigned parking spaces are located.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar parking_space_accessibility: Further easements for handicapped
        people related to this parking space or this group of parking
        spaces.
    :ivar parking_space_physics: Specifies 'driveThrough' or 'openAir'
        for the parking space or the group of parking spaces.
    :ivar parking_mode: The arrangement of the parking space or the
        group of parking spaces in relation to the road.
    :ivar parking_reservation: Indication of whether a parking
        reservation service is available and/or mandatory.
    :ivar maximum_parking_duration: The maximum parking duration for a
        parking record, a parking space or a group of parking spaces
        (e.g. to avoid overnight parking).
    :ivar distance_from_primary_road: Specifies the distance from the
        primary road in metres. Especially useful, if parking is located
        on a smaller type of road.
    :ivar parking_occupany_detection_type: Type of parking occupancy
        detection for a parking record, a parking space or a group of
        parking spaces, if any (balancing, single slot, ...  ).
    :ivar parking_security: Specifies security measures related to the
        parking site or particular spaces.
    :ivar dedicated_access:
    :ivar only_assigned_parking: Parking is only allowed for the
        assignment given in this class, i.e. other assignments are not
        allowed. By using this role, it is not allowed to use
        'assignedParkingAmongOthers' and 'prohibitedParking' for the
        same type of attributes.
    :ivar assigned_parking_among_others: Assignments for parking. Other
        assignments are allowed as well, i.e. the parking spaces are
        convenient for this kind of assignment.
    :ivar prohibited_parking: Parking is not allowed for the given
        assignment.
    :ivar parking_equipment_or_service_facility: Equiment, services and
        szenarios, which are directly related to the assigned parking
        space or parking space group. Note that the infrastructure index
        must be unique with respect to the Parking class' infrastrucure
        indeces
    :ivar parking_usage_scenario:
    :ivar parking_space_basics_extension:
    """
    parking_space_or_group_identifier: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingSpaceOrGroupIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_floor_or_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingFloorOrLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accessibility: List[AccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_accessibility: List[ParkingSpaceAccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpaceAccessibility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_physics: List[ParkingSpacePhysicsEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpacePhysics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        }
    )
    parking_mode: Optional[ParkingModeEnum] = field(
        default=None,
        metadata={
            "name": "parkingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_reservation: Optional[ReservationTypeEnum] = field(
        default=None,
        metadata={
            "name": "parkingReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_parking_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumParkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_primary_road: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromPrimaryRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupany_detection_type: List[OccupancyDetectionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingOccupanyDetectionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_security: List[ParkingSecurityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dedicated_access: List[DedicatedAccess] = field(
        default_factory=list,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    only_assigned_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "onlyAssignedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    assigned_parking_among_others: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "assignedParkingAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    prohibited_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "prohibitedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility: List[ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_usage_scenario: List[ParkingSpaceBasicsScenarioIndexParkingUsageScenario] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_basics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar poor_environment_conditions_extension:
    """
    poor_environment_type: List[PoorEnvironmentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    pollution: Optional[Pollution] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class PublicEvent(Activity):
    """
    Organised public event which could disrupt traffic.

    :ivar public_event_type: Type of public event which could disrupt
        traffic.
    :ivar public_event_extension:
    """
    public_event_type: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    public_event_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "publicEventExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    :ivar entry: The specified entry on to another road at which the
        alternative route commences.
    :ivar exit: The specified exit from the normal route/road at which
        the alternative route commences.
    :ivar road_or_junction_number: The intersecting road or the junction
        at which the alternative route commences.
    :ivar alternative_route: The definition of the alternative route
        (rerouting) specified as an ordered set of locations (itinerary)
        which may be specific to one or more defined destinations.
    :ivar rerouting_management_extension:
    """
    rerouting_management_type: List[ReroutingManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    rerouting_itinerary_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reroutingItineraryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    signed_rerouting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "signedRerouting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    entry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    exit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    road_or_junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadOrJunctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    alternative_route: List[Itinerary] = field(
        default_factory=list,
        metadata={
            "name": "alternativeRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    rerouting_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "reroutingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class RoadConditions(Conditions):
    """Conditions of the road surface which may affect driving conditions.

    These may be related to the weather (e.g. ice, snow etc.) or to
    other conditions (e.g. oil, mud, leaves etc. on the road)
    """
    road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    road_or_carriageway_or_lane_management_type: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    minimum_car_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumCarOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_or_carriageway_or_lane_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    speed_management_type: Optional[SpeedManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    temporary_speed_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "temporarySpeedLimit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    speed_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VehicleObstruction(Obstruction):
    """
    An obstruction on the road caused by one or more vehicles.

    :ivar vehicle_obstruction_type: Characterization of an obstruction
        on the road caused by one or more vehicles.
    :ivar obstructing_vehicle: The obstructing vehicle.
    :ivar vehicle_obstruction_extension:
    """
    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class VmsUnit(VmsSetting):
    """
    Status of a VMS unit which may control one or more variable message signs
    on a single gantry or on different gantries.

    :ivar vms_unit_table_reference: A reference to a versioned VMS Unit
        table.
    :ivar vms_unit_reference: A reference to a versioned VMS unit record
        in a VMS Unit table which defines the characteristics of the VMS
        unit.
    :ivar vms:
    :ivar vms_unit_fault:
    :ivar vms_unit_extension:
    """
    vms_unit_table_reference: Optional[VmsUnitTableVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_unit_reference: Optional[VmsUnitRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsUnitReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms: List[VmsUnitVmsIndexVms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_fault: List[VmsUnitFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
    winter_equipment_management_type: Optional[WinterEquipmentManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class NonWeatherRelatedRoadConditions(RoadConditions):
    """
    Road surface conditions that are not related to the weather but which may
    affect driving conditions.

    :ivar non_weather_related_road_condition_type: The type of road
        conditions which are not related to the weather.
    :ivar non_weather_related_road_conditions_extension:
    """
    non_weather_related_road_condition_type: List[NonWeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonWeatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSpace2(ParkingSpaceBasics):
    """A single parking space.

    It is possible to define the same parking space more than once with
    different properties, e.g. when there is a different parking
    assignment for different times.

    :ivar identical_to_parking_space: Points to another instance of
        'ParkingSpace', which is identical from a local point of view
        (i.e. which is the same parking space). To be used when defining
        mixed parking areas (with using different time slots).
    :ivar location:
    :ivar parking_space_dimension: Dimension of the parking space (not
        all dimension attributes need to be provided). If the parking
        space is not rectangular, its dimension is specified as the
        smallest rectangle fitting inside its shape.
    :ivar parking_space_extension:
    """
    class Meta:
        name = "ParkingSpace"

    identical_to_parking_space: List[str] = field(
        default_factory=list,
        metadata={
            "name": "identicalToParkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "parkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSpaceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class TrafficView:
    """
    An identifiable instance of a traffic view at a single point in time
    relating to a predefined location set, comprising one or more linear
    traffic views each of which comprise one or more traffic view records.

    :ivar traffic_view_time: The time to which the traffic view relates,
        i.e. the instance in time at which the traffic view was taken
        (comparable to taking a photograph).
    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar linear_traffic_view:
    :ivar traffic_view_extension:
    :ivar id:
    """
    traffic_view_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "trafficViewTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    predefined_non_ordered_location_group_reference: Optional[PredefinedNonOrderedLocationGroupVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    linear_traffic_view: List[LinearTrafficView] = field(
        default_factory=list,
        metadata={
            "name": "linearTrafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class VmsPublication(PayloadPublication):
    """
    A publication containing the current status and settings of one or more VMS
    units, each unit controlling one or more individual variable message signs.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_unit: List[VmsUnit] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    vms_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class WeatherRelatedRoadConditions(RoadConditions):
    """
    Road surface conditions that are related to the weather which may affect
    the driving conditions, such as ice, snow or water.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar weather_related_road_conditions_extension:
    """
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfParkingSpaces1:
    class Meta:
        name = "_GroupOfParkingSpaces"

    parking_space_basics: Optional[ParkingSpaceBasics] = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    group_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "groupIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingSpace1:
    class Meta:
        name = "_ParkingSpace"

    parking_space_basics: Optional[ParkingSpaceBasics] = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParkingRecord:
    """A container for static parking information.

    Must be specialised as a parking site or as a group of parking
    sites.

    :ivar parking_name: Name of the parking, i.e. name of the parking
        site or the group of parking sites.
    :ivar parking_alias: Alternative name for the parking site or the
        group of parking sites.
    :ivar parking_description: Additional description of the parking
        site or the group of parking sites.
    :ivar parking_record_version_time: Date/time that this version of
        the parking record was defined.
    :ivar parking_number_of_spaces: Number of parking spaces (attribute
        is used for a parking record as well as for a group of parking
        spaces).
    :ivar parking_principal_number_of_spaces: Number of parking spaces
        that are not assigned for a particular purpose.
    :ivar maximum_parking_duration: The maximum parking duration for a
        parking record, a parking space or a group of parking spaces
        (e.g. to avoid overnight parking).
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar parking_occupany_detection_type: Type of parking occupancy
        detection for a parking record, a parking space or a group of
        parking spaces, if any (balancing, single slot, ...  ).
    :ivar emergency_contact: Contact to be used in times of emergencies.
    :ivar owner: Contact details of the owner of the parking facility.
    :ivar responisble_authority: Contact details of the responsible
        authority of the parking facility or parking area.
    :ivar security_service: Contact details of one or more security
        services of the parking facility.
    :ivar operator: Contact details of the operator of the parking
        facility.
    :ivar service_partner: Contact details of a service partner of the
        parking record, i.e. the person or organisation that should be
        contacted to provide servicing or support services for equipment
        at the parking.
    :ivar parking_vms:
    :ivar parking_location: The location(s) or the extent of the
        parking. Examples could be an Area for parking area, a Point
        location for an urban parking facility or a Linear for on street
        parking.
    :ivar parking_route:
    :ivar parking_colour: A colour, which can be assigned to the
        parking. Often used with parking areas for a quick visual
        distinction.
    :ivar only_assigned_parking: Parking is only allowed for the
        assignment given in this class, i.e. other assignments are not
        allowed. By using this role, it is not allowed to use
        'assignedParkingAmongOthers' and 'prohibitedParking' for the
        same type of attributes.
    :ivar assigned_parking_among_others: Assignments for parking. Other
        assignments are allowed as well, i.e. the parking spaces are
        convenient for this kind of assignment.
    :ivar prohibited_parking: Parking is not allowed for the given
        assignment.
    :ivar tariffs_and_payment:
    :ivar parking_equipment_or_service_facility:
    :ivar parking_space: Properties of a single parking space. This
        aggregation may only be used with the "ParkingSpace"
        specialisation.
    :ivar group_of_parking_spaces: Properties for a group of parking
        spaces. Usually, all properties specified have to be the same
        for all spaces included. This aggregation may only be used with
        the "GroupOfParkingSpaces" specialisation.
    :ivar parking_thresholds:
    :ivar permits_and_prohibitions:
    :ivar emergency_assembly_point: Some geographic location(s) within
        or nearby the parking, where people have to meet in case of a
        fire, for example.
    :ivar entire_area: An underlaying area this parking record is
        located in or belongs to. Examples are a state, province, truck
        parking area etc. A name can be specified in the area structure.
    :ivar parking_record_dimension: Dimension either of the building or
        a virtual rectangle encapsulating the parking site(s). Use
        'dimensionUsableArea' to define the total space available for
        parking. Use 'dimensionHeight' only for a building, not for the
        restriction of vehicles.
    :ivar parking_record_extension:
    :ivar id:
    :ivar version:
    """
    parking_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_alias: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "parkingAlias",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_principal_number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingPrincipalNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_parking_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumParkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    photo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupany_detection_type: List[OccupancyDetectionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingOccupanyDetectionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    emergency_contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "emergencyContact",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    owner: List[Contact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    responisble_authority: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "responisbleAuthority",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    security_service: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "securityService",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    operator: List[Contact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    service_partner: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "servicePartner",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vms: List[ParkingVMS] = field(
        default_factory=list,
        metadata={
            "name": "parkingVMS",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "parkingLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_route: List[ParkingRoute] = field(
        default_factory=list,
        metadata={
            "name": "parkingRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_colour: Optional[RGBColour] = field(
        default=None,
        metadata={
            "name": "parkingColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    only_assigned_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "onlyAssignedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    assigned_parking_among_others: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "assignedParkingAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    prohibited_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "prohibitedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tariffs_and_payment: Optional[TariffsAndPayment] = field(
        default=None,
        metadata={
            "name": "tariffsAndPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility: List[ParkingRecordEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space: List[ParkingSpace1] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_spaces: List[GroupOfParkingSpaces1] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_thresholds: Optional[ParkingThresholds] = field(
        default=None,
        metadata={
            "name": "parkingThresholds",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    permits_and_prohibitions: List[PermitsAndProhibitions] = field(
        default_factory=list,
        metadata={
            "name": "permitsAndProhibitions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    emergency_assembly_point: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "emergencyAssemblyPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    entire_area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "entireArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "parkingRecordDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class TrafficViewPublication(PayloadPublication):
    """
    A publication containing one or more traffic views.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_view: List[TrafficView] = field(
        default_factory=list,
        metadata={
            "name": "trafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    traffic_view_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GroupOfParkingSpacesParkingSpaceIndexParkingSpace:
    class Meta:
        name = "_GroupOfParkingSpacesParkingSpaceIndexParkingSpace"

    parking_space: Optional[ParkingSpace2] = field(
        default=None,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GroupOfParkingSpaces2(ParkingSpaceBasics):
    """A group of parking spaces.

    All information provided has to be identical for all places in this
    group. Can also be used just to give the number of lorry parkings,
    for example. 'GroupOfParkingSpaces' may be multiple defined or
    include each other.

    :ivar parking_number_of_spaces: Number of parking spaces (attribute
        is used for a parking record as well as for a group of parking
        spaces).
    :ivar parking_type_of_group: Defines the type of this group
        specification.
    :ivar identical_to_group: Points to another instance of
        'GroupOfParkingSpaces', which is identical from a local point of
        view. To be used when defining mixed parking areas with
        different time slots.
    :ivar real_subset_of_group: Points to another instance of
        'GroupOfParkingSpaces', which is a real superset from a local
        point of view. To be used when defining mixed parking areas with
        different time slots.
    :ivar minimum_parking_space_dimension: Lower dimension boundaries
        for all spaces within the group. Note that there must not exist
        a space with this dimension, but each space's dimension values
        must be equal or higher.
    :ivar dimension_of_group: Dimension of a virtual rectangle
        encapsulating the group of parking spaces. Use
        'dimensionUsableArea' to define the total space available for
        parking within this group. Do not use 'dimensionHeight'.
    :ivar maximum_parking_space_dimension: Dimension of the largest
        space within this group (i.e. there must be at least one space
        of this dimension). If the comparison of dimension values is not
        unique, the length is decisive.
    :ivar parking_space:
    :ivar group_of_locations:
    :ivar group_of_parking_spaces_extension:
    """
    class Meta:
        name = "GroupOfParkingSpaces"

    parking_number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_type_of_group: Optional[ParkingTypeOfGroup] = field(
        default=None,
        metadata={
            "name": "parkingTypeOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    identical_to_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "identicalToGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    real_subset_of_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "realSubsetOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    minimum_parking_space_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "minimumParkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dimension_of_group: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "dimensionOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_parking_space_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "maximumParkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space: List[GroupOfParkingSpacesParkingSpaceIndexParkingSpace] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_spaces_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingSite(ParkingRecord):
    """A record containing static details of a parking site.

    Must be specialised as an 'Urban-' or 'InterUrbanParkingSite' or a
    'SpecialLocationParkingSite'.

    :ivar parking_reservation: Indication of whether a parking
        reservation service is available and/or mandatory.
    :ivar parking_layout: Layout of the parking site.
    :ivar highest_floor: Highest floor of the parking site. It is
        possible to have negative values here in case it is underground
        only. Must be higher or equal than 'lowestFloor'.
    :ivar lowest_floor: Lowest floor of the parking site. Positive
        values may apply in case it is over ground only. Must be lower
        or equal than 'highestFloor'.
    :ivar temporary_parking: Indicates that the parking site is on a
        temporary basis. It might close permanently within short notice
        or might only be partial equipped. The physical parking
        possibilities might be provisional, too.
    :ivar parking_site_address: Information about the parking site
        itself (address etc.). The 'GroupOfLocations' association must
        not be used for this role.
    :ivar reservation_service: Reservation service (for end users). It
        is recommended to give URL and telephone.
    :ivar parking_usage_scenario:
    :ivar opening_times:
    :ivar parking_access: An exit from the parking facility onto the
        road network from any parking space unless separate exits are
        specified for assigned parking spaces, in which case this is an
        exit from only the principal parking spaces.
    :ivar parking_standards_and_security:
    :ivar parking_site_extension:
    """
    parking_reservation: Optional[ReservationTypeEnum] = field(
        default=None,
        metadata={
            "name": "parkingReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_layout: List[ParkingLayoutEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingLayout",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    highest_floor: Optional[int] = field(
        default=None,
        metadata={
            "name": "highestFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    lowest_floor: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowestFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    temporary_parking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "temporaryParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_address: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    reservation_service: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "reservationService",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_usage_scenario: List[ParkingSiteScenarioIndexParkingUsageScenario] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    opening_times: Optional[OpeningTimes] = field(
        default=None,
        metadata={
            "name": "openingTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_access: List[ParkingAccess] = field(
        default_factory=list,
        metadata={
            "name": "parkingAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_standards_and_security: Optional[ParkingStandardsAndSecurity] = field(
        default=None,
        metadata={
            "name": "parkingStandardsAndSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingTable:
    """
    A collection of parking records, which can be parking sites or groups of
    parking sites.

    :ivar parking_table_name: The name of the parking table.
    :ivar parking_table_version_time: The date/time that this version of
        the parking table was defined by the supplier. The identity and
        version of the table are defined by the class stereotype
        implementation.
    :ivar parking_record:
    :ivar parking_table_extension:
    :ivar id:
    :ivar version:
    """
    parking_table_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingTableName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_table_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingTableVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_record: List[ParkingRecord] = field(
        default_factory=list,
        metadata={
            "name": "parkingRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    parking_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
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
class GroupOfParkingSites(ParkingRecord):
    """A logical composition of parking sites with aggregated properties (e.g.
    number of spaces).

    Examples: Urban parking area "West" or all truck parkings along a motorway. The included parking sites may -but must not- be specified as subcomponents.

    :ivar group_of_parking_sites_type: The type of this group of parking
        sites.
    :ivar parking_site_by_reference: Parking sites of this collection
        defined by reference.
    :ivar parking_site:
    :ivar group_of_parking_sites_extension:
    """
    group_of_parking_sites_type: Optional[GroupOfParkingSitesTypeEnum] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site_by_reference: List[ParkingRecordVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteByReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_site: List[ParkingSite] = field(
        default_factory=list,
        metadata={
            "name": "parkingSite",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_parking_sites_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class InterUrbanParkingSite(ParkingSite):
    """
    A parking site in an interurban context.

    :ivar inter_urban_parking_site_location: Defines whether the
        interurban parking site is located in or nearby a motorway
        context, is a layby or on-street parking.
    :ivar inter_urban_parking_site_extension:
    """
    inter_urban_parking_site_location: Optional[InterUrbanParkingSiteLocationEnum] = field(
        default=None,
        metadata={
            "name": "interUrbanParkingSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    inter_urban_parking_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "interUrbanParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class ParkingTablePublication:
    """
    A publication defining one or more tables that have entries of parking
    sites or groups of them, located in an urban or interurban context.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_table: List[ParkingTable] = field(
        default_factory=list,
        metadata={
            "name": "parkingTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )


@dataclass
class SpecialLocationParkingSite(ParkingSite):
    """
    A parking site which is located at a special location, often associated
    with some building.

    :ivar parking_special_location: The special location of the parking
        site.
    :ivar parking_other_special_location: A special location not
        available in the enumeration. Use literal 'other' in this case.
    :ivar special_location_parking_site_extension:
    """
    parking_special_location: Optional[ParkingSpecialLocationEnum] = field(
        default=None,
        metadata={
            "name": "parkingSpecialLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_other_special_location: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingOtherSpecialLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    special_location_parking_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "specialLocationParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class UrbanParkingSite(ParkingSite):
    """
    A parking site in an urban context.

    :ivar urban_parking_site_type: The type of urban parking site.
    :ivar parking_zone: Name or identifier of a parking zone this
        parking site belongs to. To be filled with the string value
        'True', if there is a parking zone with unknown name.
    :ivar urban_parking_site_extension:
    """
    urban_parking_site_type: Optional[UrbanParkingSiteTypeEnum] = field(
        default=None,
        metadata={
            "name": "urbanParkingSiteType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_zone: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingZone",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    urban_parking_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "urbanParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )


@dataclass
class GenericPublicationExtensionType:
    class Meta:
        name = "_GenericPublicationExtensionType"

    parking_table_publication: Optional[ParkingTablePublication] = field(
        default=None,
        metadata={
            "name": "parkingTablePublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_publication: Optional[ParkingStatusPublication] = field(
        default=None,
        metadata={
            "name": "parkingStatusPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vehicles_publication: Optional[ParkingVehiclesPublication] = field(
        default=None,
        metadata={
            "name": "parkingVehiclesPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class GenericPublication(PayloadPublication):
    """
    A publication used to make level B extensions at the publication level.

    :ivar generic_publication_name: The name of the generic publication.
    :ivar generic_publication_extension:
    """
    generic_publication_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericPublicationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_publication_extension: Optional[GenericPublicationExtensionType] = field(
        default=None,
        metadata={
            "name": "genericPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
