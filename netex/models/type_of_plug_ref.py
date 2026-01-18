from __future__ import annotations

from dataclasses import dataclass

from .type_of_plug_ref_structure import TypeOfPlugRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPlugRef(TypeOfPlugRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
