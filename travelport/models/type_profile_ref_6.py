from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_level_6 import TypeProfileLevel6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeProfileRef6:
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
    profile_level: None | TypeProfileLevel6 = field(
        default=None,
        metadata={
            "name": "ProfileLevel",
            "type": "Attribute",
            "required": True,
        }
    )
