from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from netex.models.data_object_permissions import DataObjectPermissions
from netex.models.data_object_service_capabilities import DataObjectServiceCapabilities
from netex.models.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    data_object_service_capabilities: Optional[DataObjectServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "DataObjectServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_object_permissions: Optional[DataObjectPermissions] = field(
        default=None,
        metadata={
            "name": "DataObjectPermissions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        }
    )
