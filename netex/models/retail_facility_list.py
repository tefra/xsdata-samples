from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[RetailFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
