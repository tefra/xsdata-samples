from dataclasses import dataclass, field
from typing import List

from .local_service_version_structure import LocalServiceVersionStructure
from .money_service_enumeration import MoneyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MoneyServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "MoneyService_VersionStructure"

    service_list: List[MoneyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "tokens": True,
        },
    )
