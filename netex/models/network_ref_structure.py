from dataclasses import dataclass

from .group_of_lines_ref_structure import GroupOfLinesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRefStructure(GroupOfLinesRefStructure):
    pass
