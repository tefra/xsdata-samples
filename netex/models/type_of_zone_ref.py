from __future__ import annotations

from dataclasses import dataclass

from .type_of_zone_ref_structure import TypeOfZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfZoneRef(TypeOfZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
