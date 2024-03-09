from dataclasses import dataclass

from .journey_part_couple_ref_structure import JourneyPartCoupleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCoupleRef(JourneyPartCoupleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
