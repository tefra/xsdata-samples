from dataclasses import dataclass
from .direction_ref_structure import DirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionRef(DirectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
