from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SafetyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
