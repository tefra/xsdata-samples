from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelType:
    """
    Parameters
    ----------
    source_link
        Indicates whether results are  returned from the vendor or  from the
        database.  If true, vendor results were returned. Supported
        providers:1G, 1V
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    source_link: None | bool = field(
        default=None,
        metadata={
            "name": "SourceLink",
            "type": "Attribute",
        },
    )
