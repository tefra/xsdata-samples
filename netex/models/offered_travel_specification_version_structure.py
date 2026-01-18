from __future__ import annotations

from dataclasses import dataclass

from .travel_specification_version_structure import (
    TravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OfferedTravelSpecificationVersionStructure(
    TravelSpecificationVersionStructure
):
    class Meta:
        name = "OfferedTravelSpecification_VersionStructure"
