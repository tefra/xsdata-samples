from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFleetValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfFleet_ValueStructure"
