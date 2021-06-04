from dataclasses import dataclass
from netex.models.service_link_in_sequence_ref_structure import ServiceLinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkInSequenceRef(ServiceLinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
