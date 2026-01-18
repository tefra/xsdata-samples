from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_occupancy import ParkingOccupancy

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfParkingSpacesStatus(ParkingOccupancy):
    """
    The status of the assigned parking spaces in the specified parking
    site, i.e. the status of those spaces assigned for particular types of
    person or vehicle and/or for specific duration types (e.g. short stay).

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

    group_declaration_valid_now: bool | None = field(
        default=None,
        metadata={
            "name": "groupDeclarationValidNow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_spaces_closed: bool | None = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesClosed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_spaces_status_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
