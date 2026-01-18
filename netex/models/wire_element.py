from __future__ import annotations

from dataclasses import dataclass

from .wire_element_version_structure import WireElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireElement(WireElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
