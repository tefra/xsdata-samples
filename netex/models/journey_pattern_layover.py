from dataclasses import dataclass
from .journey_pattern_layover_structure import JourneyPatternLayoverStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternLayover(JourneyPatternLayoverStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
