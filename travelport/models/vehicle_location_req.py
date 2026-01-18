from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.reference_point_1 import ReferencePoint1
from travelport.models.type_pickup_date_location import TypePickupDateLocation
from travelport.models.type_vehicle_search_distance import (
    TypeVehicleSearchDistance,
)
from travelport.models.vendor import Vendor

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleLocationReq(BaseReq1):
    """
    Used to request a list of vendors for a location (airport or city
    code).

    Parameters
    ----------
    vendor
    pickup_date_location
        The date and location for which a list of vendors is requested.
    reference_point
        Search Car by reference point
    search_distance
        Distance from search location. Providers: 1g/1v
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: list[Vendor] = field(
        default_factory=list,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    pickup_date_location: TypePickupDateLocation = field(
        metadata={
            "name": "PickupDateLocation",
            "type": "Element",
            "required": True,
        }
    )
    reference_point: None | ReferencePoint1 = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    search_distance: None | TypeVehicleSearchDistance = field(
        default=None,
        metadata={
            "name": "SearchDistance",
            "type": "Element",
        },
    )
    policy_reference: None | str = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
