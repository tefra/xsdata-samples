from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.air_segment_pricing_modifiers import (
    AirSegmentPricingModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingCommand:
    """
    A containter to identify individual pricing events.

    A pricing result will be returned for each pricing command according to
    its parameters.

    Parameters
    ----------
    air_pricing_modifiers
    air_segment_pricing_modifiers
    command_key
        An identifier to link the pricing responses to the pricing commands.
        The value passed here will be returned in the resulting
        AirPricingInfo(s) from this command.
    cabin_class
        Specify the cabin type to price the entire itinerary in. If segment
        level cabin selection is required, this attribute should not be
        used.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
            "max_occurs": 999,
        },
    )
    command_key: None | str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        },
    )
