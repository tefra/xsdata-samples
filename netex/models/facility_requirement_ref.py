from __future__ import annotations

from dataclasses import dataclass

from .facility_requirement_ref_structure import FacilityRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRequirementRef(FacilityRequirementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
