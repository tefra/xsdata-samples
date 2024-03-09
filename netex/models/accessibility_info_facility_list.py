from dataclasses import dataclass, field
from typing import List

from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityInfoFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessibilityInfoFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
