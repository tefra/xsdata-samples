from dataclasses import dataclass
from .activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPoint1(ActivationPointVersionStructure):
    class Meta:
        name = "ActivationPoint"
        namespace = "http://www.netex.org.uk/netex"