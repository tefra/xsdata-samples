from __future__ import annotations

from dataclasses import dataclass

from .type_of_activation_ref_structure import TypeOfActivationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfActivationRef(TypeOfActivationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
