from collections.abc import Iterable
from dataclasses import dataclass, field

from .catering_facility_enumeration import CateringFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CateringFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[CateringFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
