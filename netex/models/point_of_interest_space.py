from __future__ import annotations

from dataclasses import dataclass

from .point_of_interest_space_version_structure import (
    PointOfInterestSpaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpace(PointOfInterestSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
