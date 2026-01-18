from __future__ import annotations

from dataclasses import dataclass

from .class_in_frame_ref_structure import ClassInFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassInFrameRef(ClassInFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
