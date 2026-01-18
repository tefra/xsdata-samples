from __future__ import annotations

from dataclasses import dataclass

from .navigation_path_ref_structure import NavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathRef(NavigationPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
