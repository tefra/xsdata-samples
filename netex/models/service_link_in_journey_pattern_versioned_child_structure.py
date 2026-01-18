from __future__ import annotations

from dataclasses import dataclass, field

from .journey_run_times_rel_structure import JourneyRunTimesRelStructure
from .link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from .service_link_ref import ServiceLinkRef
from .timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkInJourneyPatternVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    class Meta:
        name = "ServiceLinkInJourneyPattern_VersionedChildStructure"

    timing_link_ref: None | TimingLinkRef = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: None | JourneyRunTimesRelStructure = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_link_ref: ServiceLinkRef = field(
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
