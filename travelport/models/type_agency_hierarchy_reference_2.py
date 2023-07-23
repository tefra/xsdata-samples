from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_agency_profile_level_2 import TypeAgencyProfileLevel2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeAgencyHierarchyReference2:
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
    profile_type: None | TypeAgencyProfileLevel2 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
