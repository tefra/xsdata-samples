from __future__ import annotations

from dataclasses import dataclass

from .line_network_version_structure import LineNetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineNetwork(LineNetworkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
