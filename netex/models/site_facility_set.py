from __future__ import annotations

from dataclasses import dataclass

from .site_facility_set_structure import SiteFacilitySetStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySet(SiteFacilitySetStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
