from dataclasses import dataclass, field
from typing import Optional
from netex.models.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkInJourneyPatternVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "LinkInJourneyPattern_VersionedChildStructure"

    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
