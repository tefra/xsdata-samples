from __future__ import annotations

from dataclasses import dataclass

from .taxi_stand_version_structure import TaxiStandVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiStand(TaxiStandVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
