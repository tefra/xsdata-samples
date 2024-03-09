from dataclasses import dataclass

from .type_of_projection_ref_structure import TypeOfProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfProjectionRef(TypeOfProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
