from dataclasses import dataclass, field
from typing import Optional

from .car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[CarServiceFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
