from dataclasses import dataclass, field
from typing import Optional
from netex.models.gender_limitation_enumeration import GenderLimitationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GenderLimitation:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
