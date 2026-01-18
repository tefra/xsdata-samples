from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_air_pnr_element import TypeAirPnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class DeleteAirPnrElement:
    """
    Container for Air PNR elements to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: TypeAirPnrElement = field(
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
