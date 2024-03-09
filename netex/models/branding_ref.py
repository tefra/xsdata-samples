from dataclasses import dataclass

from .branding_ref_structure import BrandingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BrandingRef(BrandingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
