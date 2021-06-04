from dataclasses import dataclass
from netex.models.type_of_journey_pattern_value_structure import TypeOfJourneyPatternValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfJourneyPattern(TypeOfJourneyPatternValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
