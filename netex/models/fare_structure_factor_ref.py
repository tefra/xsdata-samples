from dataclasses import dataclass
from netex.models.fare_structure_factor_ref_structure import FareStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureFactorRef(FareStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
