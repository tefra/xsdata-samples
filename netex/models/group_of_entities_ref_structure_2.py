from dataclasses import dataclass, field
from typing import Optional
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesRefStructure2(VersionOfObjectRefStructure):
    class Meta:
        name = "GroupOfEntitiesRefStructure_"

    name_of_member_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfMemberClass",
            "type": "Attribute",
        },
    )
