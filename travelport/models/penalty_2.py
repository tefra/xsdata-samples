from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Penalty2:
    """
    Parameters
    ----------
    amount
        Penalty Amount
    penalty_type
        This is the PPC (Price Processing Code)code.
    """

    class Meta:
        name = "Penalty"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    penalty_type: None | str = field(
        default=None,
        metadata={
            "name": "PenaltyType",
            "type": "Attribute",
        },
    )
