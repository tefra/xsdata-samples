from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class RoomView:
    """
    Parameters
    ----------
    code
        OTA code represents different hotel room views.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
