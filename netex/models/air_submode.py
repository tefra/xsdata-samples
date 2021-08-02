from dataclasses import dataclass, field
from .air_submode_enumeration import AirSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AirSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AirSubmodeEnumeration = field(
        default=AirSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
