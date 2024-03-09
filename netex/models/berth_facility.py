from dataclasses import dataclass, field
from typing import Optional

from .berth_facility_enumeration import BerthFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BerthFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[BerthFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
