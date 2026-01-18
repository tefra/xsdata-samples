from __future__ import annotations

from dataclasses import dataclass

from .group_of_timebands_versioned_child_structure import (
    GroupOfTimebandsVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebands(GroupOfTimebandsVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
