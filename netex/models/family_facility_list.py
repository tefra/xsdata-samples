from collections.abc import Iterable
from dataclasses import dataclass, field

from .family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FamilyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[FamilyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
