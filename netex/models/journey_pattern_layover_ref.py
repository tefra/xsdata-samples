from dataclasses import dataclass
from netex.models.journey_pattern_layover_ref_structure import JourneyPatternLayoverRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternLayoverRef(JourneyPatternLayoverRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
