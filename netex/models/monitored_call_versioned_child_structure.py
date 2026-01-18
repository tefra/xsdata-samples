from __future__ import annotations

from dataclasses import dataclass, field

from .call_versioned_child_structure import CallVersionedChildStructure
from .estimated_passing_time_view import EstimatedPassingTimeView
from .observed_passing_time_view import ObservedPassingTimeView
from .onward_calls_rel_structure import OnwardCallsRelStructure
from .previous_calls_rel_structure import PreviousCallsRelStructure
from .target_passing_time_view import TargetPassingTimeView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonitoredCallVersionedChildStructure(CallVersionedChildStructure):
    class Meta:
        name = "MonitoredCall_VersionedChildStructure"

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
    observed_passing_time_view: None | ObservedPassingTimeView = field(
        default=None,
        metadata={
            "name": "ObservedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    previous_calls: None | PreviousCallsRelStructure = field(
        default=None,
        metadata={
            "name": "previousCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_calls: None | OnwardCallsRelStructure = field(
        default=None,
        metadata={
            "name": "onwardCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
