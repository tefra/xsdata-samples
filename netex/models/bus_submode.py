from __future__ import annotations

from dataclasses import dataclass, field

from .bus_submode_enumeration import BusSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BusSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BusSubmodeEnumeration = field(
        default=BusSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
