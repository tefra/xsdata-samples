from dataclasses import dataclass

from .infrastructure_link_ref_structure import InfrastructureLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureLinkRef(InfrastructureLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
