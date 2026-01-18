from __future__ import annotations

from dataclasses import dataclass

from .estimated_passing_time_ref_structure import (
    EstimatedPassingTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeRef(EstimatedPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
