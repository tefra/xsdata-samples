from dataclasses import dataclass

from .site_connection_ref_structure import SiteConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteConnectionRef(SiteConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
