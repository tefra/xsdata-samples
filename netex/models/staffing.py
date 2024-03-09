from dataclasses import dataclass, field
from typing import Optional

from .staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Staffing:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
