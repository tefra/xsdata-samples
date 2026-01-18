from __future__ import annotations

from dataclasses import dataclass

from .complaints_service_version_structure import (
    ComplaintsServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsService(ComplaintsServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
