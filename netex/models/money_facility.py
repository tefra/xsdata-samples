from dataclasses import dataclass, field
from typing import Optional

from .money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MoneyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[MoneyFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
