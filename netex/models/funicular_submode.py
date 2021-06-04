from dataclasses import dataclass, field
from netex.models.funicular_submode_enumeration import FunicularSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FunicularSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FunicularSubmodeEnumeration = field(
        default=FunicularSubmodeEnumeration.UNKNOWN,
    )
