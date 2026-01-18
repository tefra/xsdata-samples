from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NuisanceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
