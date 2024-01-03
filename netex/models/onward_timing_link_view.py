from dataclasses import dataclass, field
from typing import Any
from .onward_timing_link_derived_view_structure import (
    OnwardTimingLinkDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardTimingLinkView(OnwardTimingLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    timing_link_in_journey_pattern_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
