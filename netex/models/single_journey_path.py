from dataclasses import dataclass
from .single_journey_path_version_structure import (
    SingleJourneyPathVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyPath(SingleJourneyPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
