from dataclasses import dataclass, field
from typing import Optional
from netex.models.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.models.timeband_refs_rel_structure import TimebandRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimebandsVersionedChildStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfTimebands_VersionedChildStructure"

    timebands: Optional[TimebandRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
