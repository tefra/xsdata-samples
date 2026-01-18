from __future__ import annotations

from dataclasses import dataclass

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointAbstract(PointVersionStructure):
    class Meta:
        name = "ActivationPoint_"
        namespace = "http://www.netex.org.uk/netex"
