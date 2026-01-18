from __future__ import annotations

from dataclasses import dataclass

from .group_of_lines_version_structure import GroupOfLinesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLines(GroupOfLinesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
