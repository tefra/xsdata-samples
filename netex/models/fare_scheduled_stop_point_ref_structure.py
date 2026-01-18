from __future__ import annotations

from dataclasses import dataclass

from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareScheduledStopPointRefStructure(ScheduledStopPointRefStructure):
    pass
