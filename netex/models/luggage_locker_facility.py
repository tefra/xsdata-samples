from __future__ import annotations

from dataclasses import dataclass, field

from .luggage_locker_facility_enumeration import (
    LuggageLockerFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageLockerFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | LuggageLockerFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
