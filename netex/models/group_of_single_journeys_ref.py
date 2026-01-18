from __future__ import annotations

from dataclasses import dataclass

from .group_of_single_journeys_ref_structure import (
    GroupOfSingleJourneysRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSingleJourneysRef(GroupOfSingleJourneysRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
