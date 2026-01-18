from __future__ import annotations

from dataclasses import dataclass

from .complaints_service_ref_structure import ComplaintsServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsServiceRef(ComplaintsServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
