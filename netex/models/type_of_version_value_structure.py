from dataclasses import dataclass
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfVersionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfVersion_ValueStructure"
