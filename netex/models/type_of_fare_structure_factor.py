from __future__ import annotations

from dataclasses import dataclass

from .type_of_fare_structure_factor_version_structure import (
    TypeOfFareStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactor(TypeOfFareStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
