from dataclasses import dataclass
from .quality_structure_factor_ref_structure import (
    QualityStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorRef(QualityStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
