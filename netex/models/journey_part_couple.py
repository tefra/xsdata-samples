from dataclasses import dataclass
from .journey_part_couple_version_structure import JourneyPartCoupleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCouple(JourneyPartCoupleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
