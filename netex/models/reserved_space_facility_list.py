from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservedSpaceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[ReservedSpaceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
