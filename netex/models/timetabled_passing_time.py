from dataclasses import dataclass
from netex.models.timetabled_passing_time_versioned_child_structure import TimetabledPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetabledPassingTime(TimetabledPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
