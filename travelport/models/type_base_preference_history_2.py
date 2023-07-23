from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_geo_political_area_type_2 import TypeGeoPoliticalAreaType2
from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_preference_purpose_2 import TypePreferencePurpose2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeBasePreferenceHistory2(TypeKeyElement2):
    """
    Base history element for the preference elements.

    Parameters
    ----------
    booking_start_date
    booking_end_date
    currency
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
        A reference to a loyalty card element.
    other_loyalty_program_number
    payment_details_ref
        A reference to a payment details element list elsewhere.
    preference_payment_method
    purpose
        The purpose of the preference.
    priority_order
        Priority order associated with this Preference.
    supplier
    trip_approval
    """
    class Meta:
        name = "typeBasePreferenceHistory"

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
    departure_geo_political_area_type: None | TypeGeoPoliticalAreaType2 = field(
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
    emphasis: None | bool = field(
        default=None,
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
    inclusive: None | bool = field(
        default=None,
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
    purpose: None | TypePreferencePurpose2 = field(
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
    trip_approval: None | bool = field(
        default=None,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )
