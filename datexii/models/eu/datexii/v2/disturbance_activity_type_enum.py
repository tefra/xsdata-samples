from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
