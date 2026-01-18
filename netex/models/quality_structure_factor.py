from __future__ import annotations

from dataclasses import dataclass

from .quality_structure_factor_version_structure import (
    QualityStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactor(QualityStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
