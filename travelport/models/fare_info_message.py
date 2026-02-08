from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareInfoMessage:
    """
    A simple textual fare information message.Providers supported :
    1G/1V/1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(default="")
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
