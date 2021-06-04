from dataclasses import dataclass
from netex.models.controllable_element_ref_structure import ControllableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementRef(ControllableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
