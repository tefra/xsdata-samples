from dataclasses import dataclass

from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfValueRef(TypeOfValueRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
