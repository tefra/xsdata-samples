from __future__ import annotations

from dataclasses import dataclass, field

from .access_mode_enumeration import AccessModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessModeEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
