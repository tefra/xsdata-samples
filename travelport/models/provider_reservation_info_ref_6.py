from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class ProviderReservationInfoRef6:
    """
    Container for Provider reservation reference key.
    """

    class Meta:
        name = "ProviderReservationInfoRef"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
