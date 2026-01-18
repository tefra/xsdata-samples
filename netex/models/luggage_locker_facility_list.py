from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .luggage_locker_facility_enumeration import (
    LuggageLockerFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageLockerFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
