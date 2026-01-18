from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_frame_ref_structure import (
    MobilityServiceFrameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceFrameRef(MobilityServiceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
