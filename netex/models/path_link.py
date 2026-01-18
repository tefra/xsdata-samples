from __future__ import annotations

from dataclasses import dataclass

from .path_link_version_structure import PathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLink(PathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
