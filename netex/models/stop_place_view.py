from dataclasses import dataclass, field
from typing import Any

from .stop_place_derived_view_structure import StopPlaceDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceView(StopPlaceDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
