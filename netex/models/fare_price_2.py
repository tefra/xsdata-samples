from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePrice2(VersionedChildStructure):
    class Meta:
        name = "FarePrice_"
        namespace = "http://www.netex.org.uk/netex"
