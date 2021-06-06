from dataclasses import dataclass, field
from typing import List
from .catering_service_enumeration import CateringServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CateringServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CateringService_VersionStructure"

    service_list: List[CateringServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
