from dataclasses import dataclass, field
from typing import Optional
from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SanitaryFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[SanitaryFacilityEnumeration] = field(
        default=None
    )
