from __future__ import annotations

from dataclasses import dataclass

from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactorVersionStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfFareStructureFactor_VersionStructure"
