from dataclasses import dataclass
from netex.models.link_sequence_projection_version_structure import LinkSequenceProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequenceProjection(LinkSequenceProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
