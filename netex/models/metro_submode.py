from dataclasses import dataclass, field
from netex.models.metro_submode_enumeration import MetroSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MetroSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MetroSubmodeEnumeration = field(
        default=MetroSubmodeEnumeration.UNKNOWN,
    )
