from dataclasses import dataclass

from .type_of_fare_product_ref_structure import TypeOfFareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareProductRef(TypeOfFareProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
