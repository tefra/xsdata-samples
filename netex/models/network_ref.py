from __future__ import annotations

from dataclasses import dataclass

from .network_ref_structure import NetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRef(NetworkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
