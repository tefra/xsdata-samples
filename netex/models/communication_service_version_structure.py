from dataclasses import dataclass, field
from typing import List
from netex.models.communication_service_enumeration import CommunicationServiceEnumeration
from netex.models.local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommunicationServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CommunicationService_VersionStructure"

    service_list: List[CommunicationServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
