from __future__ import annotations

from dataclasses import dataclass, field

from .metro_submode_enumeration import MetroSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MetroSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MetroSubmodeEnumeration = field(
        default=MetroSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
