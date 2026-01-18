from __future__ import annotations

from dataclasses import dataclass

from .assistance_service_ref_structure import AssistanceServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceServiceRef(AssistanceServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
