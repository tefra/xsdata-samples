from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .accommodation_facility_enumeration import (
    AccommodationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[AccommodationFacilityEnumeration] = field(
        default_factory=lambda: [
            AccommodationFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
