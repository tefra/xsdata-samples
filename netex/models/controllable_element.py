from dataclasses import dataclass
from .controllable_element_version_structure import (
    ControllableElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElement(ControllableElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
