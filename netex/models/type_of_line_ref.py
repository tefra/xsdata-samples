from dataclasses import dataclass
from netex.models.type_of_line_ref_structure import TypeOfLineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfLineRef(TypeOfLineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
