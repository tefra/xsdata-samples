from __future__ import annotations

from dataclasses import dataclass

from .type_of_facility_ref_structure import TypeOfFacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFacilityRef(TypeOfFacilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
