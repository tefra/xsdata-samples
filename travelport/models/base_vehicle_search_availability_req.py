from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vehicle_search_modifiers import VehicleSearchModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class BaseVehicleSearchAvailabilityReq(BaseSearchReq1):
    """
    Base request to search for vehicle availability.
    """

    vehicle_date_location: None | VehicleDateLocation = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "required": True,
        },
    )
    vehicle_search_modifiers: None | VehicleSearchModifiers = field(
        default=None,
        metadata={
            "name": "VehicleSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
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
