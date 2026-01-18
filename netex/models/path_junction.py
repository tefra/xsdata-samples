from __future__ import annotations

from dataclasses import dataclass

from .path_junction_version_structure import PathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunction(PathJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
