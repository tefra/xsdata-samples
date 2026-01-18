from __future__ import annotations

from dataclasses import dataclass, field

from .presentation_structure import PresentationStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BrandingVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "Branding_VersionStructure"

    presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
