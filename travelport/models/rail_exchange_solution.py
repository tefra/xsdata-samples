from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_exchange_info import RailExchangeInfo
from travelport.models.type_rail_pricing_solution import (
    TypeRailPricingSolution,
)

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_exchange_info: None | RailExchangeInfo = field(
        default=None,
        metadata={
            "name": "RailExchangeInfo",
            "type": "Element",
        },
    )
