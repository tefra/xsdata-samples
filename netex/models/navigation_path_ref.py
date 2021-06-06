from dataclasses import dataclass
from .navigation_path_ref_structure import NavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathRef(NavigationPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
