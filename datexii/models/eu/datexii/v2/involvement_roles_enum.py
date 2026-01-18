from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


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
