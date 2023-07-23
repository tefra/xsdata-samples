from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_position import TypePosition
from travelport.models.type_row_location import TypeRowLocation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Characteristic3:
    """
    Parameters
    ----------
    value
    position
    row_location
    padiscode
        Industry standard code that defines seat and row characteristic.
    """
    class Meta:
        name = "Characteristic"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    position: None | TypePosition = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Attribute",
        }
    )
    row_location: None | TypeRowLocation = field(
        default=None,
        metadata={
            "name": "RowLocation",
            "type": "Attribute",
        }
    )
    padiscode: None | str = field(
        default=None,
        metadata={
            "name": "PADISCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 99,
        }
    )
