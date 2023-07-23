from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_agency_profile_level_5 import TypeAgencyProfileLevel5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeAgencyHierarchyReference5:
    class Meta:
        name = "typeAgencyHierarchyReference"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: None | TypeAgencyProfileLevel5 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
