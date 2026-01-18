from __future__ import annotations

from dataclasses import dataclass

from .type_of_fleet_ref_structure import TypeOfFleetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFleetRef(TypeOfFleetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
