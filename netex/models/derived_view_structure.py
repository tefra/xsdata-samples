from __future__ import annotations

from dataclasses import dataclass, field

from .branding_ref import BrandingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DerivedViewStructure:
    branding_ref: None | BrandingRef = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
