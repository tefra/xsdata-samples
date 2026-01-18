from __future__ import annotations

from dataclasses import dataclass

from .turnaround_time_limit_time_ref_structure import (
    TurnaroundTimeLimitTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TurnaroundTimeLimitTimeRef(TurnaroundTimeLimitTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
