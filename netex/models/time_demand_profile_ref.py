from __future__ import annotations

from dataclasses import dataclass

from .time_demand_profile_ref_structure import TimeDemandProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileRef(TimeDemandProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
