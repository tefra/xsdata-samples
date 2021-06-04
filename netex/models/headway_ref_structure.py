from dataclasses import dataclass
from netex.models.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HeadwayRefStructure(JourneyTimingRefStructure):
    pass
