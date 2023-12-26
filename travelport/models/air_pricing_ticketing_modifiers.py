from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.ticketing_modifiers import TicketingModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingTicketingModifiers:
    """AirPricing TicketingModifier information
    - used to associate Ticketing Modifiers with one or more
    AirPricingInfos/ProviderReservationInfo"""

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticketing_modifiers: None | TicketingModifiers = field(
        default=None,
        metadata={
            "name": "TicketingModifiers",
            "type": "Element",
            "required": True,
        },
    )
