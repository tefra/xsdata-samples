from dataclasses import dataclass
from netex.models.group_of_services_ref_structure import GroupOfServicesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServicesRef(GroupOfServicesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
