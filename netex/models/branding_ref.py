from __future__ import annotations

from dataclasses import dataclass

from .branding_ref_structure import BrandingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BrandingRef(BrandingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
