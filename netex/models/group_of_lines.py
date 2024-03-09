from dataclasses import dataclass

from .group_of_lines_version_structure import GroupOfLinesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLines(GroupOfLinesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
