from __future__ import annotations

from dataclasses import dataclass

from .offered_travel_specification_ref_structure import (
    OfferedTravelSpecificationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OfferedTravelSpecificationRef(OfferedTravelSpecificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
