from dataclasses import dataclass
from netex.models.journey_designator_structure import JourneyDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyDesignator(JourneyDesignatorStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
