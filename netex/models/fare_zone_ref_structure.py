from __future__ import annotations

from dataclasses import dataclass

from .tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRefStructure(TariffZoneRefStructure):
    pass
