from __future__ import annotations

from dataclasses import dataclass

from .taxi_service_place_assignment_ref_structure import (
    TaxiServicePlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiServicePlaceAssignmentRef(TaxiServicePlaceAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
