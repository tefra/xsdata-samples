from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .luggage_service_facility_enumeration import (
    LuggageServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[LuggageServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
