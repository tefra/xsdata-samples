from __future__ import annotations

from dataclasses import dataclass

from .scheduled_stop_point_version_structure import (
    ScheduledStopPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPoint(ScheduledStopPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
