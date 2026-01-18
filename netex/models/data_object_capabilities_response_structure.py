from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_service_capabilities_response_structure import (
    AbstractServiceCapabilitiesResponseStructure,
)
from .data_object_permissions import DataObjectPermissions
from .data_object_service_capabilities import DataObjectServiceCapabilities
from .extensions_2 import Extensions2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectCapabilitiesResponseStructure(
    AbstractServiceCapabilitiesResponseStructure
):
    data_object_service_capabilities: None | DataObjectServiceCapabilities = (
        field(
            default=None,
            metadata={
                "name": "DataObjectServiceCapabilities",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    data_object_permissions: None | DataObjectPermissions = field(
        default=None,
        metadata={
            "name": "DataObjectPermissions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: None | Extensions2 = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )
