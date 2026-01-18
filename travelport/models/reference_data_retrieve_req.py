from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.reference_data_search_modifiers import (
    ReferenceDataSearchModifiers,
)
from travelport.models.request_reference_data_item import (
    RequestReferenceDataItem,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class ReferenceDataRetrieveReq(BaseReq1):
    """
    Request to retrieve code, name and description for a specific reference
    data type.

    Parameters
    ----------
    reference_data_search_modifiers
    request_reference_data_item
    type_code
        The code of the reference data type. Valid values are 'PaymentType',
        'PaymentFormatType', 'MerchandisingOfferType', 'HotelTaxType',
        'HotelAmenities','Airport','City','Country','CityAirport','BusinessType','Currency','PosChannel','StateProvince','SupplierType','RoleCategoryType','ResourceCategoryType','PaymentType','EmailType','HotelRateCategory','FulfillmentType','HotelRoomViewType',
        'HotelMealPlans' , 'GeoPoliticalAreaType', 'AirAndRailMiscType',
        'AirAndRailSupplierType', 'HotelMiscType' , 'HotelSupplierType' ,
        'VehicleMiscType' , 'VehicleSupplierType' ,
        'AccountingReferenceType' , 'TRMLocation' , 'Title' ,
        'PassengerTypeCode' , 'Gender' , 'PostalAddressType' ,
        'AccountingRemarkType' , 'VehicleSpecialEquipment',
        'ReferencePointSearch', 'RailStationLocation', 'RailAccommodation',
        and 'RailDiscountLoyalty'.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_search_modifiers: None | ReferenceDataSearchModifiers = (
        field(
            default=None,
            metadata={
                "name": "ReferenceDataSearchModifiers",
                "type": "Element",
            },
        )
    )
    request_reference_data_item: None | RequestReferenceDataItem = field(
        default=None,
        metadata={
            "name": "RequestReferenceDataItem",
            "type": "Element",
        },
    )
    type_code: str = field(
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
