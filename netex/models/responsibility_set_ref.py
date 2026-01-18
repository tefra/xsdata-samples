from __future__ import annotations

from dataclasses import dataclass

from .responsibility_set_ref_structure import ResponsibilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySetRef(ResponsibilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
