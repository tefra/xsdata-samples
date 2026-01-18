from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_level_3 import TypeProfileLevel3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class TypeProfileRef3:
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
    profile_level: TypeProfileLevel3 = field(
        metadata={
            "name": "ProfileLevel",
            "type": "Attribute",
            "required": True,
        }
    )
