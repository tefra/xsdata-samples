from dataclasses import dataclass
from netex.models.tariff_version_structure import TariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Tariff(TariffVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
