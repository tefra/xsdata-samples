from dataclasses import dataclass

from .target_passing_time_view_structure import TargetPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTimeView(TargetPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
