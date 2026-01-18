from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CallAbstract(VersionedChildStructure):
    class Meta:
        name = "Call_"
        namespace = "http://www.netex.org.uk/netex"
