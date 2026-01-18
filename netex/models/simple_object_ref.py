from __future__ import annotations

from dataclasses import dataclass

from .simple_object_ref_structure import SimpleObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleObjectRef(SimpleObjectRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
