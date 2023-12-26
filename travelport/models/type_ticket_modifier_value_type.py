from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeTicketModifierValueType:
    """
    Ticketing Modifier used to add value discount information.

    Parameters
    ----------
    value
    net_fare_value
        Treat the value as net fare discount information
    """

    class Meta:
        name = "typeTicketModifierValueType"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        },
    )
    net_fare_value: None | bool = field(
        default=None,
        metadata={
            "name": "NetFareValue",
            "type": "Attribute",
        },
    )
