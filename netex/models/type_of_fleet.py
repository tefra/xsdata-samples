from __future__ import annotations

from dataclasses import dataclass

from .type_of_fleet_value_structure import TypeOfFleetValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFleet(TypeOfFleetValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
