from dataclasses import dataclass
from .type_of_projection_value_structure import TypeOfProjectionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfProjection(TypeOfProjectionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
