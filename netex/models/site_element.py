from __future__ import annotations

from dataclasses import dataclass

from .site_element_version_structure import SiteElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteElement(SiteElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
