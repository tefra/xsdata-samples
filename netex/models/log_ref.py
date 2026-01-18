from __future__ import annotations

from dataclasses import dataclass

from .log_ref_structure import LogRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogRef(LogRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
