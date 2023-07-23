from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.hotel_search_location import HotelSearchLocation
from travelport.models.hotel_search_modifiers import HotelSearchModifiers
from travelport.models.hotel_stay import HotelStay
from travelport.models.point_of_sale_1 import PointOfSale1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BaseHotelSearchReq(BaseSearchReq1):
    """
    Base hotel Search Request.

    Parameters
    ----------
    hotel_search_location
    hotel_search_modifiers
    hotel_stay
    point_of_sale
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    """
    hotel_search_location: None | HotelSearchLocation = field(
        default=None,
        metadata={
            "name": "HotelSearchLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_search_modifiers: None | HotelSearchModifiers = field(
        default=None,
        metadata={
            "name": "HotelSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_stay: None | HotelStay = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    policy_reference: None | str = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
