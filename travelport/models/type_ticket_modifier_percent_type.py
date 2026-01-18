from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeTicketModifierPercentType:
    """
    Ticketing Modifier used to alter a fare percentage before or during the
    ticketing operation.

    Parameters
    ----------
    percent
        Percent associated with a ticketing modifier
    """

    class Meta:
        name = "typeTicketModifierPercentType"

    percent: str = field(
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
