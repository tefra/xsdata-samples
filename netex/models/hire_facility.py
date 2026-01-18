from __future__ import annotations

from dataclasses import dataclass, field

from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
