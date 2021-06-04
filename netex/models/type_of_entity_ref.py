from dataclasses import dataclass
from netex.models.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfEntityRef(TypeOfValueRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
