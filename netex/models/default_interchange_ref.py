from __future__ import annotations

from dataclasses import dataclass

from .default_interchange_ref_structure import DefaultInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultInterchangeRef(DefaultInterchangeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
