from dataclasses import dataclass
from netex.models.estimated_passing_time_ref_structure import EstimatedPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EstimatedPassingTimeRef(EstimatedPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
