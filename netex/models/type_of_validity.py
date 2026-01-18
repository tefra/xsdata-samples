from __future__ import annotations

from dataclasses import dataclass

from .type_of_validity_value_structure import TypeOfValidityValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfValidity(TypeOfValidityValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
