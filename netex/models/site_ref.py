from __future__ import annotations

from dataclasses import dataclass

from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteRef(SiteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
