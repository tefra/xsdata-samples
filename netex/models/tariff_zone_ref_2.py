from dataclasses import dataclass

from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneRef2(ZoneRefStructure):
    class Meta:
        name = "TariffZoneRef_"
        namespace = "http://www.netex.org.uk/netex"
