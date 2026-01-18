from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[ParkingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
