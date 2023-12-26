from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_geo_political_area_type_1 import (
    TypeGeoPoliticalAreaType1,
)
from travelport.models.type_key_element_1 import TypeKeyElement1
from travelport.models.type_other_preference_1 import TypeOtherPreference1
from travelport.models.type_preference_purpose_1 import TypePreferencePurpose1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeOtherPreferenceHistory1(TypeKeyElement1):
    """
    History Element for OtherPreference.

    Parameters
    ----------
    purpose
        The purpose of the preference.
    priority_order
        Priority order associated with this Preference.
    trip_approval
    inclusive
        Indicates whether this preference is exclusive or inclusive (e.g.
        preference for not having a queen size bed vs preference to HAVE a
        queen size bed).
    other_supplier_type
        The type of the Other Preference.
    booking_start_date
    booking_end_date
    usage_start_date
    usage_end_date
    supplier_name
    geo_political_area_type
        The type of the geographical location.
    geo_political_area_code
        The location code of the geographical location.
    preference_payment_method
    payment_details_ref
        A reference to a payment details element list elsewhere.
    max_cost_amount
    currency
    general_preference
    """

    class Meta:
        name = "typeOtherPreferenceHistory"

    purpose: None | TypePreferencePurpose1 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    trip_approval: bool = field(
        default=False,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        },
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        },
    )
    other_supplier_type: None | TypeOtherPreference1 = field(
        default=None,
        metadata={
            "name": "OtherSupplierType",
            "type": "Attribute",
        },
    )
    booking_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        },
    )
    booking_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        },
    )
    usage_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UsageStartDate",
            "type": "Attribute",
        },
    )
    usage_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UsageEndDate",
            "type": "Attribute",
        },
    )
    supplier_name: None | str = field(
        default=None,
        metadata={
            "name": "SupplierName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    geo_political_area_type: None | TypeGeoPoliticalAreaType1 = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
        },
    )
    geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    preference_payment_method: None | str = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    payment_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        },
    )
    max_cost_amount: None | str = field(
        default=None,
        metadata={
            "name": "MaxCostAmount",
            "type": "Attribute",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        },
    )
    general_preference: None | str = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
