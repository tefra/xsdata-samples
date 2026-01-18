from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from .timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyRunTimeVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    class Meta:
        name = "JourneyRunTime_VersionedChildStructure"

    timing_link_ref: TimingLinkRef | None = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_time: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
