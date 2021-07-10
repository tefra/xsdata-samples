from dataclasses import dataclass, field
from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HireFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN
    )
