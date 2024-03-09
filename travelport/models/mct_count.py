from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_mct_connection import TypeMctConnection

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctCount:
    """
    The count of MCT exceptions for the given search criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    connection: None | TypeMctConnection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
            "required": True,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    count: None | int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        },
    )
