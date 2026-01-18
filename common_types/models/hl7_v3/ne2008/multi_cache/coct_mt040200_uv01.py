from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
    TelExplicit,
)
from ..core.voc import (
    NullFlavor,
    RoleClassAgent,
)
from .coct_mt030200_uv import CoctMt030200UvPerson
from .coct_mt150000_uv02 import CoctMt150000Uv02Organization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class CoctMt040200Uv01ResponsibleParty:
    class Meta:
        name = "COCT_MT040200UV01.ResponsibleParty"

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
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    agent_organization: None | CoctMt150000Uv02Organization = field(
        default=None,
        metadata={
            "name": "agentOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    agent_person: None | CoctMt030200UvPerson = field(
        default=None,
        metadata={
            "name": "agentPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    represented_person: None | CoctMt030200UvPerson = field(
        default=None,
        metadata={
            "name": "representedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    represented_organization: None | CoctMt150000Uv02Organization = field(
        default=None,
        metadata={
            "name": "representedOrganization",
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
    class_code: RoleClassAgent = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
