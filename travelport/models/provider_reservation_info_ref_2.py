from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class ProviderReservationInfoRef2:
    """
    Container for Provider reservation reference key.
    """
    class Meta:
        name = "ProviderReservationInfoRef"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
