from dataclasses import dataclass
from .activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BeaconPointVersionStructure(ActivationPointVersionStructure):
    class Meta:
        name = "BeaconPoint_VersionStructure"
