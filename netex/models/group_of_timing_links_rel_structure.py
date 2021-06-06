from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .timing_link_refs_rel_structure import TimingLinkRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimingLinksRelStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfTimingLinks_RelStructure"

    members: Optional[TimingLinkRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
