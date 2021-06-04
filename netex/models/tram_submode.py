from dataclasses import dataclass, field
from netex.models.tram_submode_enumeration import TramSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TramSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TramSubmodeEnumeration = field(
        default=TramSubmodeEnumeration.UNKNOWN,
    )
