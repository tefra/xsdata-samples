from dataclasses import dataclass
from netex.models.timing_pattern_ref_structure import TimingPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPatternRef(TimingPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
