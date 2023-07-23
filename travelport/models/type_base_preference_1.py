from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_geo_political_area_type_1 import TypeGeoPoliticalAreaType1
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_preference_purpose_1 import TypePreferencePurpose1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeBasePreference1(TypeKeyTaggedElement1):
    """
    Parameters
    ----------
    booking_start_date
        A valid date in YYYY-MM-DD format.
    booking_end_date
        A valid date in YYYY-MM-DD format.
    currency
        ReferencedataRetrieveReq, Type Code Currency
    departure_geo_political_area_type
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    departure_geo_political_area_code
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    emphasis
    general_preference
    inclusive
        Indicates whether this preference is exclusive or inclusive (e.g.
        preference for not having a queen size bed vs preference to HAVE a
        queen size bed).
    loyalty_program_enrollment_ref
        Used to sync up Keys in  LoyaltyProgramEnrollment element with
        Preference LoyaltyProgramEnrollmentRef by entering same key number.
    other_loyalty_program_number
    payment_details_ref
        Used to sync up Keys in FormOfPayment element with Preference
        attribute PaymentDetailsRef by entering same key number.
    preference_payment_method
        See uAPI Profile Help and ReferenceDataRetrieveReq, TypeCode
        PaymentFormatType
    purpose
        The purpose of the preference.
    priority_order
        Priority order associated with this Preference.
    supplier
        a. Util:ReferenceDataRetrieveReq, TypeCode HotelSupplierType
        b.Util:ReferenceDataRetrieveReq, TypeCode VehicleSupplierType c.
        Util:ReferenceDataRetrieveReq, TypeCode AirAndRailSupplierType
    trip_approval
    """
    class Meta:
        name = "typeBasePreference"

    booking_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        }
    )
    booking_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        }
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    departure_geo_political_area_type: None | TypeGeoPoliticalAreaType1 = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    departure_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    emphasis: bool = field(
        default=False,
        metadata={
            "name": "Emphasis",
            "type": "Attribute",
        }
    )
    general_preference: None | str = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        }
    )
    loyalty_program_enrollment_ref: None | str = field(
        default=None,
        metadata={
            "name": "LoyaltyProgramEnrollmentRef",
            "type": "Attribute",
        }
    )
    other_loyalty_program_number: None | str = field(
        default=None,
        metadata={
            "name": "OtherLoyaltyProgramNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    payment_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        }
    )
    preference_payment_method: None | str = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    purpose: None | TypePreferencePurpose1 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    supplier: None | str = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    trip_approval: bool = field(
        default=False,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )
