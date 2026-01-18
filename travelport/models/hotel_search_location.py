from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.coordinate_location_1 import CoordinateLocation1
from travelport.models.distance_1 import Distance1
from travelport.models.hotel_location import HotelLocation
from travelport.models.type_hotel_reference_point import (
    TypeHotelReferencePoint,
)
from travelport.models.type_structured_address_1 import TypeStructuredAddress1
from travelport.models.vendor_location_1 import VendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelSearchLocation:
    """
    Location information for the hotel.

    Parameters
    ----------
    hotel_location
        Date and Location information for the Hotel.
    vendor_location
    hotel_address
        Search by address or postal code.  Applicable for 1G, 1V, 1P
    reference_point
        Search for hotels near a reference point. HotelLocation/Location is
        mandatory for aggregated scenario if ReferencePoint is used.
        Applicable for 1G,1V,1P.  Country/State are only applicable for 1P
    coordinate_location
        Search using latitude and longitude.  Applicable for 1G, 1V only.
        Not applicable for HotelSuperShopper
    distance
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_location: None | HotelLocation = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Element",
        },
    )
    vendor_location: list[VendorLocation1] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    hotel_address: None | TypeStructuredAddress1 = field(
        default=None,
        metadata={
            "name": "HotelAddress",
            "type": "Element",
        },
    )
    reference_point: None | TypeHotelReferencePoint = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
        },
    )
    coordinate_location: None | CoordinateLocation1 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    distance: None | Distance1 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
