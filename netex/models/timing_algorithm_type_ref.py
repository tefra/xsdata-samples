from dataclasses import dataclass
from .timing_algorithm_type_ref_structure import TimingAlgorithmTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingAlgorithmTypeRef(TimingAlgorithmTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
