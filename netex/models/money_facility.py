from __future__ import annotations

from dataclasses import dataclass, field

from .money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MoneyFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
