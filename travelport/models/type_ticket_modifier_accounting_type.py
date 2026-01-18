from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeTicketModifierAccountingType:
    """
    Ticketing Modifier used to add accounting - discount information.
    """

    class Meta:
        name = "typeTicketModifierAccountingType"

    value: str = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )
