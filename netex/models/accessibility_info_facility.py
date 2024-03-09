from dataclasses import dataclass, field
from typing import Optional

from .accessibility_info_facility_enumeration import (
    AccessibilityInfoFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityInfoFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[AccessibilityInfoFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
