from __future__ import annotations

from dataclasses import dataclass

from .requested_travel_specification_version_structure import (
    RequestedTravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecification(
    RequestedTravelSpecificationVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
