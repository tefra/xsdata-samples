from __future__ import annotations

from dataclasses import dataclass, field

from .funicular_submode_enumeration import FunicularSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FunicularSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FunicularSubmodeEnumeration = field(
        default=FunicularSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
