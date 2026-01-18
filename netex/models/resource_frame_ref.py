from __future__ import annotations

from dataclasses import dataclass

from .resource_frame_ref_structure import ResourceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResourceFrameRef(ResourceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
