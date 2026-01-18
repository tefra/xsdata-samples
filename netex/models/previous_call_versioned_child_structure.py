from __future__ import annotations

from dataclasses import dataclass, field

from .call_versioned_child_structure import CallVersionedChildStructure
from .estimated_passing_time_view import EstimatedPassingTimeView
from .target_passing_time_view import TargetPassingTimeView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreviousCallVersionedChildStructure(CallVersionedChildStructure):
    class Meta:
        name = "PreviousCall_VersionedChildStructure"

    target_passing_time_view: None | TargetPassingTimeView = field(
        default=None,
        metadata={
            "name": "TargetPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    estimated_passing_time_view: None | EstimatedPassingTimeView = field(
        default=None,
        metadata={
            "name": "EstimatedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
