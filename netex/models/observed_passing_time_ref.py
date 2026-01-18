from __future__ import annotations

from dataclasses import dataclass

from .observed_passing_time_ref_structure import (
    ObservedPassingTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTimeRef(ObservedPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
