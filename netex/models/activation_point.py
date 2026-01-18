from __future__ import annotations

from dataclasses import dataclass

from .activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPoint(ActivationPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
