from __future__ import annotations

from dataclasses import dataclass

from .schedule_request_ref_structure import ScheduleRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduleRequestRef(ScheduleRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
