from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_agency_profile_level_1 import (
    TypeAgencyProfileLevel1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeAgencyHierarchyReference1:
    class Meta:
        name = "typeAgencyHierarchyReference"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeAgencyProfileLevel1 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
