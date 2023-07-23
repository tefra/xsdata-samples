from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TypeHotelReferencePoint:
    """
    Parameters
    ----------
    value
    country
        Country code.
    state
        State or Province Code.
    """
    class Meta:
        name = "typeHotelReferencePoint"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 30,
        }
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        }
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "max_length": 6,
        }
    )
