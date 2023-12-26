from dataclasses import dataclass, field
from typing import List
from .emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmergencyServiceList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
