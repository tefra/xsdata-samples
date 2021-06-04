from dataclasses import dataclass, field
from typing import List
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NuisanceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[NuisanceFacilityEnumeration] = field(
        default_factory=lambda: [
            NuisanceFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        }
    )
