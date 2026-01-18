from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .dead_run_ref import DeadRunRef
from .journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultDeadRunRunTimeVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    class Meta:
        name = "DefaultDeadRunRunTime_VersionedChildStructure"

    run_time: XmlDuration = field(
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    dead_run_ref: None | DeadRunRef = field(
        default=None,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
