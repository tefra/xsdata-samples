from dataclasses import dataclass, field
from typing import List

from .meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MealFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MealFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
