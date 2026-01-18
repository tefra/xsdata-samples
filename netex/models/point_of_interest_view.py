from __future__ import annotations

from dataclasses import dataclass

from .point_of_interest_derived_view_structure import (
    PointOfInterestDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestView(PointOfInterestDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
