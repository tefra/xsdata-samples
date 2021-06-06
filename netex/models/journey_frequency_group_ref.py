from dataclasses import dataclass
from .journey_frequency_group_ref_structure import JourneyFrequencyGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyFrequencyGroupRef(JourneyFrequencyGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
