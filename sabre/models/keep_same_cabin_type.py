from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class KeepSameCabinType:
    """
    Attributes:
        enabled: Set to "true" guarantees that all segments within
            single shopping option belong to the requested cabin.
    """

    enabled: None | bool = field(
        default=None,
        metadata={
            "name": "Enabled",
            "type": "Attribute",
            "required": True,
        },
    )
