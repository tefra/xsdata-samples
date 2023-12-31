from dataclasses import dataclass
from .fleet_version_structure import FleetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Fleet(FleetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
