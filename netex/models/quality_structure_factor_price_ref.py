from dataclasses import dataclass
from .quality_structure_factor_price_ref_structure import (
    QualityStructureFactorPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorPriceRef(QualityStructureFactorPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
