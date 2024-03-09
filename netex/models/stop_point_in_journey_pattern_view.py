from dataclasses import dataclass

from .stop_point_in_journey_pattern_derived_view_structure import (
    StopPointInJourneyPatternDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternView(
    StopPointInJourneyPatternDerivedViewStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
