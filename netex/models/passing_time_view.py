from dataclasses import dataclass
from netex.models.passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeView(PassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
