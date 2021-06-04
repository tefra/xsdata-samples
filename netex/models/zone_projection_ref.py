from dataclasses import dataclass
from netex.models.zone_projection_ref_structure import ZoneProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneProjectionRef(ZoneProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
