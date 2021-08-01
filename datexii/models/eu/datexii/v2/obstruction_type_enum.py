from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
