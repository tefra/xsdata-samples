from dataclasses import dataclass

from .quality_structure_factor_price_versioned_child_structure import (
    QualityStructureFactorPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorPrice(
    QualityStructureFactorPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
