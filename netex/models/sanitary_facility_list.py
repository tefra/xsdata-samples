from collections.abc import Iterable
from dataclasses import dataclass, field

from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SanitaryFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
