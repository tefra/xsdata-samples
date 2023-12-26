from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_geo_political_area_type_1 import (
    TypeGeoPoliticalAreaType1,
)
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_other_preference_1 import TypeOtherPreference1
from travelport.models.type_preference_purpose_1 import TypePreferencePurpose1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class OtherPreference1(TypeKeyTaggedElement1):
    """
    Defines a preference for a particular set of criteria (e.g. dates, supplier,
    etc.) that does not fall into the Air, Rail, Vehicle, or Hotel categories.

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
    supplier_name
    booking_start_date
        A valid date in YYYY-MM-DD format.
    booking_end_date
        A valid date in YYYY-MM-DD format.
    usage_start_date
    usage_end_date
    geo_political_area_type
        The type of the geographical location.
    geo_political_area_code
        The location code of the geographical location.
    preference_payment_method
        See uAPI Profile Help and ReferenceDataRetrieveReq, TypeCode
        PaymentFormatType
    payment_details_ref
        Used to sync up Keys in FormOfPayment element with Preference
        attribute PaymentDetailsRef by entering same key number.
    max_cost_amount
        See uAPI Profile Help.
    currency
        ReferencedataRetrieveReq, Type Code Currency
    general_preference
    """

    class Meta:
        name = "OtherPreference"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
    supplier_name: None | str = field(
        default=None,
        metadata={
            "name": "SupplierName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
