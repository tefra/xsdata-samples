from __future__ import annotations

from dataclasses import dataclass

from .lost_property_service_version_structure import (
    LostPropertyServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LostPropertyService(LostPropertyServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
