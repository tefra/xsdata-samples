from __future__ import annotations

from dataclasses import dataclass

from .service_version_frame_structure import ServiceVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFrame(ServiceVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
