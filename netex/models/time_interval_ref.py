from __future__ import annotations

from dataclasses import dataclass

from .time_interval_ref_structure import TimeIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalRef(TimeIntervalRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
