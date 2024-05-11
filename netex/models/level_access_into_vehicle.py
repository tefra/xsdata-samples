from dataclasses import dataclass, field

from .limitation_status_enumeration import LimitationStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LevelAccessIntoVehicle:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LimitationStatusEnumeration = field(
        default=LimitationStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
