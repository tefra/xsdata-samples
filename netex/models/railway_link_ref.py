from dataclasses import dataclass
from netex.models.railway_link_ref_structure import RailwayLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayLinkRef(RailwayLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
