from dataclasses import dataclass
from netex.models.scheduled_stop_point_derived_view_structure import ScheduledStopPointDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointView(ScheduledStopPointDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
