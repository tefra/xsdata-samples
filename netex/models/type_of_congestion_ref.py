from dataclasses import dataclass

from .type_of_congestion_ref_structure import TypeOfCongestionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfCongestionRef(TypeOfCongestionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
