from dataclasses import dataclass, field
from typing import Optional
from .presentation_structure import PresentationStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BrandingVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "Branding_VersionStructure"

    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
