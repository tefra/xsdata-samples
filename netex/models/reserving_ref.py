from __future__ import annotations

from dataclasses import dataclass

from .reserving_ref_structure import ReservingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservingRef(ReservingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
