from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_weight import TypeWeight

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaggageAllowance:
    """
    Free Baggage Allowance.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    number_of_pieces: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfPieces",
            "type": "Element",
        },
    )
    max_weight: None | TypeWeight = field(
        default=None,
        metadata={
            "name": "MaxWeight",
            "type": "Element",
        },
    )
