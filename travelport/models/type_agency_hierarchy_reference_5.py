from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_agency_profile_level_5 import (
    TypeAgencyProfileLevel5,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class TypeAgencyHierarchyReference5:
    class Meta:
        name = "typeAgencyHierarchyReference"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeAgencyProfileLevel5 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
