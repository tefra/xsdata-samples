from dataclasses import dataclass
from netex.models.group_of_timebands_ref_structure import GroupOfTimebandsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimebandsRef(GroupOfTimebandsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
