from __future__ import annotations

from dataclasses import dataclass

from .administrative_zone_ref_structure import AdministrativeZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZoneRef(AdministrativeZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
