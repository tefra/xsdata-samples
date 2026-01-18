from __future__ import annotations

from dataclasses import dataclass

from .duty_ref_structure import DutyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutyRef(DutyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
