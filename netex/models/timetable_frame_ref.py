from __future__ import annotations

from dataclasses import dataclass

from .timetable_frame_ref_structure import TimetableFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetableFrameRef(TimetableFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
