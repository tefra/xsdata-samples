from dataclasses import dataclass
from netex.models.stop_area_version_structure import StopAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopArea(StopAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
