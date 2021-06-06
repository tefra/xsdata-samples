from dataclasses import dataclass
from .zone_projection_version_structure import ZoneProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneProjection(ZoneProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
