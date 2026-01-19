from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .luggage_locker_facility_enumeration import (
    LuggageLockerFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
