from dataclasses import dataclass
from netex.models.geographical_structure_factor_ref_structure import GeographicalStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalStructureFactorRef(GeographicalStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
