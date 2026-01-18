from __future__ import annotations

from dataclasses import dataclass

from .catering_service_version_structure import CateringServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringService(CateringServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
