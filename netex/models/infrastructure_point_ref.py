from dataclasses import dataclass

from .infrastructure_point_ref_structure import InfrastructurePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructurePointRef(InfrastructurePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
