from __future__ import annotations

from dataclasses import dataclass

from .group_of_timing_links_ref_structure import GroupOfTimingLinksRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimingLinksRef(GroupOfTimingLinksRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
