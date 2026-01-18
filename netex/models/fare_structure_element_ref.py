from __future__ import annotations

from dataclasses import dataclass

from .fare_structure_element_ref_structure import (
    FareStructureElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementRef(FareStructureElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
