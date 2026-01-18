from dataclasses import dataclass, field

from .call_versioned_child_structure import CallVersionedChildStructure
from .estimated_passing_time_view import EstimatedPassingTimeView
from .observed_passing_time_view import ObservedPassingTimeView
from .onward_calls_rel_structure import OnwardCallsRelStructure
from .previous_calls_rel_structure import PreviousCallsRelStructure
from .target_passing_time_view import TargetPassingTimeView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonitoredCallVersionedChildStructure(CallVersionedChildStructure):
    class Meta:
        name = "MonitoredCall_VersionedChildStructure"

    target_passing_time_view: TargetPassingTimeView | None = field(
        default=None,
        metadata={
            "name": "TargetPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    estimated_passing_time_view: EstimatedPassingTimeView | None = field(
        default=None,
        metadata={
            "name": "EstimatedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    observed_passing_time_view: ObservedPassingTimeView | None = field(
        default=None,
        metadata={
            "name": "ObservedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    previous_calls: PreviousCallsRelStructure | None = field(
        default=None,
        metadata={
            "name": "previousCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_calls: OnwardCallsRelStructure | None = field(
        default=None,
        metadata={
            "name": "onwardCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
