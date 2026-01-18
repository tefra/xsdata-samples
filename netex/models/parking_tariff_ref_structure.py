from __future__ import annotations

from dataclasses import dataclass

from .tariff_ref_structure import TariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingTariffRefStructure(TariffRefStructure):
    pass
