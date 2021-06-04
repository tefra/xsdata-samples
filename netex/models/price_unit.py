from dataclasses import dataclass
from netex.models.price_unit_version_structure import PriceUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceUnit(PriceUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
