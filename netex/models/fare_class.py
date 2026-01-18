from __future__ import annotations

from dataclasses import dataclass, field

from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareClass:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FareClassEnumeration = field(
        default=FareClassEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
