from __future__ import annotations

from dataclasses import dataclass

from .time_interval_version_structure import TimeIntervalVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeInterval(TimeIntervalVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
