from collections.abc import Iterable
from dataclasses import dataclass, field

from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HireFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
