from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.passenger_receipt_override import (
    PassengerReceiptOverride,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class DocumentOptions:
    """
    Allows an agency to set different document options for the itinerary.

    Parameters
    ----------
    passenger_receipt_override
    override_option
        Allows an agency to override print options for documents during
        document generation.
    suppress_itinerary_remarks
        True when itinerary remarks are suppressed.
    generate_itin_numbers
        True when itinerary numbers are system generated.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    passenger_receipt_override: None | PassengerReceiptOverride = field(
        default=None,
        metadata={
            "name": "PassengerReceiptOverride",
            "type": "Element",
        },
    )
    override_option: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OverrideOption",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 50,
        },
    )
    suppress_itinerary_remarks: None | bool = field(
        default=None,
        metadata={
            "name": "SuppressItineraryRemarks",
            "type": "Attribute",
        },
    )
    generate_itin_numbers: None | bool = field(
        default=None,
        metadata={
            "name": "GenerateItinNumbers",
            "type": "Attribute",
        },
    )
