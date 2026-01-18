from __future__ import annotations

from dataclasses import dataclass

from .group_of_single_journeys_version_structure import (
    GroupOfSingleJourneysVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSingleJourneys(GroupOfSingleJourneysVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
