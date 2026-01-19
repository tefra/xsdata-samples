from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationAccessList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
