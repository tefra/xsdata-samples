from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_version_frame_structure import (
    InfrastructureVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureFrame(InfrastructureVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
