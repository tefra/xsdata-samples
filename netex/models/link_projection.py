from dataclasses import dataclass
from netex.models.link_projection_version_structure import LinkProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkProjection(LinkProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
