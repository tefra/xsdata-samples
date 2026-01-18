from __future__ import annotations

from dataclasses import dataclass

from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPoint(TimingPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
