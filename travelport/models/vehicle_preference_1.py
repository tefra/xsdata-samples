from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_base_preference_1 import TypeBasePreference1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class VehiclePreference1(TypeBasePreference1):
    """
    Defines a preference for a particular set of criteria for vehicle (e.g., dates,
    equipment, vendor, car type).

    Parameters
    ----------
    corporate_id
    pick_up_start_date
        A valid date in YYYY-MM-DD format.
    pick_up_end_date
        A valid date in YYYY-MM-DD format.
    rate_code
    special_equip_misc_travel
        Util: ReferenceDataRetrieveReq, TypeCode VehicleMiscType
    special_equip_ref_category
        Util: ReferenceDataRetrieveReq, TypeCode VehicleMiscType
    special_request_misc_travel
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType', Util:
        ReferenceDataRetrieveReq, TypeCode VehicleMiscType.
    special_request_ref_category
        Util: ReferenceDataRetrieveReq, TypeCode 'HotelMiscType', Util:
        ReferenceDataRetrieveReq, TypeCode VehicleMiscType.
    vehicle_type_misc_travel
        Util: ReferenceDataRetrieveReq, TypeCode VehicleMiscType
    vehicle_type_ref_category
        Util: ReferenceDataRetrieveReq, TypeCode VehicleMiscType
    """

    class Meta:
        name = "VehiclePreference"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    corporate_id: None | str = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    pick_up_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PickUpStartDate",
            "type": "Attribute",
        },
    )
    pick_up_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PickUpEndDate",
            "type": "Attribute",
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
    special_equip_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "SpecialEquipMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    special_equip_ref_category: str = field(
        default="CEQ",
        metadata={
            "name": "SpecialEquipRefCategory",
            "type": "Attribute",
            "max_length": 4,
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
    vehicle_type_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "VehicleTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    vehicle_type_ref_category: str = field(
        default="CTP",
        metadata={
            "name": "VehicleTypeRefCategory",
            "type": "Attribute",
            "max_length": 4,
        },
    )
