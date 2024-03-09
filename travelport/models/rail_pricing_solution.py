from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_rail_pricing_solution import (
    TypeRailPricingSolution,
)

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailPricingSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"
