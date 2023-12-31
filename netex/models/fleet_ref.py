from dataclasses import dataclass
from .fleet_ref_structure import FleetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FleetRef(FleetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
