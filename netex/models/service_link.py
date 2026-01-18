from __future__ import annotations

from dataclasses import dataclass

from .service_link_version_structure import ServiceLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLink(ServiceLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
