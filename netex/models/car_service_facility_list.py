from dataclasses import dataclass, field
from typing import List
from netex.models.car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CarServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
