from dataclasses import dataclass
from netex.models.link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "InfrastructureLink_VersionStructure"
