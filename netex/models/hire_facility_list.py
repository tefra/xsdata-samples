from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
