from __future__ import annotations

from dataclasses import dataclass

from .submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SubmodeRef(SubmodeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
