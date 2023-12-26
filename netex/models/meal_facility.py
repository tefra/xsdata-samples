from dataclasses import dataclass, field
from typing import Optional
from .meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MealFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[MealFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
