from __future__ import annotations

from dataclasses import dataclass

from .quay_ref_structure import QuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayRef(QuayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
