from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    TelExplicit,
)
from ..core.voc import (
    NullFlavor,
    RoleClassContact,
)
from .coct_mt030203_uv02 import CoctMt030203Uv02Person
from .coct_mt150003_uv03 import CoctMt150003Uv03Organization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class CoctMt040203Uv01NotificationParty:
    class Meta:
        name = "COCT_MT040203UV01.NotificationParty"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    contact_organization: None | CoctMt150003Uv03Organization = field(
        default=None,
        metadata={
            "name": "contactOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    contact_person: None | CoctMt030203Uv02Person = field(
        default=None,
        metadata={
            "name": "contactPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassContact = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
