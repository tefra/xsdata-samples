from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_version_frame_structure import (
    MobilityServiceVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityServiceFrame(MobilityServiceVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
