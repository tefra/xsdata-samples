from dataclasses import dataclass
from netex.models.headway_ref_structure import HeadwayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HeadwayRef(HeadwayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
