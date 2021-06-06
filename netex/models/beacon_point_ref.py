from dataclasses import dataclass
from .beacon_point_ref_structure import BeaconPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BeaconPointRef(BeaconPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
