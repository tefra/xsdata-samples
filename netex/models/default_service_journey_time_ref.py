from __future__ import annotations

from dataclasses import dataclass

from .default_service_journey_time_ref_structure import (
    DefaultServiceJourneyTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultServiceJourneyTimeRef(DefaultServiceJourneyTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
