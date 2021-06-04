from dataclasses import dataclass
from netex.models.type_of_version_value_structure import TypeOfVersionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfVersion(TypeOfVersionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
