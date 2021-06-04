from dataclasses import dataclass
from netex.models.service_facility_set_version_structure import ServiceFacilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFacilitySet(ServiceFacilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
