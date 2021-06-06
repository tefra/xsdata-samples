from dataclasses import dataclass, field
from .rail_submode_enumeration import RailSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RailSubmodeEnumeration = field(
        default=RailSubmodeEnumeration.UNKNOWN,
    )
