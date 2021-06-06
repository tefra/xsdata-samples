from dataclasses import dataclass
from .validable_element_ref_structure import ValidableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementRef(ValidableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
