from collections.abc import Iterable
from dataclasses import dataclass, field

from .nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NuisanceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[NuisanceFacilityEnumeration] = field(
        default_factory=lambda: [
            NuisanceFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
