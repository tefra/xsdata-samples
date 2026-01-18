from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_agency_profile_level_4 import (
    TypeAgencyProfileLevel4,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class TypeAgencyHierarchyReference4:
    class Meta:
        name = "typeAgencyHierarchyReference"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeAgencyProfileLevel4 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
