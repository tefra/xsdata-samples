from __future__ import annotations

from dataclasses import dataclass

from .trip_plan_request_ref_structure import TripPlanRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TripPlanRequestRef(TripPlanRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
