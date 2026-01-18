from __future__ import annotations

from dataclasses import dataclass, field

from .car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CarServiceFacilityEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
