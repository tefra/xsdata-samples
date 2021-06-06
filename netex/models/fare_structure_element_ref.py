from dataclasses import dataclass
from .fare_structure_element_ref_structure import FareStructureElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementRef(FareStructureElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
