from __future__ import annotations

from dataclasses import dataclass

from .travel_specification_version_structure import (
    TravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecificationVersionStructure(
    TravelSpecificationVersionStructure
):
    class Meta:
        name = "RequestedTravelSpecification_VersionStructure"
