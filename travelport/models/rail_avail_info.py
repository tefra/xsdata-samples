from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailAvailInfo:
    """
    Parameters
    ----------
    class_code
        A booking code or fare basis code or fare class.
    quantity
        Available fare basis code or fare class quantity.
    cabin_class
        The fare basis code or fare class for this fare.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    class_code: None | str = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
