from __future__ import annotations

from dataclasses import dataclass

from .general_frame_ref_structure import GeneralFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameRef(GeneralFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
