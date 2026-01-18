from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .local_service_version_structure import LocalServiceVersionStructure
from .retail_service_enumeration import RetailServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "RetailService_VersionStructure"

    service_list: Iterable[RetailServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
