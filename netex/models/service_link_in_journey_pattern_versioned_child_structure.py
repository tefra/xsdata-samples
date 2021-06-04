from dataclasses import dataclass, field
from typing import Optional
from netex.models.journey_run_times_rel_structure import JourneyRunTimesRelStructure
from netex.models.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkInJourneyPatternVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "ServiceLinkInJourneyPattern_VersionedChildStructure"

    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_times: Optional[JourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
