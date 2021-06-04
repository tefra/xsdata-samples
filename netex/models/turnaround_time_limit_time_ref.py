from dataclasses import dataclass
from netex.models.turnaround_time_limit_time_ref_structure import TurnaroundTimeLimitTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TurnaroundTimeLimitTimeRef(TurnaroundTimeLimitTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
