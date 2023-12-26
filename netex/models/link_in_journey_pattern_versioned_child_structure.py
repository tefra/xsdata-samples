from dataclasses import dataclass, field
from typing import Optional, Union
from .link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from .service_link_ref import ServiceLinkRef
from .timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkInJourneyPatternVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    class Meta:
        name = "LinkInJourneyPattern_VersionedChildStructure"

    service_link_ref_or_timing_link_ref: Optional[
        Union[ServiceLinkRef, TimingLinkRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
