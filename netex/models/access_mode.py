from dataclasses import dataclass, field
from typing import Optional

from .access_mode_enumeration import AccessModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[AccessModeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
