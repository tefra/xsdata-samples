from dataclasses import dataclass
from netex.models.timetabled_passing_time_view_structure import TimetabledPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetabledPassingTimeView(TimetabledPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
