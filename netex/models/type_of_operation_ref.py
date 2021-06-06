from dataclasses import dataclass
from .type_of_operation_ref_structure import TypeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOperationRef(TypeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
