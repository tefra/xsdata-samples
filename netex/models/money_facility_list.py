from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[MoneyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
