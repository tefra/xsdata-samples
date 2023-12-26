from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vendor import Vendor

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleLocationDetailReq(BaseReq1):
    """
    Parameters
    ----------
    vendor
    vehicle_date_location
    point_of_sale
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: None | Vendor = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "required": True,
        },
    )
    vehicle_date_location: None | VehicleDateLocation = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "required": True,
        },
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
