from dataclasses import dataclass, field
from typing import Optional
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[AssistanceFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
