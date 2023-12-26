from dataclasses import dataclass, field
from typing import List
from .nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NuisanceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
