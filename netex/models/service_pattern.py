from __future__ import annotations

from dataclasses import dataclass

from .service_pattern_version_structure import ServicePatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicePattern(ServicePatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
