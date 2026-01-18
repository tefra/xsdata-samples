from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityInfoFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[AccessibilityInfoFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
