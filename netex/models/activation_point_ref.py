from __future__ import annotations

from dataclasses import dataclass

from .activation_point_ref_structure import ActivationPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointRef(ActivationPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
