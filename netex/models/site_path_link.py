from dataclasses import dataclass
from netex.models.site_path_link_version_structure import SitePathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SitePathLink(SitePathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
