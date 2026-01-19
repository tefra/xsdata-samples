from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .communication_service_enumeration import CommunicationServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CommunicationService_VersionStructure"

    service_list: Sequence[CommunicationServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
