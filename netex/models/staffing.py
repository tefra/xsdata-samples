from __future__ import annotations

from dataclasses import dataclass, field

from .staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Staffing:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: StaffingEnumeration = field(
        metadata={
            "required": True,
        }
    )
