from dataclasses import dataclass
from .single_journey_path_ref_structure import SingleJourneyPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyPathRef(SingleJourneyPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
