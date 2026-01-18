from __future__ import annotations

from dataclasses import dataclass

from .scheduled_stop_point_derived_view_structure import (
    ScheduledStopPointDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointView(ScheduledStopPointDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
