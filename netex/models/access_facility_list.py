from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[AccessFacilityEnumeration] = field(
        default_factory=lambda: [
            AccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
