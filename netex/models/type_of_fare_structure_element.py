from __future__ import annotations

from dataclasses import dataclass

from .type_of_fare_structure_element_version_structure import (
    TypeOfFareStructureElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureElement(TypeOfFareStructureElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
