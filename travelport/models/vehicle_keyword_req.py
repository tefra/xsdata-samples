from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.keyword_1 import Keyword1
from travelport.models.type_pickup_date_location import TypePickupDateLocation
from travelport.models.vendor import Vendor

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleKeywordReq(BaseSearchReq1):
    """
    Used to request a list of keywords or specific keyword information for a car
    vendor.

    Parameters
    ----------
    vendor
    pickup_date_location
        The date and location for which a list of vendors is requested.
    keyword
        Used to request specific keyword details
    keyword_list
        When true, a list of keywords should be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: None | Vendor = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "required": True,
        }
    )
    pickup_date_location: None | TypePickupDateLocation = field(
        default=None,
        metadata={
            "name": "PickupDateLocation",
            "type": "Element",
            "required": True,
        }
    )
    keyword: list[Keyword1] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 3,
        }
    )
    keyword_list: None | bool = field(
        default=None,
        metadata={
            "name": "KeywordList",
            "type": "Attribute",
        }
    )
