from dataclasses import dataclass

from .border_point_value_structure import BorderPointValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BorderPoint(BorderPointValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
