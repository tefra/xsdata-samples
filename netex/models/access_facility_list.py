from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[AccessFacilityEnumeration] = field(
        default_factory=lambda: [
            AccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
