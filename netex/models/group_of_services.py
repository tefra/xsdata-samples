from dataclasses import dataclass
from netex.models.group_of_services_version_structure import GroupOfServicesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServices(GroupOfServicesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
