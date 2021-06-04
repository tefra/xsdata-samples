from dataclasses import dataclass
from netex.models.tariff_ref_structure import TariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffRef(TariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
