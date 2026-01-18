from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .accommodation_facility_enumeration import (
    AccommodationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[AccommodationFacilityEnumeration] = field(
        default_factory=lambda: [
            AccommodationFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
