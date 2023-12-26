from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
