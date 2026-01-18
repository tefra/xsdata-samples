from __future__ import annotations

from dataclasses import dataclass

from .taxi_service_ref_structure import TaxiServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServiceRef(TaxiServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
