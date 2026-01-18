from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_mct_connection import TypeMctConnection

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class MctCount:
    """
    The count of MCT exceptions for the given search criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    connection: TypeMctConnection = field(
        metadata={
            "name": "Connection",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    count: int = field(
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )
