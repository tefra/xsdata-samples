from dataclasses import dataclass

from .direction_value_structure import DirectionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Direction(DirectionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
