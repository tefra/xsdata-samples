from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_route import ParkingRoute
from datexii.models.eu.datexii.v2.parking_route_details_versioned_reference import (
    ParkingRouteDetailsVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRouteByReference(ParkingRoute):
    """
    A route defined by a reference to an earlier specified route.

    :ivar parking_route_reference: A reference to a parking route.
    :ivar parking_route_by_reference_extension:
    """

    parking_route_reference: Optional[
        ParkingRouteDetailsVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "parkingRouteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_route_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRouteByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
