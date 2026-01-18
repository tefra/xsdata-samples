from __future__ import annotations

from dataclasses import dataclass

from .assistance_service_version_structure import (
    AssistanceServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceService(AssistanceServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
