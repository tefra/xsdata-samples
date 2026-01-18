from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_route_details_versioned_reference import (
    ParkingRouteDetailsVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRouteStatus:
    """
    The status of a parking route (active/inactive) defined in the static
    part of the model.

    :ivar parking_route_reference: A reference to a parking route.
    :ivar parking_route_active: Defines if this parking route is
        currently active or not.
    :ivar parking_route_status_extension:
    """

    parking_route_reference: ParkingRouteDetailsVersionedReference | None = field(
        default=None,
        metadata={
            "name": "parkingRouteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_route_active: bool | None = field(
        default=None,
        metadata={
            "name": "parkingRouteActive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_route_status_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingRouteStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
