from dataclasses import dataclass, field
from typing import Optional

from .emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmergencyService:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: EmergencyServiceEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
