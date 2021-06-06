from dataclasses import dataclass
from .timing_algorithm_type_value_structure import TimingAlgorithmTypeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingAlgorithmType(TimingAlgorithmTypeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
