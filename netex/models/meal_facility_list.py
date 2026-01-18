from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MealFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[MealFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
