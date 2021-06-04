from dataclasses import dataclass
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareZoneRefStructure(TariffZoneRefStructure):
    pass
