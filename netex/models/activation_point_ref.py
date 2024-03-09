from dataclasses import dataclass

from .activation_point_ref_structure import ActivationPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointRef(ActivationPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
