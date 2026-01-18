from __future__ import annotations

from dataclasses import dataclass

from .facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRef(FacilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
