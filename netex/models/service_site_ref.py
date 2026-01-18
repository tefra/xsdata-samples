from __future__ import annotations

from dataclasses import dataclass

from .service_site_ref_structure import ServiceSiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceSiteRef(ServiceSiteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
