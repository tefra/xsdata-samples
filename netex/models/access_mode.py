from __future__ import annotations

from dataclasses import dataclass, field

from .access_mode_enumeration import AccessModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessModeEnumeration = field(
        metadata={
            "required": True,
        }
    )
