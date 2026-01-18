from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.file_finishing_info_1 import FileFinishingInfo1
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_stay import HotelStay

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class HotelCancelReq(BaseReq1):
    """
    Cancel request for a hotel booking.

    Given a provider code and a provider locator code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    hotel_property: None | HotelProperty = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    hotel_stay: None | HotelStay = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    file_finishing_info: None | FileFinishingInfo1 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    supplier_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
        },
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: str = field(
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
