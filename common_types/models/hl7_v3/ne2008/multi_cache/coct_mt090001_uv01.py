from dataclasses import dataclass, field
from typing import List, Optional

from ..core.datatypes_base import (
    Ce,
    Cs,
    Ii,
)
from ..core.voc import (
    NullFlavor,
    RoleClassAssignedEntity,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt090001Uv01AssignedEntity:
    class Meta:
        name = "COCT_MT090001UV01.AssignedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[RoleClassAssignedEntity] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
