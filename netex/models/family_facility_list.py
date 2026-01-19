from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FamilyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[FamilyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
