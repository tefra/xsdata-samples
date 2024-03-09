from dataclasses import dataclass

from .group_of_timebands_versioned_child_structure import (
    GroupOfTimebandsVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimebands(GroupOfTimebandsVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
