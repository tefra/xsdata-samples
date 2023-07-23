from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class IncludedItem:
    """
    Provides details of included item.

    Parameters
    ----------
    code
        Code for included item.
    description
        Description of included item.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
