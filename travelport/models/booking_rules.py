from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_rules_fare_reference import (
    BookingRulesFareReference,
)
from travelport.models.charges_rules import ChargesRules
from travelport.models.document_required import DocumentRequired
from travelport.models.restriction_2 import Restriction2

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BookingRules:
    """
    Rules related to pre pay booking.

    Parameters
    ----------
    booking_rules_fare_reference
    rule_info
        Pre pay booking rule information
    restriction
        Booking restrictions for associated pre pay account
    document_required
        Detail about required documents for this pre pay id
    gender_dob_required
        Vendor populates if gender/DOB data is required in book.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_rules_fare_reference: list[BookingRulesFareReference] = field(
        default_factory=list,
        metadata={
            "name": "BookingRulesFareReference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rule_info: list[BookingRules.RuleInfo] = field(
        default_factory=list,
        metadata={
            "name": "RuleInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    restriction: list[Restriction2] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    document_required: list[DocumentRequired] = field(
        default_factory=list,
        metadata={
            "name": "DocumentRequired",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    gender_dob_required: None | bool = field(
        default=None,
        metadata={
            "name": "GenderDobRequired",
            "type": "Attribute",
        },
    )

    @dataclass
    class RuleInfo:
        charges_rules: None | ChargesRules = field(
            default=None,
            metadata={
                "name": "ChargesRules",
                "type": "Element",
            },
        )
