from __future__ import annotations

from dataclasses import dataclass

from .navigation_path_version_structure import NavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPath(NavigationPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
