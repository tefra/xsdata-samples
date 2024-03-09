from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_pnr_element import TypePnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class DeletePnrElement:
    """
    Container for PNR elements to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: None | TypePnrElement = field(
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
