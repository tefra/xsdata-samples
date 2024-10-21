from collections.abc import Iterable
from dataclasses import dataclass, field

from .retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[RetailFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
