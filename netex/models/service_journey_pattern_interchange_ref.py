from __future__ import annotations

from dataclasses import dataclass

from .service_journey_pattern_interchange_ref_structure import (
    ServiceJourneyPatternInterchangeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternInterchangeRef(
    ServiceJourneyPatternInterchangeRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
