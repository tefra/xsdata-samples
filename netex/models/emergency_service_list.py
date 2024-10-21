from collections.abc import Iterable
from dataclasses import dataclass, field

from .emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmergencyServiceList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
