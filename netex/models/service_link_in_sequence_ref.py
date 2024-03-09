from dataclasses import dataclass

from .service_link_in_sequence_ref_structure import (
    ServiceLinkInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkInSequenceRef(ServiceLinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
