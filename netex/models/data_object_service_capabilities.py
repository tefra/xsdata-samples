from __future__ import annotations

from dataclasses import dataclass

from .data_object_service_capabilities_structure import (
    DataObjectServiceCapabilitiesStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectServiceCapabilities(DataObjectServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
