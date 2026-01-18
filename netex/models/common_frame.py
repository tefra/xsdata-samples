from __future__ import annotations

from dataclasses import dataclass

from .common_version_frame_structure import CommonVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonFrame(CommonVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
