from __future__ import annotations

from dataclasses import dataclass

from .trace_structure import TraceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Trace(TraceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
