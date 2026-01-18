from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
