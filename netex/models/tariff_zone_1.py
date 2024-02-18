from dataclasses import dataclass
from .tariff_zone_version_structure import TariffZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZone1(TariffZoneVersionStructure):
    class Meta:
        name = "TariffZone"
        namespace = "http://www.netex.org.uk/netex"
