from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[CarServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
