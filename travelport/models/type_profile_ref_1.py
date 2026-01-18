from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_level_1 import TypeProfileLevel1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeProfileRef1:
    """
    ProfileEntityID and ProfileLevel together identity a profile entity.
    """

    class Meta:
        name = "typeProfileRef"

    profile_entity_id: str = field(
        metadata={
            "name": "ProfileEntityID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_level: TypeProfileLevel1 = field(
        metadata={
            "name": "ProfileLevel",
            "type": "Attribute",
            "required": True,
        }
    )
