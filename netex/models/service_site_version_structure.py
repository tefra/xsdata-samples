from dataclasses import dataclass
from netex.models.site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceSiteVersionStructure(SiteVersionStructure):
    class Meta:
        name = "ServiceSite_VersionStructure"
