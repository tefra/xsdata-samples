from dataclasses import dataclass
from .group_of_timing_links_ref_structure import GroupOfTimingLinksRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimingLinksRef(GroupOfTimingLinksRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
