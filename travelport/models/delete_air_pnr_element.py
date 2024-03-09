from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_air_pnr_element import TypeAirPnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class DeleteAirPnrElement:
    """
    Container for Air PNR elements to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: None | TypeAirPnrElement = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
