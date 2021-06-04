from dataclasses import dataclass
from netex.models.timetabled_passing_time_ref_structure import TimetabledPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetabledPassingTimeRef(TimetabledPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
