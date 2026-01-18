from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.air_segment_pricing_modifiers import (
    AirSegmentPricingModifiers,
)
from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AutoPricingInfo:
    """
    Auto Pricing based on Segment and Traveler Association.

    Parameters
    ----------
    air_segment_ref
    booking_traveler_ref
    air_pricing_modifiers
    air_segment_pricing_modifiers
    key
    pricing_type
        Indicates the Pricing Type used. The possible values are
        TicketRecord, StoredFare, PricingInstruction.
    plating_carrier
        The Plating Carrier for this journey
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 100,
        },
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 100,
        },
    )
    air_pricing_modifiers: None | AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
        },
    )
    air_segment_pricing_modifiers: list[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 100,
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    pricing_type: None | str = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
