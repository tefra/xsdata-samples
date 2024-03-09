from dataclasses import dataclass

from .beacon_point_version_structure import BeaconPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BeaconPoint(BeaconPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
