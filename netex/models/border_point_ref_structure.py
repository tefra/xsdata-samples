from __future__ import annotations

from dataclasses import dataclass

from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointRefStructure(TimingPointRefStructure):
    pass
