from dataclasses import dataclass, field
from typing import Optional
from netex.models.emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmergencyService:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[EmergencyServiceEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
