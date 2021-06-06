from dataclasses import dataclass, field
from typing import Optional
from .branding_ref import BrandingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DerivedViewStructure:
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
