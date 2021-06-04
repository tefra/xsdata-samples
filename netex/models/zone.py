from dataclasses import dataclass
from netex.models.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Zone(ZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
