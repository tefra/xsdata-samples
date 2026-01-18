from __future__ import annotations

from dataclasses import dataclass

from .facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetRefStructure(FacilitySetRefStructure):
    pass
