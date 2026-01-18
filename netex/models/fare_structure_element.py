from __future__ import annotations

from dataclasses import dataclass

from .fare_structure_element_version_structure import (
    FareStructureElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElement(FareStructureElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
