from __future__ import annotations

from dataclasses import dataclass

from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneRefAbstract(ZoneRefStructure):
    class Meta:
        name = "TariffZoneRef_"
        namespace = "http://www.netex.org.uk/netex"
