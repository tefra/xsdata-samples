from dataclasses import dataclass
from .type_of_fare_structure_factor_ref_structure import TypeOfFareStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareStructureFactorRef(TypeOfFareStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
