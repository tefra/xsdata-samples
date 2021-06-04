from dataclasses import dataclass
from netex.models.railway_link_ref_by_value_structure import RailwayLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayLinkRefByValue(RailwayLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
