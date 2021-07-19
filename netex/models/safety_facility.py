from dataclasses import dataclass, field
from typing import Optional
from .safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SafetyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[SafetyFacilityEnumeration] = field(
        default=None
    )
