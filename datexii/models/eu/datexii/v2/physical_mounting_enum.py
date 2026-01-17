from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
