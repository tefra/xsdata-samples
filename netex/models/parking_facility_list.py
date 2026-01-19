from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[ParkingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
