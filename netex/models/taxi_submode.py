from dataclasses import dataclass, field
from netex.models.taxi_submode_enumeration import TaxiSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TaxiSubmodeEnumeration = field(
        default=TaxiSubmodeEnumeration.UNKNOWN,
    )
