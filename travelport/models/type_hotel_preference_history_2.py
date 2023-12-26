from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_base_preference_history_2 import (
    TypeBasePreferenceHistory2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeHotelPreferenceHistory2(TypeBasePreferenceHistory2):
    """
    Defines a hotel preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    Parameters
    ----------
    bed_type_misc_travel
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType'
    bed_type_ref_category
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType'
    check_in_start_date
    check_in_end_date
    corporate_discount_number
    max_room_rate_amount
    multi_level_rate_code
    property_id
    rate_code
    smoking_room
    special_request_misc_travel
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType', Util:
        ReferenceDataRetrieveReq, TypeCode VehicleMiscType.
    special_request_ref_category
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType', Util:
        ReferenceDataRetrieveReq, TypeCode VehicleMiscType.
    """

    class Meta:
        name = "typeHotelPreferenceHistory"

    bed_type_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "BedTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    bed_type_ref_category: None | str = field(
        default=None,
        metadata={
            "name": "BedTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    check_in_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "CheckInStartDate",
            "type": "Attribute",
        },
    )
    check_in_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "CheckInEndDate",
            "type": "Attribute",
        },
    )
    corporate_discount_number: None | str = field(
        default=None,
        metadata={
            "name": "CorporateDiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    max_room_rate_amount: None | str = field(
        default=None,
        metadata={
            "name": "MaxRoomRateAmount",
            "type": "Attribute",
        },
    )
    multi_level_rate_code: None | str = field(
        default=None,
        metadata={
            "name": "MultiLevelRateCode",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    property_id: None | str = field(
        default=None,
        metadata={
            "name": "PropertyID",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    rate_code: None | str = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    smoking_room: None | bool = field(
        default=None,
        metadata={
            "name": "SmokingRoom",
            "type": "Attribute",
        },
    )
    special_request_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "SpecialRequestMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    special_request_ref_category: None | str = field(
        default=None,
        metadata={
            "name": "SpecialRequestRefCategory",
            "type": "Attribute",
            "max_length": 3,
        },
    )
