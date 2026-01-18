from __future__ import annotations

from dataclasses import dataclass

from .fare_frame_ref_structure import FareFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareFrameRef(FareFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
