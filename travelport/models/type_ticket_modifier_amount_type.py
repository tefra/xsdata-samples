from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeTicketModifierAmountType:
    """
    Ticketing Modifier used to alter a fare amount before or during the ticketing
    operation.

    Parameters
    ----------
    amount
        Amount associated with a ticketing modifier
    """

    class Meta:
        name = "typeTicketModifierAmountType"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        },
    )
