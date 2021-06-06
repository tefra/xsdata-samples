from dataclasses import dataclass
from .tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneRef1(TariffZoneRefStructure):
    class Meta:
        name = "TariffZoneRef"
        namespace = "http://www.netex.org.uk/netex"
