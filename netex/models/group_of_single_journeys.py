from dataclasses import dataclass

from .group_of_single_journeys_version_structure import (
    GroupOfSingleJourneysVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSingleJourneys(GroupOfSingleJourneysVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
