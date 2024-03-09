from dataclasses import dataclass

from .type_of_service_ref_structure import TypeOfServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfServiceRef(TypeOfServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
