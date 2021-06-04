from dataclasses import dataclass
from netex.models.group_of_timing_links_rel_structure import GroupOfTimingLinksRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimingLinks(GroupOfTimingLinksRelStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
