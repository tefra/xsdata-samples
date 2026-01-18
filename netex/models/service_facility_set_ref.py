from __future__ import annotations

from dataclasses import dataclass

from .service_facility_set_ref_structure import ServiceFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetRef(ServiceFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
