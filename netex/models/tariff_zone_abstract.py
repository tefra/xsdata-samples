from __future__ import annotations

from dataclasses import dataclass

from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneAbstract(ZoneVersionStructure):
    class Meta:
        name = "TariffZone_"
        namespace = "http://www.netex.org.uk/netex"
