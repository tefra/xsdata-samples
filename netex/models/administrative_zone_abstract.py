from __future__ import annotations

from dataclasses import dataclass

from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZoneAbstract(ZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone_"
        namespace = "http://www.netex.org.uk/netex"
