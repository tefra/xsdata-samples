from __future__ import annotations

from dataclasses import dataclass

from .operational_context_ref_structure import OperationalContextRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperationalContextRef(OperationalContextRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
