from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairEndStructure:
    continuing_handrail: bool | None = field(
        default=None,
        metadata={
            "name": "ContinuingHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    textured_surface: bool | None = field(
        default=None,
        metadata={
            "name": "TexturedSurface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_contrast: bool | None = field(
        default=None,
        metadata={
            "name": "VisualContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
