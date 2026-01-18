from __future__ import annotations

from dataclasses import dataclass, field

from .priceable_object_version_structure import (
    FareStructureFactorVersionStructure,
)
from .quality_structure_factor_prices_rel_structure import (
    QualityStructureFactorPricesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorVersionStructure(
    FareStructureFactorVersionStructure
):
    class Meta:
        name = "QualityStructureFactor_VersionStructure"

    value: None | object = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | QualityStructureFactorPricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
