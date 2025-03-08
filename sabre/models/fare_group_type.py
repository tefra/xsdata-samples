from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FareGroupType:
    """
    IntelliSell Type.
    """

    fare_type_name: None | str = field(
        default=None,
        metadata={
            "name": "FareTypeName",
            "type": "Attribute",
        },
    )
