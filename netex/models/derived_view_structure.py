from dataclasses import dataclass, field

from .branding_ref import BrandingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DerivedViewStructure:
    branding_ref: BrandingRef | None = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
