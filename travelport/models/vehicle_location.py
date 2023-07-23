from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.coordinate_location_1 import CoordinateLocation1
from travelport.models.distance_1 import Distance1
from travelport.models.location_information import LocationInformation
from travelport.models.vendor_location_1 import VendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleLocation:
    """
    The information for a rental car location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_location: None | VendorLocation1 = field(
        default=None,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    distance: None | Distance1 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    coordinate_location: None | CoordinateLocation1 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    location_information: None | LocationInformation = field(
        default=None,
        metadata={
            "name": "LocationInformation",
            "type": "Element",
            "required": True,
        }
    )
