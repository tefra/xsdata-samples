from __future__ import annotations

from dataclasses import dataclass

from .service_frame_ref_structure import ServiceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFrameRef(ServiceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
