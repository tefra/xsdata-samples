from __future__ import annotations

from dataclasses import dataclass

from .local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalService(LocalServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
