from dataclasses import dataclass
from .link_sequence_version_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Route2(LinkSequenceVersionStructure):
    class Meta:
        name = "Route_"
        namespace = "http://www.netex.org.uk/netex"
