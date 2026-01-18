from __future__ import annotations

from dataclasses import dataclass

from .fare_request_ref_structure import FareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RepeatedTripFareRequestRefStructure(FareRequestRefStructure):
    pass
