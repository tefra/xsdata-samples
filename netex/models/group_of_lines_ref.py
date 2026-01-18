from __future__ import annotations

from dataclasses import dataclass

from .group_of_lines_ref_structure import GroupOfLinesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinesRef(GroupOfLinesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
