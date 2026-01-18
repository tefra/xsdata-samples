from __future__ import annotations

from dataclasses import dataclass, field

from .gender_limitation_enumeration import GenderLimitationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GenderLimitation:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: GenderLimitationEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
