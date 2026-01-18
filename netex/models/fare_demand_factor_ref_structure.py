from __future__ import annotations

from dataclasses import dataclass

from .quality_structure_factor_ref_structure import (
    QualityStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDemandFactorRefStructure(QualityStructureFactorRefStructure):
    pass
