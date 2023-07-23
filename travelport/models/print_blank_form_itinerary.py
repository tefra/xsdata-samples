from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrintBlankFormItinerary:
    """
    Produce a customized itinerary/Invoice document in blank form format.

    Parameters
    ----------
    include_description
        If it is true then document will be printed including descriptions.
    include_header
        If it is true then document will be printed including it's header.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    include_description: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeDescription",
            "type": "Attribute",
            "required": True,
        }
    )
    include_header: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeHeader",
            "type": "Attribute",
            "required": True,
        }
    )
