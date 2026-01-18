from __future__ import annotations

from dataclasses import dataclass, field

from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityInfoFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | AccessibilityInfoFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
