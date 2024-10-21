from collections.abc import Iterable
from dataclasses import dataclass, field

from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationAccessList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
