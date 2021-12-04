from dataclasses import dataclass
from .tariff_zone_version_structure import TariffZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZone(TariffZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
