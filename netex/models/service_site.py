from dataclasses import dataclass

from .service_site_version_structure import ServiceSiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceSite(ServiceSiteVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
