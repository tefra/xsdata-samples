from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_type import HotelType
from travelport.models.media_item_1 import MediaItem1
from travelport.models.property_description import PropertyDescription
from travelport.models.rate_info import RateInfo
from travelport.models.type_result_message_1 import TypeResultMessage1
from travelport.models.vendor_location_1 import VendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSearchResult:
    """
    A single hotel availabilty result.

    Parameters
    ----------
    vendor_location
    hotel_property
        The hotel property. Multiple property can only be supported with GDS
        property aggrigation.
    hotel_search_error
    corporate_discount_id
    rate_info
    media_item
    hotel_type
        Supported Providers:1P
    property_description
        Hotel Property description. Maximum of 100 words returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    vendor_location: list[VendorLocation1] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_property: list[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    hotel_search_error: list[HotelSearchResult.HotelSearchError] = field(
        default_factory=list,
        metadata={
            "name": "HotelSearchError",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    corporate_discount_id: list[CorporateDiscountId1] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    rate_info: list[RateInfo] = field(
        default_factory=list,
        metadata={
            "name": "RateInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    media_item: None | MediaItem1 = field(
        default=None,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_type: None | HotelType = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        }
    )
    property_description: None | PropertyDescription = field(
        default=None,
        metadata={
            "name": "PropertyDescription",
            "type": "Element",
        }
    )

    @dataclass
    class HotelSearchError(TypeResultMessage1):
        """
        Parameters
        ----------
        rate_supplier
            Indicates the supplier of the rate.
        """
        rate_supplier: None | str = field(
            default=None,
            metadata={
                "name": "RateSupplier",
                "type": "Attribute",
                "max_length": 64,
            }
        )
