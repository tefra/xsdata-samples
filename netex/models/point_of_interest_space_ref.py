from __future__ import annotations

from dataclasses import dataclass

from .point_of_interest_space_ref_structure import (
    PointOfInterestSpaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpaceRef(PointOfInterestSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
