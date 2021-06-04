from dataclasses import dataclass
from netex.models.geographical_structure_factor_version_structure import GeographicalStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalStructureFactor(GeographicalStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
