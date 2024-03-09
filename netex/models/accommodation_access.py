from dataclasses import dataclass, field
from typing import Optional

from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationAccess:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[AccommodationAccessEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
