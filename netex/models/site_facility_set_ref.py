from dataclasses import dataclass

from .site_facility_set_ref_structure import SiteFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFacilitySetRef(SiteFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
