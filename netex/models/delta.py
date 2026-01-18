from __future__ import annotations

from dataclasses import dataclass

from .delta_structure import DeltaStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Delta(DeltaStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
