from __future__ import annotations

from dataclasses import dataclass

from .class_of_use_value_structure import ClassOfUseValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassOfUse(ClassOfUseValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
