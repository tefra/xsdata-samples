from dataclasses import dataclass
from netex.models.border_point_ref_structure import BorderPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BorderPointRef(BorderPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
