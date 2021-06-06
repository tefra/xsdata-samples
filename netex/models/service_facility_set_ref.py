from dataclasses import dataclass
from .service_facility_set_ref_structure import ServiceFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFacilitySetRef(ServiceFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
