from __future__ import annotations

from dataclasses import dataclass

from .passing_time_ref_structure import PassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeRef(PassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
