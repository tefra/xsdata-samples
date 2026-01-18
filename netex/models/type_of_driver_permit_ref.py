from __future__ import annotations

from dataclasses import dataclass

from .type_of_driver_permit_ref_structure import TypeOfDriverPermitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDriverPermitRef(TypeOfDriverPermitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
