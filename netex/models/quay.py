from __future__ import annotations

from dataclasses import dataclass

from .quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Quay(QuayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
