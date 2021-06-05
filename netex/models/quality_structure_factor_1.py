from dataclasses import dataclass
from netex.models.quality_structure_factor_version_structure import QualityStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactor1(QualityStructureFactorVersionStructure):
    class Meta:
        name = "QualityStructureFactor"
        namespace = "http://www.netex.org.uk/netex"
