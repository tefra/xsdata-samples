from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_level_4 import TypeProfileLevel4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeProfileRef4:
    """
    ProfileEntityID and ProfileLevel together identity a profile entity.
    """
    class Meta:
        name = "typeProfileRef"

    profile_entity_id: None | str = field(
        default=None,
        metadata={
            "name": "ProfileEntityID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_level: None | TypeProfileLevel4 = field(
        default=None,
        metadata={
            "name": "ProfileLevel",
            "type": "Attribute",
            "required": True,
        }
    )
