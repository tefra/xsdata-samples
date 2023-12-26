from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class StockControl2:
    """
    The Stock Control Numbers related details of the MCO.

    Parameters
    ----------
    type_value
        Stock control type valid options include: Pending, Failed, Plain
        Paper, Blank, Suppressed.
    number
        Stock control number.
    """

    class Meta:
        name = "StockControl"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
