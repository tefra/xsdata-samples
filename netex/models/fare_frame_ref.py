from __future__ import annotations

from dataclasses import dataclass

from .fare_frame_ref_structure import FareFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareFrameRef(FareFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
