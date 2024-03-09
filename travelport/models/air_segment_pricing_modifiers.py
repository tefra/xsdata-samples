from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_code import BookingCode
from travelport.models.type_connection_indicator import TypeConnectionIndicator
from travelport.models.type_fare_break import TypeFareBreak

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentPricingModifiers:
    """Specifies modifiers that a particular segment should be priced in.

    If this is used, then there must be one for each AirSegment in the
    AirItinerary.

    Parameters
    ----------
    permitted_booking_codes
    air_segment_ref
    cabin_class
    account_code
    prohibit_advance_purchase_fares
    prohibit_non_refundable_fares
    prohibit_penalty_fares
    fare_basis_code
        The fare basis code to be used for pricing.
    fare_break
        Fare break point modifier to instruct Fares where it should or
        should not break the fare.
    connection_indicator
        ConnectionIndicator attribute will be used to map connection
        indicators AvailabilityAndPricing, TurnAround and Stopover. This
        attribute is for Wordspan/1P only.
    brand_tier
        Modifier to price by specific brand tier number.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    permitted_booking_codes: (
        None | AirSegmentPricingModifiers.PermittedBookingCodes
    ) = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        },
    )
    air_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        },
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        },
    )
    prohibit_penalty_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitPenaltyFares",
            "type": "Attribute",
        },
    )
    fare_basis_code: None | str = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
        },
    )
    fare_break: None | TypeFareBreak = field(
        default=None,
        metadata={
            "name": "FareBreak",
            "type": "Attribute",
        },
    )
    connection_indicator: None | TypeConnectionIndicator = field(
        default=None,
        metadata={
            "name": "ConnectionIndicator",
            "type": "Attribute",
        },
    )
    brand_tier: None | str = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        },
    )

    @dataclass
    class PermittedBookingCodes:
        booking_code: list[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
