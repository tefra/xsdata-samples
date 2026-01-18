from __future__ import annotations

from dataclasses import dataclass

from .single_trip_fare_request_ref_structure import (
    SingleTripFareRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleTripFareRequestRef(SingleTripFareRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
