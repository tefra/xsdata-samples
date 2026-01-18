from __future__ import annotations

from dataclasses import dataclass

from .estimated_passing_time_view_structure import (
    EstimatedPassingTimeViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EstimatedPassingTimeView(EstimatedPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
