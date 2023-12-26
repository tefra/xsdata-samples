from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .link_sequence_refs_rel_structure import LinkSequenceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinkSequencesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLinkSequences_VersionStructure"

    members: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
