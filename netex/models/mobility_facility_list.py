from collections.abc import Iterable
from dataclasses import dataclass, field

from .mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
