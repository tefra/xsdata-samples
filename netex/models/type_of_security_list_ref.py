from __future__ import annotations

from dataclasses import dataclass

from .type_of_security_list_ref_structure import TypeOfSecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfSecurityListRef(TypeOfSecurityListRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
