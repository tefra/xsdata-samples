from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class ProviderReservationInfoRef1:
    """
    Container for Provider reservation reference key.
    """
    class Meta:
        name = "ProviderReservationInfoRef"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
