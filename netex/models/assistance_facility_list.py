from dataclasses import dataclass, field
from typing import List
from .assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
