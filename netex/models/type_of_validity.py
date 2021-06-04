from dataclasses import dataclass
from netex.models.type_of_validity_value_structure import TypeOfValidityValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfValidity(TypeOfValidityValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
