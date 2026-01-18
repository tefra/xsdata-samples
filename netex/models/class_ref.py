from __future__ import annotations

from dataclasses import dataclass

from .class_ref_structure import ClassRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassRef(ClassRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
