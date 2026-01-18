from __future__ import annotations

from dataclasses import dataclass

from .geographical_structure_factor_ref_structure import (
    GeographicalStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactorRef(GeographicalStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
