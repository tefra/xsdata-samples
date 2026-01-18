from dataclasses import dataclass, field
from typing import Optional

from .all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
