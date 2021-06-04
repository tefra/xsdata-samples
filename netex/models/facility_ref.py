from dataclasses import dataclass
from netex.models.facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRef(FacilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
