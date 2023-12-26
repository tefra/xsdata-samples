from dataclasses import dataclass, field
from typing import List
from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationAccessList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
